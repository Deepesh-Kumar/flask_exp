from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from db import db


class ItemModel(db.Model):

	



    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help="this cannot be blank")

    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')




    def __init__(self,name, price, store_id):
        self.name=name
        self.price = price
	self.store_id = store_id

    def json(self):
        return {'name': self.name, 'price': self.price}
	

    @classmethod
    def find_By_name(cls,name):
	return cls.query.filter_by(name=name).first() #we can build queries using this query builder ItemModel is the class, we query the model and we build the query on db 
							#same as SELECT * FROM {table_name} WHERE item={} (name=name) LIMIT 1 no need to connect every single time in this
							#return a ItemModel object

    def save_to_db(self):
	db.session.add(self) #we have to say to insert the objectno need to convert it the session is a collection of objects to write to the database
	db.session.commit() #when we get an object from db that has an id then we can change the name sql alchemy will do an update and the insert 

    def delete_from_db(self):
	db.session.delete(self)
	db.session.commit()
