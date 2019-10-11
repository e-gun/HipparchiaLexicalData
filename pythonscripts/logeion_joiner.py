# -*- coding: utf-8 -*-
"""
        HipparchiaServer: an interface to a database of Greek and Latin texts
        Copyright: E Gunderson 2016-19
        License: GNU GENERAL PUBLIC LICENSE 3
                (see LICENSE in the top level directory of the distribution)
"""

import os
import glob
import subprocess
import re
from collections import deque

# needs to be run in the same directory at the logeion greatscott files

dir_path = os.path.dirname(os.path.realpath(__file__))
files = sorted(glob.glob(dir_path+'/*.xml'))
writeto = 'logeion.lsj.xml'
allentries = deque()
divopen = re.compile(r'<div2')
divclose = re.compile(r'</div2>')

for f in files:
	onefile = open(f, encoding='utf-8', mode='r')
	lines = onefile.readlines()
	onefile.close()
	entries = [l for l in lines if l[0:5] == '<div2' and re.search(divclose, l)]
	allentries.extend(entries)

# try:
# 	os.remove(writeto)
# except FileNotFoundError:
# 	pass

with open(writeto, 'w') as outfile:
	outfile.write(''.join(allentries))

subprocess.run(['gzip', '{f}'.format(f=writeto)])
