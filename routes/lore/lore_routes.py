from flask import request
from indexes.indexes import ORGANIZATION
from app import app, es
from routes.base_routes import get_all, handle_single_result


@app.route('/lore/organizations/')
def get_all_organization():
    return get_all(es, ORGANIZATION)


@app.route('/lore/organizations/<name>', methods=['POST', 'GET', 'PUT'])
def handle_organization(name):
    return handle_single_result(es, ORGANIZATION, request)
