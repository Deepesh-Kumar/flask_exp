
import os
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT, jwt_required
from security import authenticate, identity
from resources.user1 import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from flask_restful import Api




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPOGATE_EXCEPTIONS'] = True
app.secret_key = 'deepesh'
api = Api(app)


jwt = JWT(app, authenticate, identity)





items = []



 
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(User, '/user/<int:user_id>'')



if __name__ == '__main__':

    from db import db
    db.init_app(app)
    app.run(host='0.0.0.0', debug=True)



