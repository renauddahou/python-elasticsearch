from flask import Flask, request
from elasticsearch7 import Elasticsearch
from flask_cors import CORS
from indexes.indexes import TALENTS

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

app = Flask(__name__)
CORS(app)


@app.route('/talents/')
def get_all_talents():
    return es.search(
        index=TALENTS
    )


@app.route('/talents/<name>', methods=['POST', 'GET', 'PUT'])
def handle_talents(name):
    name = request.view_args['name']
    if request.method == 'POST':
        return es.index(
            index=TALENTS,
            id=name,
            document={'name': name}
        )
    elif request.method == 'PUT':
        return es.update(
            index=TALENTS,
            id=name,
            body=request.json
        )
    else:
        return es.get(
            index=TALENTS,
            id=name
        )


if __name__ == '__main__':
    app.run()
