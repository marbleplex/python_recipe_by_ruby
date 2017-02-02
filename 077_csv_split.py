#!python
# coding: utf-8

import re, sys, os
r = re.compile(r'\s+')
p = os.popen2('ls -l')
buf = p[1].read()
ary = []
for l in buf.splitlines():
    ary.append(r.split(l))
print ary
for a in ary:
    print ','.join(a)
