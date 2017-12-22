#!/usr/bin/env python
#-*- encoding: utf8 -*-

import pandas as pd
import elasticsearch
import json
from pandas import Series, DataFrame
from pandas.io.json import json_normalize

total_docs = 0 
num_docs = 0

es = elasticsearch.Elasticsearch("localhost:9200")

#Process hits here
def process_hits(hits):
    global total_docs
    global num_docs

    num_docs = len(hits)
    total_docs += num_docs
    print ("[Total: %d, Num:%d] retrieved" % (total_docs, num_docs))

    df = json_normalize(hits)
    print (df.shape)
    print (df.columns)

    '''
    for item in hits:
        df = pd.DataFrame(item['_source'], index=[0])
        print (df.shape)
        print (df.columns)
    '''


docs = es.search(index = 'cars',
    doc_type = 'cars_doc',
    body = {
        'query': {
            'match_all': { }
        }
    },
    scroll = '1m', 
    size = 1000) 
# Process current batch of hits
process_hits(docs['hits']['hits'])

scroll_id = docs['_scroll_id']
while num_docs > 0:
    docs = es.scroll(scroll_id = scroll_id, scroll = '1m')
    num_docs = len(docs['hits']['hits'])
    if num_docs > 0:
        # Process current batch of hits
        process_hits(docs['hits']['hits'])

