from flask import request
from indexes.indexes import GEAR
from app import app, es
from routes.base_routes import get_all, handle_single_result


@app.route('/equipment/gear/')
def get_all_gear():
    return get_all(es, GEAR)


@app.route('/equipment/gear/<name>', methods=['POST', 'GET', 'PUT'])
def handle_gear(name):
    return handle_single_result(es, GEAR, request)