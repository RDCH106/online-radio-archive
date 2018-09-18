# -*- coding: utf-8 -*-

from os import listdir, path

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
    return onlyfiles


for genre in genres:
    print(get_files(genre))
