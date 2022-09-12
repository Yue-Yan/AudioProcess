# Author: feiyue
# Date: 2022-09-10
# https://blog.csdn.net/diyiday/article/details/82153780

from operator import index
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import json

# connect host
def es_connect():
    es_connecter = Elasticsearch(
        host=['192.168.1.1:9200', '192.168.1.2:9200']) # maybe you need user name and password
    return es_connecter

# config mapping
def config_mapping():
    mappings = {
        "properties":{  
            'phone_number':{
                'type': 'text' # old verison should be 'string'
            },
            'text':{
                'type': 'text'
            },
            's3_path':{
                'type':'text'
            }
        }

    }
    return mappings

def load_matched_result_json(matched_result_json):
    with open(matched_result_json) as f:
        text = f.read() # it should be a string
        text_str2list = json.loads(text)
    return text_str2list


if __name__ == '__main__':
    index = 'XXXX-v1'
    es_connecter = es_connect()
    # CREATE INDEX
    # UPLOAD DATA
    try:
        es_connecter.indiecs.create(index=index, body=config_mapping())
        bulk(load_matched_result_json(), index=index)
    except Exception as e:
        print(f'Other Error: {e}')

    # COUNT
    q = {}
    res = es_connecter.count(index=index, body=q)
    print(f'Count: {res}')
    # SEARCH ONE ITEM
    q = {
        "query":{
            "term":{
                "phone_number":"111"
            }
        }
    }
    res = es_connecter.get(index=index, body=q)
    print(res)
    # SEARCH ITEM
    q = {
        "query":{
            "match_all": {}
        }
    }
    res = es_connecter.search(index=index, body=q)
    print(res)

    # DELETE ONE ITEM
    es_connecter.delete(index=index, id='xxxxx')
    # DELETE INDEX
    es_connecter.delete(index=index)
