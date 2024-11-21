#!/usr/bin/env python3
# rearch archiving with pandoc
import re
import requests
import bs4
import subprocess
import sys
import os

from pathlib import Path

# fail if no url
if len(sys.argv) < 2:
    print("no url")
    sys.exit()

# path setup
archive_path = Path.home() / "ark"

if archive_path.is_dir():
    pass
else:
    archive_path.mkdir()
    print("archive path created")

print("Getting page info...")

# get url
url = sys.argv[1]
res = requests.get(url)

# get title
soup = bs4.BeautifulSoup(res.text, "html.parser")
page_title = soup.title.string

# print("page title: " + page_title)

# format title (name.of.article.txt)
word_title = re.sub("\\W", "_", page_title)
short_title = word_title[:36]
dedup_title = re.sub("_{2,}", "_", short_title)
clip_title = dedup_title.rstrip("_")
actual_title = clip_title.lower() + ".txt"

# print("formatted title: " + actual_title)

# build destination path
title_path = Path(actual_title)
destination = archive_path / title_path

# pandoc command
print("Running Pandoc...")
subprocess.run(["pandoc", "-f", "html", "-t", "plain", url, "-o", destination])

# append to archive list
catalog_path = archive_path / "ark.catalog"

with open(catalog_path, "a") as file:
    file.write(url + "\n")
