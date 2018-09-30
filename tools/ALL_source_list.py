# -*- coding: utf-8 -*-

from os import path
from common import logo, genres
from common import parse_m3u, get_files
from metadata import Metadata


print(logo)
meta = Metadata()
print("version " + meta.get_version() + "\n")


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
