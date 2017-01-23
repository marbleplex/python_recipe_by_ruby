#!python
# coding: utf-8

a = 'abcabc'
text = 'りんご'

print 'length of' + a + 'is'
print len(a)

utext =  unicode(text, 'utf-8')
print 'length of text: ' + text + ' is'
print len(text)
print 'length of utext: ' + utext + ' is'
print len(utext)
stext =  unicode(text, 'utf-8').encode('shift-jis')
print 'length of stext: ' + stext  + ' is'
print len(stext)

