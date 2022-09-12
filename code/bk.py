# Author: feiyue
# Date: 2022-09-11

import os 
import json
import pandas as pd

def load_matched_json(matched_result_json):
    with open(matched_result_json, 'r') as f:
        text = f.read()
        text_str2list = json.loads(text)
    
    df = pd.DataFrame(text_str2list)
    return df
    
def version_compare(old_version_matched_json, new_version_matched_json):
    pass

def merge_to_compare():
    pass


if __name__ == '__main__':
    old_matched_A_json = ""
    new_matched_A_json = ""
    old_matched_B_json = ""
    new_matched_B_json = ""

    