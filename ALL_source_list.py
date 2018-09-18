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


def parse_m3u(infile):
    try:
        assert (type(infile) == '_io.TextIOWrapper')
    except AssertionError:
        infile = open(infile, 'r')

    """
        All M3U files start with #EXTM3U.
        If the first line doesn't start with this, we're either
        not working with an M3U or the file we got is corrupted.
    """

    line = infile.readline()
    if not line.startswith('#EXTM3U'):
        return

    # initialize playlist variables before reading file
    playlist = []
    song = Track(None, None, None)

    for line in infile:
        line = line.strip()
        if line.startswith('#EXTINF:'):
            # pull length and title from #EXTINF line
            length, title = line.split('#EXTINF:')[1].split(',', 1)
            song = Track(length, title, None)
        elif (len(line) != 0):
            # pull song path from all other, non-blank lines
            song.path = line
            playlist.append(song)
            # reset the song variable so it doesn't use the same EXTINF more than once
            song = Track(None, None, None)

    infile.close()
    return playlist


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


def get_m3u_sources(genre, file):
    pwd = path.dirname(path.abspath(__file__))
    sources = parse_m3u(path.join(pwd, genre, file))
    return sources


for genre in genres:
    files = get_files(genre)
    for file in files:
        playlist = get_m3u_sources(genre, file)
        for track in playlist:
            print(track.title + "  " + track.length + "  " + track.path)
