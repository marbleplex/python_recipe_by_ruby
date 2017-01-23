#!python
# coding: utf-8

print 'sjist = open("021_sjis.txt", "r").read()'
b = open('021_sjis.txt', 'r').read()
print 'b[:16]'
print b[:16]
print "s = b.decode('shift-jis')"
print "s[:16:]"
s = b.decode('shift-jis')
print s[:16]

import re

print "re.search(u'各部屋', s)"
print re.search(u'各部屋', s)
print "matched = re.findall(u'各部屋.+', s)"
print "matched[0].encode('utf-8')"
matched = re.findall(u'各部屋.+', s)
print matched[0].encode('utf-8')
