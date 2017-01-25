#!python
# coding: utf-8

import re
print 'better to pre-compile the re'
print 'for ^$'
re_blank = re.compile(r'^$')
print re_blank.match('\n'), r'\n'
print re_blank.match('aaa\n'), r'aaa\n'
print re_blank.match('aaa\n\nbbb'), r'aaa\n\nbbb'
print '-'*12
print 'for ^$ with re.DOTALL'
re_blankm = re.compile(r'^$', re.DOTALL)
re_blankm = re.compile(r'^$', re.S)
print re_blankm.match('\n'), r'\n'
print re_blankm.match('aaa\n'), r'aaa\n'
print re_blankm.match('aaa\n\nbbb'), r'aaa\n\nbbb'
print '-'*12
print 'for \A\s*\z'
re_blankb = re.compile(r'^$', re.S)
print re_blankb.match('\n'), r'\n'
print re_blankb.match('aaa\n'), r'aaa\n'
print re_blankb.match('aaa\n\nbbb'), r'aaa\n\t  \nbbb'
