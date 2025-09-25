from flask import Flask 
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

# 1a. create a model (i.e. the strucutre for db, holds a row)
class Destination(db.Model):
    #below, we define our columns 
    id = db.Column(db.Integer, primary_key=True) # setting id to be primary key of our DB
    destination = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Float(), nullable=False)
    
    # this helper function enables returning output to JSON 
    def to_dict(self):
        return {
            "id": self.id,
            "destination" : self.destination,
            "country" : self.country,
            "rating": self.rating
        }

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
@app.route("/") # we are using a decorator that takes in to set home route 
def home():
    return "hai :3" # we want to return JSON objects 

if __name__ == "__main__":
    app.run(debug = True) # runs flask dev if current module is main.py, debug=True will constantly update for changes  

