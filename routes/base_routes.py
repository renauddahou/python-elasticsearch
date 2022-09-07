
def get_all(es, index):
    slim_results = []
    for result in es.search(index=index, size=1000)['hits']['hits']:
        slim_results.append(result['_source'])
    return slim_results


def handle_single_result(es, index, request):
    name = request.view_args['name']
    if request.method == 'POST':
        return es.index(
            index=index,
            id=name,
            document={'name': name}
        )
    elif request.method == 'PUT':
        return es.update(
            index=index,
            id=name,
            body={'doc': request.json}
        )
    else:
        return es.get(
            index=index,
            id=name
        )['_source']
