# Author: feiyue
# Date: 2022-09-11

import pandas as pd
import json

def matched_person(matched_result_json):
    """
    Usually one person reads several sentenses, 
    we just want to figure out the unique count of speaker.
    """
    with open(matched_result_json, 'r') as f:
        text = f.read()
        text_str2list = json.loads(text)
    
    df = pd.DataFrame(text_str2list)
    matched_person = df['taker'].nunique()
    print(f'{matched_person} out of {len(df)}')


if __name__ == '__main__':
    matched_result_json = "aaa"
    matched_person(matched_result_json)
