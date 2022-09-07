from flask import Flask, request
from elasticsearch7 import Elasticsearch
from flask_cors import CORS
from indexes.indexes import TALENTS

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

app = Flask(__name__)
CORS(app)


@app.route('/talents/')
def get_all_talents():
    results = es.search(
        index=TALENTS,
        size=1000,
    )['hits']['hits']
    slim_results = []
    for result in results:
        slim_results.append(result['_source'])
    return slim_results


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
            body={'doc': request.json}
        )
    else:
        return es.get(
            index=TALENTS,
            id=name
        )['_source']


if __name__ == '__main__':
    app.run()
