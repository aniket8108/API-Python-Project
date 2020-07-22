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


@app.route('/', methods=['GET'])
def home():
    return '''<h1>API</h1>
<p>You have Entered API</p>'''


@app.route('/news', methods=['GET'])
def api_all():
    conn = sqlite3.connect('datanews.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_books = cur.execute('SELECT * FROM news;').fetchall()

    return jsonify(all_books)
	
@app.route('/news/id/<id>', methods=['GET'])
def getEvalByID(id):
    conn = sqlite3.connect('datanews.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    cur.execute('select * from news where id=' +(id))
    res = cur.fetchall()
    return jsonify({'test':(res)})
	
	



@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

app.run()
