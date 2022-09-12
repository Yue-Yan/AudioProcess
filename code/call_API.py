# Author: feiyue
# Date: 2022-09-11

import os 
import json
from multiprocessing import Pool

class CallService(object):
    def __init__(self):
        self.a = a 

    def service(self):
        pass


if __name__ == '__main__':
    pool = Pool(os.cpu_count/2)
    wav_list = []
    pool.map(service, wav_list)