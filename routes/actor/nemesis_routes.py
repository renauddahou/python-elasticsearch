from flask import request
from indexes.indexes import NEMESIS
from app import app, es
from routes.base_routes import get_all, handle_single_result


@app.route('/actors/nemesis/')
def get_all_nemesis():
    return get_all(es, NEMESIS)


@app.route('/actors/nemesis/<name>', methods=['POST', 'GET', 'PUT'])
def handle_nemesis(name):
    return handle_single_result(es, NEMESIS, request)
