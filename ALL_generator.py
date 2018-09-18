# -*- coding: utf-8 -*-

from os import listdir, path
import re

logo ="""
                       !
                       |
                       |    |~/
                       |   _|~
         .============.|  (_|   |~/
       .-;____________;|.      _|~
       | [_________I__] |     (_|
       |  \"\"\"ºº\"\" (_) (_) |
       | .=====..=====. |
       | |:::::||:::::| |
       | '=====''=====' |
       '----------------'

                   _ _       
                  | (_)      
     _ __ __ _  __| |_  ___  
    | '__/ _` |/ _` | |/ _ \ 
    | | | (_| | (_| | | (_) |
    |_|  \__,_|\__,_|_|\___/ 
       
    """
        
print(logo)

genres = ["Electronic", "JPop", "Soundtrack"]
repo_base_url = "https://raw.githubusercontent.com/RDCH106/online-radio-archive/master"


def get_files(genre):
    pwd = path.dirname(path.abspath(__file__))
    onlyfiles = [f for f in listdir(path.join(pwd, genre)) if path.isfile(path.join(pwd, genre, f))]
    all_regex = re.compile("ALL_[A-Za-z]+\.m3u")
    filtered_files = [file for file in onlyfiles if not all_regex.match(file)]
    return filtered_files


for genre in genres:
    print(get_files(genre))
