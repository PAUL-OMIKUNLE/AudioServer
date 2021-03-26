# AudioServer
For short code above will have 4 endpoints with capabilities to create new record, get all records from database, get record detail by id, update selected record, and delete selected record. Also on this code we define model for our database.
# Let’s take a look to the code part by part
 <br> **from flask import Flask, request, jsonify
 <br> from flask_sqlalchemy import SQLAlchemy
 <br> from flask_marshmallow import Marshmallow
 <br> import os**
 
 <br>On this part we import all module that needed by our application. We import Flask to create instance of web application, request to get request data, jsonify to turns the JSON output into a Response object with the application/json mimetype, SQAlchemy from flask_sqlalchemy to accessing database, and Marshmallow from flask_marshmallow to serialized object.
 
<br> **app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'crud.sqlite')**

<br> This part create an instances of our web application and set path of our SQLite uri.
<br>**db = SQLAlchemy(app)
<br>ma = Marshmallow(app)**
<br>On this part we binding SQLAlchemy and Marshmallow into our flask application.

<br>**class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_of_song = db.Column(db.String(100), unique=True)
    Duration_in_seconds = db.Column(db.Integer, primary_key=True)
    Uploaded_time = db.Column(db.Datetime, primary_key=True)
    Participants = db.Column(db.String(100), unique=True)
    Title_of_the_audiobook = db.Column(db.String(100), unique=True)
    Author_of_the_title = db.Column(db.String(100), unique=True)
    Narrator = db.Column(db.String(100), unique=True)
    Host = db.Column(db.String(100), unique=True)**

<br>  **def __init__(self, id,  name_of_song, Duration_in_seconds, Uploaded_time, Participants, Title_of_the_audiobook , Author_of_the_title, Narrator, Host):
        self.id = id
        self.name_of_song = name_of_song
        self.Duration_in_seconds = Duration_in_seconds
        self.Uploaded_time = Uploaded_time
        self.Participants = Participants
        self.Title_of_the_audiobook = Title_of_the_audiobook
        self.Author_of_the_title = Author_of_the_title
        self.Narrator = Narrator
        self.Host = Host**
        
<br>   This part defined structure of response of our endpoint. We want that all of our endpoint will have JSON response. Here we define that our JSON response will have 9 keys(id,  name_of_song, Duration_in_seconds, Uploaded_time,  Participants, Title_of_the_audiobook, Author_of_the_title,  Narrator, and Host ). Also we defined user_schema as instance of UserSchema, and user_schemas as instances of list of UserSchema.     


<br> **@app.route("/user", methods=["POST"])
def add_user():
    #insert null where it not apllicable
    id = request.json['id']
    name_of_song = request.json['name_of_song']
    Duration_in_seconds = request.json['Duration_in_seconds']
    Uploaded_time = request.json['Uploaded_time']
    Participants = request.json['Participants']
    Title_of_the_audiobook = request.json['Title_of_the_audiobook']
    Author_of_the_title = request.json['Author_of_the_title']
    Narrator = request.json['Narrator']
    Host = request.json['Host']
    new_audio = audio('id', 'name_of_song', 'Duration_in_seconds', 'Uploaded_time', 'Participants', 'Title_of_the_audiobook', 'Author_of_the_title', 'Narrator', 'Host' )

    db.session.add(new_audio)
    db.session.commit()


 <br> On this part we define endpoint to create new user. First we set the route to “/user” and set HTTP methods to POST. After set the route and methods we define function that will executed if we access this endpoint. On this function first we get username and email from request data. After that we create new user using data from request data. Last we add new user to data base and show new user in JSON form as response.
    
