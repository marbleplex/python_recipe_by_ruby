#!python
# coding: utf-8

import re, sys, os
dir = os.path.abspath('.')
filelist = os.listdir(dir)
for f in filelist:
    try:
        print f, os.stat(f)
        m = re.search('\d+', f)
        print f, ' matched : ' , m.group(0)
    except AttributeError:
        continue
#    try:
#        m = re.findall('\S+', f)
#        print f
#    except AttributeError:
#        continue


