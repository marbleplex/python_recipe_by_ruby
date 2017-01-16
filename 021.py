#!python
# coding: utf-8

text = u'りんご'
text.encode('utf-8')
text.encode('shift-jis')
# ※PythonではUTF-8とUnicodeは別物です
text = 'りんご'
print unicode(text, 'utf-8')

sjis_file = open('021_sjis.txt')
utf8_file = open('021_utf8out.txt', 'w')
for line in sjis_file:
    print unicode(line, 'shift-jis').encode('utf-8')
    utf8_file.write(unicode(line, 'shift-jis').encode('utf-8'))

utf8_file.close()
sjis_file.close()
