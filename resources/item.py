from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel
import sqlite3


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help="this cannot be blank")
    parser.add_argument('store_id', type=int, required=True, help="this cannot be blank")

    def get(self,name):
        item = ItemModel.find_By_name(name)
	if item:
	    return item.json()
 	else:
	    return {'message': 'Item not found'}, 404

    def post(self, name):
        if ItemModel.find_By_name(name):
	    return {'message':'This item Already exists'}, 400
    	data = Item.parser.parse_args()
        item = ItemModel(name, data['price'], data['store_id'])
 	try:
	    item.save_to_db()
        except:
	    return {'message':'An error occured'}, 500


    def delete(self,name):
	item = ItemModel.find_By_name(name)
	if item is not None:
	    item.delete_from_db()
	return {'message':'The item was deleted'}



    def put(self, name):
        data = Item.parser.parse_args()
	item = ItemModel.find_By_name(name)
	if item is None:
	    item = ItemModel(name, data['price'], data['store_id'])
	else:
	    item.price = data['price']
	item.save_to_db()
	return item.json()
	



class ItemList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help="this cannot be blank")


    def get(self):
        a = ItemModel.query.all()
        items = []
	for item in a:
            return {'items': item.json()}
