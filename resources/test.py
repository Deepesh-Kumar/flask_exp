
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel
import sqlite3



class ItemList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help="this cannot be blank")


    def get(self):
        a = ItemModel.query.all()
        items = []
        for row in a:
	    items.append({'name' :row[0], 'price':row[1]})
        return {'items': items}
