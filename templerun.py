#!/usr/bin/env python

""" run file through jones (must be in path)"""

import sys
import subprocess

if len(sys.argv) < 2:
    print("no file")
    sys.exit()

with open(sys.argv[1], encoding="uft-8") as url_file:
    for line in url_file:
        print(line.strip())
        subprocess.run(["jones", line.strip()], check=False)
