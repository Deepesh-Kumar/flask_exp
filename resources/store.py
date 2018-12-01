from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):
    def get(self, name):
	store = StoreModel.find_By_name(name) #may return a store object or none
	if store:
	    return store.json(), 200
	return {'message': 'Store not found'}, 404 # we return a tuple of dictionary and the status code

    def post(self, name):
	if StoreModel.find_By_name(name):
	    return {'message': 'Store already there'}
        store = StoreModel(name)
        try:
	    store.save_to_db()
	except:
 	    return {'message': 'Error occured'}, 500
	return store.json()


    def delete(self, name):
	store = StoreModel.find_By_name(name)
	if store:    
	    store.delete_from_db()
	return {'message': 'Store Deleted'}


class StoreList(Resource):
    def get(self):
	a = StoreModel.query.all()
        for store in a:
            return {'stores': store.json()}	
