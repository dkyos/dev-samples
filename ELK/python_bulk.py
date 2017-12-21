#!/usr/bin/env python

import sys
import os
import csv
import codecs
import pandas as pd
from elasticsearch import Elasticsearch
from elasticsearch import helpers

es = Elasticsearch(['127.0.0.1'])
if not es.indices.exists("cars"):
    es.indices.create("cars")
    print("create index with cars")
else:
    es.indices.delete("cars")
    es.indices.create("cars")
    print("delete & create index with cars")

mapping = {
        "properties": {
          "body_type": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 512
              }
            }
          },
          "color_slug": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 512
              }
            }
          },
          "date_created": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 512
              }
            }
          },
          "date_last_seen": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 512
              }
            }
          },
          "door_count": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 512
              }
            }
          },
          "engine_displacement": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 512
              }
            }
          },
          "engine_power": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 512
              }
            }
          },
          "fuel_type": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 512
              }
            }
          },
          "host": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 512
              }
            }
          },
          "maker": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 512
              }
            }
          },
          "manufacture_year": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 512
              }
            }
          },
          "message": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 512
              }
            }
          },
          "mileage": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 512
              }
            }
          },
          "model": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 512
              }
            }
          },
          "path": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 512
              }
            }
          },
          "price_eur": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 512
              }
            }
          },
          "seat_count": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 512
              }
            }
          },
          "stk_year": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 512
              }
            }
          },
          "transmission": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 512
              }
            }
          }
        }
}

es.indices.put_mapping(index="cars",doc_type="cars_doc",body=mapping)


load_cols = ['maker', 'model', 'mileage', 'manufacture_year', 
        'engine_displacement', 'engine_power', 'body_type', 'color_slug', 
        'stk_year', 'transmission', 'door_count', 'seat_count', 
        'fuel_type', 'date_created', 'date_last_seen', 'price_eur' ]

csv_file="/home/dkyun77/dkyos/github_dkyos/dev-samples/ELK/data/cars.csv"

def to_int(s):
    try:
        return int(s)
    except ValueError:
        return 0

def get_chunk(data):
    print(" get_chunk - " + str(data.shape))
    data = data.fillna('')
    actions = []
    for index, row in data.iterrows():
        action = {
            '_op_type': 'index',
            "_index": 'cars',
            "_type": 'cars_doc',
            "_id": int(index),
            "_source": {
                "maker":row['maker'],
                "model":row['model'],
                "mileage":row["mileage"],
                "manufacture_year":row["manufacture_year"],
                "engine_displacement":row["engine_displacement"],
                "engine_power":row["engine_power"],
                "body_type":row["body_type"],
                "color_slug":row["color_slug"],
                "stk_year":row["stk_year"],
                "transmission":row["transmission"],
                "door_count":row["door_count"],
                "seat_count":row["seat_count"],
                "fuel_type":row["fuel_type"],
                "date_created":row["date_created"],
                "date_last_seen":row["date_last_seen"],
                "price_eur":row["price_eur"]
            }
        }
        actions.append(action)

    helpers.bulk(es, actions)

    return data

data = pd.DataFrame()
count = 1
chunksize=50000
for chunk in pd.read_csv(csv_file , sep=',' , dtype='object' , usecols = load_cols
            , error_bad_lines=False , quoting=csv.QUOTE_NONE , chunksize=chunksize
            , encoding='utf-8'):
    df = get_chunk(chunk)
    data = data.append(df)
    print("- appended(%d): %s" % (count, str(data.shape)))
    count = count+1
    del(df)
    del(chunk)
    print("- Total: " + str(data.shape) + "\n")

