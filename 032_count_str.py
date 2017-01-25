#!python
# coding: utf-8

a = 'aaabbbbbbbbbaaaaaaaaa\n'
print a
print 'count of "aa" is ' 
print a.count('aa')

import re
print 'count with re.findall("a+", a)'
print re.findall('a+', a)
print len(re.findall('a+', a))
print 'count with re.finditer("a+", a) for saving memory'
i = 0
for m in re.finditer('a+', a):
        i += 1
print i
