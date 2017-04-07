#!/usr/bin/env python
import re
import requests
from bs4 import BeautifulSoup

login = "tagada"
password = "tagada"
# login = "syllabes"
# password = "P7#^yZDN/NTvEH(<=kFF]0|6|ETWL6"
shaarli_url = "https://my.framasoft.org/u/%s/" % login


def get_param_value_from_html(html, param_name):
    soup = BeautifulSoup(html, 'html.parser')
    return get_param_value(soup, param_name)

def get_param_value(soup, param_name):
    try:
        tag = soup.find('input', attrs={'name': param_name})
    except Exception as e:
        print("Can't find %s : %s " % (param_name, str(e)))
    if tag is None:
        print("Can't find %s" % param_name)
        return ''
    return tag['value']


# Get token from login page
s = requests.Session()
r = s.get("%s?do=login" % shaarli_url)
token = get_param_value_from_html(r.content, 'token')

# Login
data = {"login": login,
        "password": password,
        "longlastingsession": "on",
        "token": token,
        "do": "login"}
r = s.post(shaarli_url, data)
token = get_param_value_from_html(r.content, 'token')

# Post link

url = 'http://example.org'
tags = ['tag1', 'tag2', 'tag3']
desc = 'weouhwge owuehgowhug wehugowuehg'

## Submit URL to retrieve save form and already filled fields
r = s.get('%s?post=%s' % (shaarli_url, url))
soup = BeautifulSoup(r.content, 'html.parser')
token = get_param_value(soup, 'token')
lf_linkdate = get_param_value(soup, 'lf_linkdate')
lf_title = get_param_value(soup, 'lf_title')
lf_description = soup.find('textarea', attrs={'name': 'lf_description'}).content
lf_tags = soup.find('input', attrs={'name': 'lf_tags'})['value']
# TODO lf_private is ignored for now

## Merge
## tags w/ existing lf_tags
## desc w/ existing lf_description + timestamp ?

## Submit save form
r = s.post('%s?post=%s' % (shaarli_url, url), {
    'lf_linkdate': lf_linkdate,
    'lf_url': url,
    'lf_title': lf_title,
    'lf_description': desc,
    'lf_tags': ' '.join(tags),
    'save_edit': 'Enregistrer',
    'token': token
    })
html = r.content

def dump(soup):
    with open('t.html', 'w') as f:
        f.write(str(soup))
