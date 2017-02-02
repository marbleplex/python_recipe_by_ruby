#!python
# coding: utf-8

import re
s = u'I love Ruby!'
print "s.replace(u'Ruby', u'Python')"
print s + ' -> ' + s.replace(u'Ruby', u'Python')

print "re.sub(u'あい', u'愛', u'あいあいあい')"
print re.sub(u'あい', u'愛', u'あいあいあい')
print "re.sub(u'あい', u'愛', u'あいあいあい', count=1)"
print re.sub(u'あい', u'愛', u'あいあいあい', count=1)

print "re.sub('(.)([A-Z])', ur'\1 \2', u'FrontPage')"
print u'FrontPage' + ' -> ' + re.sub('(.)([A-Z])', ur'\1 \2', u'FrontPage')

def dashrepl(matchobj):
    if matchobj.group(0) == u'-':
        return u' '
    else:
        return u'-'

print re.sub(u'-{1,2}', dashrepl, u'pro----gram-files')

