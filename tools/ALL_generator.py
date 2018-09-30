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

"""
    song info lines are formatted like:
    EXTINF:419,Alice In Chains - Rotten Apple
    length (seconds)
    Song title
    file name - relative or absolute path of file
    ..\Minus The Bear - Planet of Ice\Minus The Bear_Planet of Ice_01_Burying Luck.mp3
"""


class Track(object):
    def __init__(self, length, title, path):
        self.length = length
        self.title = title
        self.path = path


def get_files(genre):
    pwd = path.dirname(path.abspath(__file__))
    onlyfiles = [f for f in listdir(path.join(pwd, genre)) if path.isfile(path.join(pwd, genre, f))]
    all_regex = re.compile("ALL_[A-Za-z]+\.m3u")
    filtered_files = [file for file in onlyfiles if not all_regex.match(file)] #List comprehension
    # Equivalent of filtered_files = [file for file in onlyfiles if not all_regex.match(file)]
    # filtered_files = []
    # for file in onlyfiles:
    #     if not all_regex.match(file):
    #         filtered_files.append(file)

    return filtered_files


def add_source(m3u_file, track):
    prettified_title = track.title.replace("-", " ")
    prettified_title = prettified_title.replace(".m3u", "")
    source = "#EXTINF:" + str(track.length) + "," + prettified_title + "\n"
    source = source + track.path + "\n"
    m3u_file += source

    return m3u_file


for genre in genres:
    files = get_files(genre)
    m3u_file = "#EXTM3U\n"
    for file in files:
        track = Track(-1, file, (repo_base_url + "/" + genre + "/" + file))
        m3u_file = add_source(m3u_file, track)

    file = open(genre + "/" + "ALL_" + genre + ".m3u", "w")
    file.write(m3u_file)
    file.close()
    print("ALL_" + genre + ".m3u" + " saved!")
    m3u_file = ""
