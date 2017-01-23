#!python
# coding: utf-8

import re
members = 'yamada hirobumi\nkoyamada kiyotako\nsuzuki sanetomi\nyamada aritomo'

print 'members are:' + members
print 're.findall("yamada.*", members)'
print re.findall('yamada.*', members)
print 're.findall(\'^yamada.*\', members)'
print re.findall('^yamada.*', members)
print 're.findall(\'^yamada.*\', members, re.M)'
print re.findall('^yamada.*', members, re.M)
print 're.findall(\'.*$\', members, re.M)'
print re.findall('.*o$', members, re.M)

