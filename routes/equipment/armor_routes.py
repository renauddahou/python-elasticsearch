from flask import request
from indexes.indexes import ARMOR
from app import app, es
from routes.base_routes import get_all, handle_single_result


@app.route('/equipment/armor/')
def get_all_armor():
    return get_all(es, ARMOR)


@app.route('/equipment/armor/<name>', methods=['POST', 'GET', 'PUT'])
def handle_armor(name):
    return handle_single_result(es, ARMOR, request)
