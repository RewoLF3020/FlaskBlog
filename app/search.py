from flask import current_app


def add_to_index(index, model):
    if not current_app.elasticsearch:
        return
    
    payload = {}
    for field in model.__searchable__:
        payload[field] = getattr(model, field)
    current_app.elasticsearch.index(index=index, id=model.id, body=payload)


def remove_from_index(index, model):
    if not current_app.elasticsearch:
        return
    current_app.elasticsearch.delete(index=index, id=model.id)


def query_index(index, query, page, per_page):
    if not current_app.elasticsearch:
        return [], 0
    
    search = current_app.elasticsearch.search(
        index=index,
        body={'query': {'multi_match': {'query': query, 'fields': ['*']}},
              'from': (page - 1) * per_page, 'size': per_page})
    """ from: Это параметр, определяющий смещение (начиная с какой позиции) результатов, которые нужно вернуть.
        Вычисляется как (page - 1) * per_page.
        Например, если page равно 1 и per_page равно 10, то from будет равно 0, что означает, что нужно начать с первого результата.
        Если page равно 2, то from будет равно 10, что означает, что нужно начать со 11-го результата.
        size: Это параметр, определяющий количество результатов, которые нужно вернуть на каждой странице.
        В данном случае значение установлено равным per_page, что означает, что будет возвращено per_page результатов.
    """
    ids = [int(hit('_id')) for hit in search['hits']['hits']]
    return ids, search['hits']['total']