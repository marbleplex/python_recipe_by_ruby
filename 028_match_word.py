#!python
# coding: utf-8

import re

print "m = re.search(r'\bspec\b\", \'abc spec def\')"
print 'print m.group(0)'
m = re.search(r'\bspec\b', 'abc spec def')
print m.group(0)

print 'm = re.search(r''\bspec\b'', ''abc specification def'')'
print 'm'
m = re.search(r'\bspec\b', 'abc specification def')
print m
