from random import  choice as rc, sample
from faker import Faker
from app import app
from models import db, Restaurant, RestaurantPizza, Pizza
import random

#defined a list of the restaurant names
restaurant_names = [
    "Pasta Paradise",
    "Burger Bliss",
    "Pizza Palace",
    "Sushi Sensation",
    "Taco Time",
    "Steakhouse Supreme",
    "Chinese Delight",
    "Indian Spice",
    "Mediterranean Magic",
    "Vegetarian Vibes",
    "Seafood Shack",
    "BBQ Barn",
    "Greek Grill",
    "Café Express",
    "Deli Delight",
    "Thai Treats",
    "Southern Comfort",
    "Wok and Roll",
    "Noodle Nation",
    "Bakery Bliss",
    "Bistro Bon Appétit",
    "Crepes and Cravings",
    "Samosa Street",
    "Taste of Tuscany",
    "Brewery Bites",
    "Diner Delights",
    "Bagel Haven",
    "Waffle Wonders",
    "Ice Cream Oasis",
    "Donut Dreams",
]
#defined a list of ingredients
ingredients = [
    "Pepperoni",
    "Mushrooms",
    "Bell peppers",
    "Onions",
    "Black olives",
    "Sausage",
    "Fresh basil",
    "Pineapple",
    "Ham",
    "Spinach",
    "Feta cheese",
    "Sun-dried tomatoes",
    "Anchovies",
    "Arugula",
    "Provolone cheese",
    "Artichoke hearts",
    "Goat cheese",
    "Garlic",
    "Jalapeños",
    "Ricotta cheese",
    "Red pepper flakes",
    "Fresh tomatoes",
    "Bacon",
    "Mozzarella cheese",
    "Fresh oregano",
    "Capers",
    "Chicken",
    "Parmesan cheese",
    "Gorgonzola cheese",
    "Fresh cilantro",
]

fake = Faker()
# a context manager to ensure database operations occur within the application context
with app.app_context():
    #delete existing data from tables
    db.session.query(RestaurantPizza).delete()
    db.session.query(Restaurant).delete()
    db.session.query(Pizza).delete()
    #initialize an empty list
    restaurants = []
    for i in range(100):
        r = Restaurant(
            name = fake.company(),
            address = fake.address()
        )
        restaurants.append(r)
        
    db.session.add_all(restaurants)
    db.session.commit()
    #initialize an empty list
    pizzas = []
    for i in range(100):
        p = Pizza(
            #get a random ingredient from the ingredient list to be used as the name of the pizza
            name =rc(ingredients),
            #create a random list of 3 ingredients joined to a single string
            ingredients =','.join(sample(ingredients,3)),            
        )
        pizzas.append(p)
        
    db.session.add_all(pizzas)
    db.session.commit()
    
    restaurant_pizzas = []
    for i in range(10) : 
        rp =  RestaurantPizza(
            name=fake.unique.company(), #generate a unique company name using faker 
            price=random.randint(1, 30),#generate a random price   
            pizza_id=rc(pizzas).id, #select a random pizza object from the pizza list 
            restaurant_id=rc(restaurants).id)   #select a random restaurant object from the restaurants list 
        restaurant_pizzas.append(rp)
     
    db.session.add_all(restaurant_pizzas)
    db.session.commit()
