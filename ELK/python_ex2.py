#!/usr/bin/env python
#-*- encoding: utf8 -*-

import elasticsearch
import json

es_client = elasticsearch.Elasticsearch("localhost:9200")

docs = es_client.search(index = 'deraw',
    doc_type = 'deraw_doc',
    body = {
        'query': {
            'match_all': { }
        }
    },
    scroll = '1m',   # scroll 정보를 1분 유지
    size = 1000) 

scroll_id = docs['_scroll_id']

num_docs = len(docs['hits']['hits'])
print ("{0} docs retrieved".format(num_docs))

'''
while num_docs > 0:
    docs = es_client.scroll(scroll_id = scroll_id, scroll = '1m')

    num_docs = len(docs['hits']['hits'])
    print ("{0} docs retrieved".format(num_docs))
'''



