import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for publishdatex, col in enumerate(cursor.description):
        d[col[0]] = row[publishdatex]
    return d


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Hello Aniket</h1>
<p>You have Entered to API</p>'''


@app.route('/newslist', methods=['GET'])
def api_all():
    conn = sqlite3.connect('datanew.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_news = cur.execute('SELECT * FROM new order by date(publishdate) asc;').fetchall()
    return jsonify(all_news)
	
@app.route('/newslist/title/<title>', methods=['GET'])
def getEvalBytitle(title):
    conn = sqlite3.connect('datanew.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    cur.execute('select * from new where title=' +(title))
    res = cur.fetchall()
    return jsonify({'news':(res)})
	


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

app.run()
