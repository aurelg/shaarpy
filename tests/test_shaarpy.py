#!/usr/bin/env python

from shaarpy.shaarpy import Shaarpy
import sys

# Account description
login = "tagada"
shaarli_url = "https://my.framasoft.org/u/%s/" % login
try:
    password = sys.argv[1]
except:
    print('Enter password for %s on %s' % (login, shaarli_url))
    sys.exit(1)

# Post link
url = 'http://example.org'
tags = ['tag1', 'tag2', 'tag3']
desc = 'description'

s = Shaarpy()
s.login(login, password, shaarli_url)
s.post_link(url, tags)
