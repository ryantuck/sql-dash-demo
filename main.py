# ================================================================
#
#   MVP SQL stored query app
#
# ================================================================

import json

from flask import Flask
from flask import render_template
from flask import jsonify

from db import *

app = Flask(__name__)

# load up basic db config from a dummy RDS instance i own
with open('db_config.json') as f:
    db_config = json.load(f)['db']

db = DsDb(db_config)

# ================================================================
# load up our page with stored data and current time
# ================================================================
@app.route('/')
def hello_world():

    return render_template('index.html',**locals())

@app.route('/test', methods=['GET'])
def do_something():

    print 'get request received from front-end'

    return 'here is data'

@app.route('/get-table', methods=['GET'])
def return_table():

    q = 'select * from puppies'
    t = db.html_table(q)
    return t

@app.route('/all-queries',methods=['GET'])
def return_queries_list():

    q = 'select * from queries_master'
    r = { 'results': db.list_of_lists(q)}
    return jsonify(r)

@app.route('/query/<query_number>', methods=['POST'])
def return_query_results(query_number):

    q_string = 'select query from queries_master where id = ' + str(query_number)

    q = db.val(q_string)
    t = db.html_table(q)
    return t

# ================================================================
# actually fire up app!
# ================================================================
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

