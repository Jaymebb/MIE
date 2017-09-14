def generate_response(code, task, doc_id, entities):
    """generate api response"""
    body = {
        'status': code,
        'task': task,
        'document id': doc_id,
        'response': entities
    }
    return body
