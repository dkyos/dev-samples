#!/usr/bin/env python



from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()

res = es.search(index="deraw", body={"query": {"match_all": {}}})
print("Got %d Hits:" % res['hits']['total'])

