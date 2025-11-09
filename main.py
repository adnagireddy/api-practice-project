from flask import Flask, jsonify, request 
from flask_sqlalchemy import SQLAlchemy

"""
API framework => platforms with libs tools, pre-built components to help build APIs 
    - Springboot (JAVA)
    - FastAPI, Falcon (python) 
    - Echo (Go) 
    - .NET COre (C#)
    - Ruby on Rails (Ruby)

Flask = api microframework for python based applications 
    - is lightweight = much more lightweight compared to general api frameworks 
    - intended for developers who work in pyhon and want to integrate python libs into API 
    -enables
        - request handling 
        - routing 
        - dynamic web pages throgh Jinjia2 template 
        - responses 


Flask_SQLAlchemy => an extension of flask that enables an app to use SQLALchemy 

SQLAlchemy => an open=source Python lib that provies an SQL toolkit, and an OBJECT RELATIONAL MAPPER 
    - TLDR; makes using SQL an OOP process, easy to use as a dev without having to use extensive SQL

-------------------------------------------------------{PAGE BREAK}-----------------------------------------------------------------------------------------------
"""
app = Flask(__name__) # __name__ is a special var that holds the name of the current module, lets Flask identify relevant files and dependancies to use 

# 1. create a database 
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ananya-travel.db" # we have configured our flask app to access a sqlite db

db = SQLAlchemy(app) # create empty db

# 1a. create a model (i.e. the structure for db, holds a row)
class Destination(db.Model):
    #below, we define our columns 
    id = db.Column(db.Integer, primary_key=True) # setting id to be primary key of our DB
    destination = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Float(), nullable=False)
    
    def to_dict(self):  # this helper function enables returning output to JSON 

        return {
            "id": self.id,
            "destination" : self.destination,
            "country" : self.country,
            "rating": self.rating
        }

# 3. Create a ContextManager 
"""
context manager: a python object that ensures that ensures resurces are set up before executing a particular block of code. 
The syntax for using a context manager is "with ____ as __ :". Allows you to return the resource 

app_context(): method that pushes an application context onto the application context stack. 
This is reqired to make queries and to access db methods

application context: the environment (set of data) within which an app operates in. The data
defines how an API interacts and works within a specific app.
When an app is accessed through its endpoints, app context is generated 
"""
with app.app_context():
    db.create_all()

# 2. create routes 
""" 
API routes => the link you put in your browser to access a server 
- Formal Definition: the defined paths and CRUD methods in an API. 
- path + method + query logic = api route  
used to access API endpoints, used in API URLs 
- a feature of api frameworks, allows devs to create server-side API endpoints within an app's codebase 
- api routes neable creating backend API parallel to frontend code within the same directory 
- instead of being executed on client, they are executed on the server
    - this is good for handling sensitive data, enablong an app to interact with DBs, perform server-side logic 

"""

# https://wwww.websitedomain.com/
@app.route("/") # we are using a decorator that takes in to set home route 
def home():
    return jsonify({"message" : "Hai :3"}) # we want to return JSON objects 

#https://www.websitedomain.com/desintations
@app.route("/destinations", methods=["GET"])
def get_destinations():
    destinations = Destination.query.all()
    return jsonify([destination.to_dict()] for destination in destinations) 

#FOR THE ROUTES BELOW, THIS IS THE URL: https://www.websitedomain.com/desintations/<int:destination_id> -> this would be a single destination

# GET => retrieve an existing  destination 
@app.route("/destinations/<int:destination_id>", methods=["GET"])
def get_destination(destination_id):
    destination = Destination.query.get(destination_id)
    if destination:
        return jsonify(destination.to_dict())
    else:
        return jsonify({"error" : " Destination not found "}), 404

# POST => create a new destination and add to endpoint 
@app.route("/destinations/<int:destination_id>", methods=["POST"])
def add_destinations():
    data = request.get_json()

    new_dest = Destination(destination=data["destination"],
                          country=data["country"],
                          rating = data["rating"])
    db.session.add(new_dest)
    db.session.commit()

    return jsonify(new_dest.to_dict()), 200

# PUT => modify an exisiting destination 
@app.route("/destinations/<int:destination_id>", methods=["PUT"])
def update_destination(destination_id):
    data = request.get_json()
    destination = Destination.query.get(destination_id)
    if destination:
        destination.destination = data.get("destination", destination.destination)
        destination.country = data.get("country", destination.country)
        destination.rating = data.get("rating", destination.rating)

        db.session.commit()
        return jsonify(destination.to_dict()), 200
    else:
        return jsonify({"error" : "Destination not found"}), 404
    

# DELETE => delete an exisitng destination from an endpoint 
@app.route("/destinations/<int:destination_id>", methods=["DELETE"])
def delete_destination(destination_id):
    destination = Destination.query.get(destination_id)
    if destination: 
        db.session.delete(destination)
        db.session.commit()

        return jsonify({"message" : "destination was deleted"}), 200
    else:
        return jsonify({"error":"Destination not found"}), 400

if __name__ == "__main__":
    app.run(debug = True, port=5001) # runs flask dev if current module is main.py, debug=True will constantly update for changes, automatically runs on port 5000  
