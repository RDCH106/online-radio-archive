# -*- coding: utf-8 -*-

from os import listdir, path
import re
from common import logo, genres
from common import Track, parse_m3u, get_files

print(logo)


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
