# -*- coding: utf-8 -*-

from os import listdir, path
import re
from common import logo, genres
from common import Track, parse_m3u

print(logo)


def get_files(genre):
    pwd = path.join(path.dirname(path.abspath(__file__)), "../")
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
    sources = parse_m3u(path.join(pwd, "../", genre, file))
    return sources


for genre in genres:
    files = get_files(genre)
    for file in files:
        playlist = get_m3u_sources(genre, file)
        for track in playlist:
            print(track.title + "  " + track.length + "  " + track.path)
