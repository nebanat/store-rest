from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from resources.item import Item, ItemList
from resources.store import Store, StoreList

from resources.user import UserRegister

from security import authenticate, identity

app = Flask(__name__)

app.config.from_object('config.settings')
app.config.from_pyfile('settings.py', silent=True)

api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)  # creates endpoint /auth

# add  all resources
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
