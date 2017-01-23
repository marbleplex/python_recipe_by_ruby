#!python
# coding: utf-8

print 'sjist = open("021_sjis.txt", "r").read()'
b = open('021_sjis.txt', 'r').read()
print "s = b.decode('shift-jis')"
s = b.decode('shift-jis')

import re

print "re.search(u'各部屋', s)"
print re.search(u'各部屋', s)
print "matched = re.findall(u'各部屋.+', s)"
print "matched[0].encode('utf-8')"
matched = re.findall(u'各部屋.+', s)
print matched[0].encode('utf-8')

print "for matching for multilines use re.S or re.DOTALL"
print "matched = re.findall(u'各部屋.+', s, re.DOTALL)"
print "matched[0].encode('utf-8')"
matched = re.findall(u'元.+', s, re.DOTALL)
print matched[0].encode('utf-8')

print "create re obj for split, sub, sbn"
m =  re.compile(u'各部屋.+フロア', re.DOTALL).split(s)
print m[0].encode('utf-8')
