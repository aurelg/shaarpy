#!/usr/bin/env python

from shaarpy.shaarpy import Shaarpy

# Account description
login = "tagada"
password = "tagada"
shaarli_url = "https://my.framasoft.org/u/%s/" % login

# Post link
url = 'http://example.org'
tags = ['tag1', 'tag2', 'tag3']
desc = 'description'

s = Shaarpy()
s.login(login, password, shaarli_url)
s.post_link(url, tags, desc)
