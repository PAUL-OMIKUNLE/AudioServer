from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'crud.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_of_song = db.Column(db.String(100), unique=True)
    Duration_in_seconds = db.Column(db.Integer, primary_key=True)
    Uploaded_time = db.Column(db.Datetime, primary_key=True)
    Participants = db.Column(db.String(100), unique=True)
    Title_of_the_audiobook = db.Column(db.String(100), unique=True)
    Author_of_the_title = db.Column(db.String(100), unique=True)
    Narrator = db.Column(db.String(100), unique=True)
    Host = db.Column(db.String(100), unique=True)

    def __init__(self, id,  name_of_song, Duration_in_seconds, Uploaded_time, Participants, Title_of_the_audiobook , Author_of_the_title, Narrator, Host):
        self.id = id
        self.name_of_song = name_of_song
        self.Duration_in_seconds = Duration_in_seconds
        self.Uploaded_time = Uploaded_time
        self.Participants = Participants
        self.Title_of_the_audiobook = Title_of_the_audiobook
        self.Author_of_the_title = Author_of_the_title
        self.Narrator = Narrator
        self.Host = Host


class AudioSchema(ma.Audio):
    class Meta:
        # Fields to expose
        fields = ('id', 'name_of_song', 'Duration_in_seconds', 'Uploaded_time', 'Participants', 'Title_of_the_audiobook', 'Author_of_the_title', 'Narrator', 'Host' )


audio_schema = AudioSchema()
audio_schema = AudioSchema(many=True)


# endpoint to create new audio
@app.route("/user", methods=["POST"])
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

    return jsonify(new_audio)


# endpoint to show all audio
@app.route("/user", methods=["GET"])
def get_audio():
    all_audio = Audio.query.all()
    result = audio_schema.dump(all_audio)
    return jsonify(result.data)


# endpoint to get audio detail by id
@app.route("/user/<id>", methods=["GET"])
def audio_detail(id):
     = Audio.query.get(id)
    return audio_schema.jsonify(user)


# endpoint to update audio
@app.route("/audio/<id>", methods=["PUT"])
def audio_update(id):
    audio = Audio.query.get(id)
    name_of_song = request.json['name_of_song']
    Duration_in_seconds = request.json['Duration_in_seconds']
    Uploaded_time = request.json['Uploaded_time']
    Participants = request.json['Participants']
    Title_of_the_audiobook = request.json['Title_of_the_audiobook']
    Author_of_the_title = request.json['Author_of_the_title']
    Narrator = request.json['Narrator']
    Host = request.json['Host']
    audio.email = email
    audio.username = username

    db.session.commit()
    return audio_schema.jsonify(user)


# endpoint to delete audio
@app.route("/user/<id>", methods=["DELETE"])
def audio_delete(id):
    audio = Audio.query.get(id)
    db.session.delete(audio)
    db.session.commit()

    return audio_schema.jsonify(user)
#error handling 
@app.errorhandler(200)
def Action_is_successful(e):
    return "<h1>200 OK</h1><p>Action is successful.</p>", 200

@app.errorhandler(400)
def The_request_is_invalid(a):
    return "<h1>400 OK</h1><p>The request is invalid.</p>", 400

@app.errorhandler(500)
def Any_error(b):
    return "<h1>500 OK</h1><p> internal server error .</p>", 500





if __name__ == '__main__':
    app.run(debug=True)
