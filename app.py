import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
@app.route('/')
def main():
    return render template (Audio.html)	


@app.route('/', methods=['POST'])
def home():
    id = request.form["id"]
	name_of_song = request.form["name_of_song"]
	duration_in_seconds = request.form["duration_in_seconds"]
	Uploaded_time = request.form["Uploaded_time"]
	Host = request.form["Host"]
	Participants = request.form["Participants"]
	Title_of_the_audiobook =  request.form["Title_of_the_audiobook"]
	Author_of_the_title =  request.form["Author_of_the_title"]
	Narrator =  request.form["Narrator"]
	Duration_in_number_of_seconds =  request.form["Duration_in_number_of_seconds"]
	Uploaded_time =  request.form["Uploaded_time"]
	
	connection = sqlite3.connect(currentdirectory + "\Songfile.db")
	cursor = connection.cursor() 
	a= "INSERT INTO Songfile VALUES ({ID} , {name_of_song},  {duration_in_seconds}, {Uploaded_time}"
	b= "INSERT INTO Songfile VALUES ({ID} , {name_of_song},  {duration_in_seconds}, {Uploaded_time}, {Host}, {Participants}"
	c= "INSERT INTO Songfile VALUES ({ID} , {Title_of_the_audiobook},  {Author_of_the_title}, {Narrator}, {Duration_in_number_of_seconds}, {Uploaded_time}"
	if (query1 = a)
	cursor.execute (query1) 
	elif (query2 = b)
	cursor.execute (query2) 
	else (query3 = c
	cursor.execute (query3)  
	      
	      @app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    conn = sqlite3.connect('Songfile.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_books = cur.execute('SELECT * FROM books;').fetchall()
return jsonify(Songfile)
   

@app.route('/api/v1/resources/books/all', methods=['PUT'])
def api_all():
    conn = sqlite3.connect('Songfile.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_books = cur.execute('SELECT * FROMongfile ;').fetchall()
			   

    return jsonify(all_books)

@app.route('/api/v1/resources/books/all', methods=['DELETE'])
def api_all():
    conn = sqlite3.connect('books.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_books = cur.execute('SELECT * FROM books;').fetchall()
	
	
	@app.route('/api/v1/resources/books/all', methods=['READ'])
def api_all():
    conn = sqlite3.connect('books.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_books = cur.execute('SELECT * FROM books;').fetchall()

    return jsonify(songs)


    




@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/api/v1/resources/books', methods=['GET'])
def api_filter():
    query_parameters = request.args

    id = query_parameters.get('id')
    published = query_parameters.get('published')
    author = query_parameters.get('author')

    query = "SELECT * FROM books WHERE"
    to_filter = []

    if id:
        query += ' id=? AND'
        to_filter.append(id)
    if published:
        query += ' published=? AND'
        to_filter.append(published)
    if author:
        query += ' author=? AND'
        to_filter.append(author)
    if not (id or published or author):
        return page_not_found(404)

    query = query[:-4] + ';'

    conn = sqlite3.connect('books.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)

app.run()
