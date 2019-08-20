from flask import Flask, jsonify, request
import pymongo
from flask_cors import CORS
from pymongo import MongoClient
import req
import conexion
import dummy

app = Flask(__name__)
cors = CORS(app)

client = pymongo.MongoClient('DB')
db1 = client.db_users
users = db1.users

db2 = client.db_interactions
interactions = db2.interaction


@app.route('/v1/interactions')
def index():
    result = conexion.getTickets(interactions,users)
    return jsonify(result)

@app.route('/v1/users')
def get_ti():
    result = conexion.getDataUsers(users)
    return jsonify(result)


@app.route('/v1/filter_interaction')
def get_filter_interaction():
    id_interaction = request.args.get('id_interaction')
    result = conexion.getFilterIdInteraction(interactions,users,id_interaction)
    return jsonify(result)


@app.route('/v1/filter')
def filter2():
    id_user = request.args.get('id_user')
    id_priority = request.args.get('id_priority')
    id_status = request.args.get('id_status') 
    print('user'+id_user+'pri'+id_priority+'st'+id_status)
    result = conexion.getFilter(interactions,users,id_user,id_priority,id_status)
    return jsonify(result)

#---------------------------------------------------------------#

@app.route('/v1/import_users')
def import_users():
    result = req.importUsers(users)
    return jsonify(result)

@app.route('/v1/create_interactions')
def create_interactions():
    num = request.args.get('num')
    result = req.createTickets(users,num)
    return jsonify(result)

@app.route('/v1/import_interactions')
def import_interactions():
    result = req.importInteractions(interactions)
    return jsonify(result)

#----------------------------------------------------#

@app.route('/v1')
def test():
    result = []
    #db1.users.drop()
    #db2.interaction.drop()
    result = req.test()
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug = True)