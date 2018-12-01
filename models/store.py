from db import db


class StoreModel(db.Model):

    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    items = db.relationship('ItemModel', lazy='dynamic')	

    def __init__(self,name):
        self.name=name

    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}


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
