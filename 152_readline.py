#!python
# coding: utf-8

import re, sys, os
f = open('021_utf8out.txt', 'r')
for line in f:
    print line
f.close
f = open('021_utf8out.txt', 'r')
print f.readlines()
f.close
