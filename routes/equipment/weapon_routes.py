from flask import request
from indexes.indexes import WEAPON
from app import app, es
from routes.base_routes import get_all, handle_single_result


@app.route('/equipment/weapon/')
def get_all_weapons():
    return get_all(es, WEAPON)


@app.route('/equipment/weapon/<name>', methods=['POST', 'GET', 'PUT'])
def handle_weapon(name):
    return handle_single_result(es, WEAPON, request)
