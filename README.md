 # Flask Pizza Restaurant API

Introduction
This Flask API allows you to manage pizza restaurants and their pizza offerings. You can create, read, update, and delete restaurants, pizzas, and their associations using the provided endpoints. Additionally, there are validations in place to ensure data integrity.

## Technologies Used
The following technologies have been used in this project:

- [Python3](https://docs.python.org/3.10/)
- [Flask](https://flask.palletsprojects.com/en/2.3.x/)
- [Pytest](https://docs.pytest.org/en/latest/contents.html)
- [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/quickstart/)
- [Flask Migrate](https://flask-migrate.readthedocs.io/en/latest/)
- [Flask Restful](https://flask-restful.readthedocs.io/en/latest/)
- [Flask Marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/)
- [Faker](https://faker.readthedocs.io/en/master/)

## Project Setup
- Clone the repository:
git clone <repository-url>

- Navigate to the cloned repository:
cd pizza_restaurants-challenge

-  Create a Pipenv environment and install dependencies:
pipenv install

- Activate the environment:
pipenv shell

- Set environment variables:
export FLASK_APP=run.py
export FLASK_RUN_PORT=5555

- Create the database with Flask Migrate:
cd app
flask db upgrade head

- Populate the database with seed data:
cd ..
python3 seed.py

- Start the Flask application:
python run.py

## Endpoints

**GET /restaurants**
Returns a list of restaurants in JSON format:

json

[
  {
    "id": 1,
    "name": "Dominion Pizza",
    "address": "Good Italian, Ngong Road, 5th Avenue"
  },
  {
    "id": 2,
    "name": "Pizza Hut",
    "address": "Westgate Mall, Mwanzi Road, Nrb 100"
  }
]

**GET /restaurants/:id**
Returns information about a specific restaurant in JSON format, including its pizzas:

json

{
  "id": 1,
  "name": "Dominion Pizza",
  "address": "Good Italian, Ngong Road, 5th Avenue",
  "pizzas": [
    {
      "id": 1,
      "name": "Cheese",
      "ingredients": "Dough, Tomato Sauce, Cheese"
    },
    {
      "id": 2,
      "name": "Pepperoni",
      "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
    }
  ]
}

**DELETE /restaurants/:id**
Deletes a restaurant by ID, along with associated RestaurantPizzas. Returns an empty response body on success.

**GET /pizzas**
Returns a list of available pizzas in JSON format:

json

  {
    "id": 1,
    "name": "Cheese",
    "ingredients": "Dough, Tomato Sauce, Cheese"
  },
  {
    "id": 2,
    "name": "Pepperoni",
    "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
  }
]

**POST /restaurant_pizzas**
Creates a new RestaurantPizza association between an existing pizza and restaurant. Requires the following JSON data in the request body:

json

{
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 3
}
Returns information about the associated pizza on success or validation errors on failure.

## Running Tests
To run tests, use pytest:
pytest

## Usage
You can use Postman or other API testing tools to interact with the endpoints provided by the API.

## AUTHORS

- [Gift Kimani](https://github.com/kimani56)

## Copyright

Released under the MIT License.