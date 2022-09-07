from flask import request
from indexes.indexes import SKILLS
from app import app, es
from routes.base_routes import get_all, handle_single_result


@app.route('/skills/')
def get_all_skills():
    return get_all(es, SKILLS)


@app.route('/skills/<name>', methods=['POST', 'GET', 'PUT'])
def handle_skill(name):
    return handle_single_result(es, SKILLS, request)
