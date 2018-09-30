# -*- coding: utf-8 -*-

from common import logo, genres, repo_base_url
from common import Track, get_files
from metadata import Metadata


print(logo)
meta = Metadata()
print("version " + meta.get_version() + "\n")


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

    file = open("../" + genre + "/" + "ALL_" + genre + ".m3u", "w")
    file.write(m3u_file)
    file.close()
    print("ALL_" + genre + ".m3u" + " saved!")
    m3u_file = ""
