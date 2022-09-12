# Author: feiyue
# Date: 2022-09-11

import json
import pandas as pd
from elasticSearch import *

# functions for one language compare
def load_matched_json(matched_result_json):
    with open(matched_result_json, 'r') as f:
        text = f.read()
        text_str2list = json.loads(text)
    
    df = pd.DataFrame(text_str2list)
    return df
    
def version_compare_each_language(old_version_matched_json, new_version_matched_json):
    old_version_set = set(load_matched_json(old_version_matched_json).to_list())
    new_version_set = set(load_matched_json(new_version_matched_json).to_list())
    only_in_old_version = old_version_set - new_version_set
    only_in_new_version = new_version_set - old_version_set
    both_in_two_versions = old_version_set & new_version_set
    print('--------Description--------')
    print(f'Count of old version: {len(old_version_set)}')
    print(f'Count of new version: {len(new_version_set)}')
    print(f'Only in old version: {only_in_old_version}')
    print(f'Only in new version: {only_in_new_version}')
    print(f'Both in two versions: {both_in_two_versions}')
    return None

# functions for indexes compare
def query_es(maxsize=10000):
    query_body = {
        "_source": ['phone_number', 's3_path'],
        "query": {
            "match_all": {}
        },
        "size": maxsize
    }
    return query_body

def search_es(index=None):
    try:
        es_connecter = es_connect()
        res = es_connecter.search(index=index, body=query_es())
        return res
    except Exception as e:
        print(f'Other Issue: {e}')
        return None
    return None

def analyse_es(es_res):
    s3_path_list = list()
    es_res = search_es()
    src = es_res['hits']['hits']
    for item in src:
        s3_path = item['_source']['s3_path'] # 's3_path' is unique, so we use this as key word
        s3_path_list.append(s3_path)
    s3_path_set = set(s3_path_list)
    print(f'{len(s3_path_set)} in this index')
    return s3_path_set

def compare_two_es(old_es_res=None, new_es_res=None):
    old_es_res = analyse_es()
    new_es_res = analyse_es()
    only_in_old_version = old_es_res - new_es_res
    only_in_new_version = new_es_res - old_es_res
    both_in_two_versions = old_es_res & new_es_res
    print('--------Description--------')
    print(f'Count of old version: {len(old_es_res)}')
    print(f'Count of new version: {len(new_es_res)}')
    print(f'Only in old version: {only_in_old_version}')
    print(f'Only in new version: {only_in_new_version}')
    print(f'Both in two versions: {both_in_two_versions}')
    return None


if __name__ == '__main__':
    old_index = 'xxxx-v1'
    new_index = 'xxxx-v2'
    # compare one language
    old_matched_A_json = "AAA/AA/A_v1.json"
    new_matched_A_json = "AAA/AA/A_v2.json"
    # old_matched_B_json = "BBB/BB/B_v1.json"
    # new_matched_B_json = "BBB/BB/B_v2.json"
    version_compare_each_language(old_matched_A_json, new_matched_A_json)
    # version_compare_each_language(old_matched_B_json, new_matched_B_json)

    # compare two es indexes
    old_es_res = search_es(old_index)
    new_es_res = search_es(new_index)
    old_s3_path_set = analyse_es(old_es_res)
    new_s3_path_set = analyse_es(new_es_res)
    compare_two_es(old_s3_path_set, new_s3_path_set)



    