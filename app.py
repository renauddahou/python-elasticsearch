from flask import Flask
from elasticsearch7 import Elasticsearch
from flask_cors import CORS

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

app = Flask(__name__)
CORS(app)

# Do not remove route imports
from routes import talent_routes

if __name__ == '__main__':
    app.run()
