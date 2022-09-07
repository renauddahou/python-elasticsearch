from flask import request
from indexes.indexes import TALENTS
from app import app, es
from routes.base_routes import get_all, handle_single_result


@app.route('/talents/')
def get_all_talents():
    return get_all(es, TALENTS)


@app.route('/talents/<name>', methods=['POST', 'GET', 'PUT'])
def handle_talent(name):
    return handle_single_result(es, TALENTS, request)
