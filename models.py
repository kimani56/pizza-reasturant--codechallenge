from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'
    
    serialize_rules = ('-pizzas.restaurant','-restaurant.pizzas')
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),nullable= False,unique= True)
    address = db.Column(db.String)
    
    pizzas = db.relationship('RestaurantPizza',backref='restaurants')
    
    @validates("name")
    def validate_name(self, key, name):
        if  len(name) > 50:
            raise ValueError("Name must be less than 50 characters")
        return name
    
class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizzas'
    
    serialize_rules = ('-restaurants.pizza','-restaurant.pizzas')
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ingredients = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    restaurants = db.relationship('RestaurantPizza',backref='pizzas')

class RestaurantPizza(db.Model, SerializerMixin):
    __tablename__ = 'restaurant_pizzas'
    
    serialize_rules = ('restaurant','pizza')
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # restaurant1 = db.relationship('RestaurantPizza',back_populates='restaurants')
    # pizza1 = db.relationship('RestaurantPizza',back_populates='pizzas')

    @validates("price")
    def validate_price(self, key, value):
        if not (1 <= value <= 30):
            raise ValueError("Price must be between 1 and 30")
        return value