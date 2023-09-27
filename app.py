from flask import Flask, make_response,jsonify,request
from flask_migrate import Migrate
from flask_restful import Api,Resource
from models import db, Restaurant, Pizza, RestaurantPizza
from flask_swagger_ui import get_swaggerui_blueprint
# from werkzeug.exceptions import NotFound

app = Flask(__name__)

SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = '/static/swagger.json'  # Our API url (can of course be a local resource)


# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Test application"
    },
    # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
    #    'clientId': "your-client-id",
    #    'clientSecret': "your-client-secret-if-required",
    #    'realm': "your-realms",
    #    'appName': "your-app-name",
    #    'scopeSeparator': " ",
    #    'additionalQueryStringParams': {'test': "hello"}
    # }
)

app.register_blueprint(swaggerui_blueprint)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'#specifies the URI for the sqlite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)
api= Api(app)#create an instance of the Flask-restful API extension 
[]
#define a new class home
#Resource class is used to define how different http methods shold be handled
class Home(Resource):
    def get(self):
        
        response_dict ={
            "message":"Welcome to my Flask Code Challenge - Pizza Restaurants",
        }
        
        response = make_response(
            response_dict,
            200    
        )
        return response
api.add_resource(Home, '/')

class Restaurants(Resource):
    def get(self):
        #initialize an empty list
        restaurants = []
        for restaurant  in Restaurant.query.all():
            #resturant_dict is used to store information about a single restaurant 
            restaurant_dict={
                "id": restaurant.id,
                "name": restaurant.name,
                "address": restaurant.address
            }
            restaurants.append(restaurant_dict)
        return make_response(jsonify(restaurants), 200)

api.add_resource(Restaurants,'/restaurants')  
 
class RestaurantByID(Resource):

    def get(self, id):
        restaurant = Restaurant.query.filter_by(id=id).first()
        if restaurant:
            restaurant_dict=restaurant.to_dict()
            return make_response(jsonify(restaurant_dict), 200)
        else:
            return make_response(jsonify({"error": "Restaurant not found"}), 404)


    def delete(self,id):
        restaurant = Restaurant.query.filter_by(id=id).first()
        if restaurant:
            db.session.delete(restaurant)
            db.session.commit()
            return make_response(jsonify({"message":"Restaurant succesfully deleted"}), 204)
        else:
            return make_response(jsonify({"error": "Restaurant not found"}), 404)



api.add_resource(RestaurantByID, '/restaurants/<int:id>')

class Pizzas(Resource):

    def get(self):
        pizzas = []
        for pizza in Pizza.query.all():
            pizza_dict={
                "id": pizza.id,
                "name": pizza.name,
                "ingredients": pizza.ingredients
            }
            pizzas.append(pizza_dict)
        return make_response(jsonify(pizzas), 200)
api.add_resource(Pizzas, '/pizzas')

class RestaurantPizzas(Resource):
    def post(self):
        data = request.get_json()#retrieve json data from the http request body

        # Validate that the required fields are present in the request
        if not all(key in data for key in ("price", "pizza_id", "restaurant_id")):
            return make_response(jsonify({"errors": ["validation errors.include all keys"]}), 400)

        price = data["price"]
        pizza_id = data["pizza_id"]
        restaurant_id = data["restaurant_id"]

        # Check if the Pizza and Restaurant exist in the database based on their respective ids
        pizza = Pizza.query.get(pizza_id)
        restaurant = Restaurant.query.get(restaurant_id)


        if not pizza or not restaurant:
            return make_response(jsonify({"errors": ["validation errors pizza and restaurant dont exist"]}), 400)

        # Create a new RestaurantPizza
        restaurant_pizza = RestaurantPizza(
            price = data["price"],
            pizza_id = data["pizza_id"],
            restaurant_id = data["restaurant_id"]

        )

        db.session.add(restaurant_pizza)
        db.session.commit()

        # Return data related to the Pizza
        pizza_data = {
            "id": pizza.id,
            "name": pizza.name,
            "ingredients": pizza.ingredients
        }

        return make_response(jsonify(pizza_data), 201)
api.add_resource(RestaurantPizzas,'/restaurant_pizzas')   
 
# @app.errorhandler(NotFound)
# def handle_not_found(e):
#     response = make_response(
#         "Not Found: The requested resource does not exist.",
#         404
#     )
#     return response


if __name__ == '_main_':
    app.run(port=5555, debug=True)