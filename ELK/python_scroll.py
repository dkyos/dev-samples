#!/usr/bin/env python
#-*- encoding: utf8 -*-

import elasticsearch
import json

es_client = elasticsearch.Elasticsearch("localhost:9200")

docs = es_client.search(index = 'cars',
    doc_type = 'cars_doc',
    body = {
        'query': {
            'match_all': { }
        }
    },
    scroll = '1m', 
    size = 10000) 

scroll_id = docs['_scroll_id']

total_docs = 0 
num_docs = 1
while num_docs > 0:
    docs = es_client.scroll(scroll_id = scroll_id, scroll = '1m')
    num_docs = len(docs['hits']['hits'])
    total_docs += num_docs
    print ("[Total: %d, Iter:%d] retrieved" % (total_docs, num_docs))

