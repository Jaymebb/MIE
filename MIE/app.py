from __init__ import *

matcher = None

@app.route('/medir/api/v0.1/quickumls/<string:doc_id>', methods=['GET'])
def quick_umls(doc_id):
    #initialize QUICKUMLS
    print "initializing.."
    global matcher
    if matcher == None:
        matcher = QuickUMLS(os.environ.get("DEST_PATH"))
    print "extracting text"
    text = q.query_by_id(doc_id)
    print "processing"
    res = sum(matcher.match(text, best_match = True, ignore_syntax=False),[])
    res_new = []
    for ins in res:
        res_new.append({k:v for k, v in ins.items() if k != "semtypes"})
    res = resp.generate_response(200, 'QUICK-UMLS ENTITY EXTRACTION', doc_id, res_new)
    return jsonify(res)

@app.route('/medir/api/v0.1/metamap/<string:doc_id>', methods=['GET'])
def meta_map(doc_id):
    #start metamap
    mm = MetaMap.get_instance(os.environ.get("INSTANCE_PATH"))
    text = q.query_by_id(doc_id)
    print "processing"
    sents = []
    sents.append(text)
    concepts, error = mm.extract_concepts(sents,[1])
    res = resp.generate_response(200, 'META MAP EXTRACTION', doc_id, concepts)
    return jsonify(res)

@app.route('/medir/api/v0.1/ctakes/<string:doc_id>', methods=['GET'])
def ctakes(doc_id):
    c = cTakes()
    text = q.query_by_id(doc_id)
    print "processing"
    result = c.pipeline(text)
    res = resp.generate_response(200, 'cTAKES EXTRACTION', doc_id, result)
    return jsonify(res)



if __name__ == '__main__':
    app.run(debug=True)
