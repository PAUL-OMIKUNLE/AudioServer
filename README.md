# AudioServer
For short code above will have 4 endpoints with capabilities to create new record, get all records from database, get record detail by id, update selected record, and delete selected record. Also on this code we define model for our database.
# Let’s take a look to the code part by part
 <br> **from flask import Flask, request, jsonify
 <br> from flask_sqlalchemy import SQLAlchemy
 <br> from flask_marshmallow import Marshmallow
 <br> import os**
 
 <br>On this part we import all module that needed by our application. We import Flask to create instance of web application, request to get request data, jsonify to turns the JSON output into a Response object with the application/json mimetype, SQAlchemy from flask_sqlalchemy to accessing database, and Marshmallow from flask_marshmallow to serialized object.
 
 (<br>)  **app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'crud.sqlite')**
