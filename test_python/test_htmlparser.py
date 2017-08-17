#!/usr/bin/env python

html_doc = '''\
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
'''

from HTMLParser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Encountered a start tag:", tag
        print self.getpos()
        print self.get_starttag_text()

    def handle_endtag(self, tag):
        print "Encountered an end tag :", tag
        print self.getpos()
        print self.get_starttag_text()

    def handle_data(self, data):
        print "Encountered some data  :", data
        print self.getpos()
        print self.get_starttag_text()

p = MyHTMLParser()
p.feed(u'''<html>
    <head>
    </head>
    <body>
    <h1 style="display:none">tttttt</h1
''')

print p.getpos()
print p.get_starttag_text()
p.close()


