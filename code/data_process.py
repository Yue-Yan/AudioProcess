# Author: feiyue
# Date: 2022-09-10

import os
import pandas as pd
import subprocess
import wave

def DataProcess(object):
    """
    languages_folder_path
        language_A
            mp3_folder
            A.json
        language_B
            mp3_folder
            B.json
        ...
    """
    def __init__(self, languages_folder):
        self.languages_folder = languages_folder

    # get languages_folder_path info
    # ['A', 'B', 'C', ...]
    def get_languages_folder_info(self):
        language_list = [item for item in os.listdir(self.languages_folder)]
        languages_list = [item.split('_')[2] for item in language_list if not item.startswith('.')] 
        print(f'{len(languages_list)} here: {languages_list}')
        
    def get_each_language_folder_info(self):
        pass

    def get_each_language_folder_mp3(self):
        languages_path_list = [os.path.join(self.languages_folder, item) for item in os.listdir(self.languages_folder) \
            if os.path.isdir(item)]
        

    def convert_mp3_to_wav(self):
        pass

    
if __name__ == '__main__':
    languages_folder = r""
    dp = DataProcess(languages_folder)
    dp.get_languages_folder_info()
    dp.get_each_language_folder_info()