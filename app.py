from flask import Flask
from elasticsearch7 import Elasticsearch
from flask_cors import CORS

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

app = Flask(__name__)
CORS(app)

# Do not remove route imports
from routes import talent_routes, skill_routes
from routes.actor import nemesis_routes, player_routes
from routes.lore import lore_routes
from routes.equipment import weapon_routes, gear_routes, armor_routes

if __name__ == '__main__':
    app.run()
