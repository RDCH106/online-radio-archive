# -*- coding: utf-8 -*-

from os import listdir
from os.path import isfile, join

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

generes = ["Electronic", "JPop", "Soundtrack"]
repo_base_url = "https://raw.githubusercontent.com/RDCH106/online-radio-archive/master"

def get_files(genere):
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]


for genere in generes:
    pass
