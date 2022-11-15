from flask import request
from indexes.indexes import PLAYER
from app import app, es
from routes.base_routes import get_all, handle_single_result


@app.route('/actors/players/')
def get_all_players():
    return get_all(es, PLAYER)


@app.route('/actors/players/<name>', methods=['POST', 'GET', 'PUT'])
def handle_players(name):
    return handle_single_result(es, PLAYER, request)
