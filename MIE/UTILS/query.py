from __init__ import *

def query_by_id(doc_id):
    """Query pdf document by paper pmid
    """
    with Con(db = os.environ.get("MONGO_DB"), host = os.environ.get("MONGO_URL"), port = int(os.environ.get("MONGO_PORT")), col = os.environ.get("MONGO_COL")) as col:
        doc = col.find_one({'pmid': doc_id})
        doc_text = [v for k,v in doc['abstract'].iteritems()]
        doc_text = ' '.join(doc_text) + doc['title']
    return doc_text
