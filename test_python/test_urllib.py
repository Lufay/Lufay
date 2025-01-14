#! /usr/bin/env python

import urllib.parse as urlparser

up = urlparser.urlsplit('http://a.b.c?a=1&a=2&b=3&c=4&d=5')
q= urlparser.parse_qsl(up.query)
print(up, q)

j = urlparser.unwrap('http://www.cwi.nl/%7Eguido/Python.html?a=3&b=5&d=6#mmm')
print(j)