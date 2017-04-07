#!/usr/bin/env python

from shaarpy import Shaarpy

# Account description
login = "tagada"
password = "tagada"
shaarli_url = "https://my.framasoft.org/u/%s/" % login

# Post link
url = 'http://example.org'
tags = ['tag1', 'tag2', 'tag3']
desc = 'weouhwge owuehgowhug wehugowuehg'

s = Shaarpy()
s.login(login, password, shaarli_url)
s.post_link(url, tags, desc)

# def dump(soup):
#     with open('t.html', 'w') as f:
#         f.write(str(soup))
