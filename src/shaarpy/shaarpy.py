#!/usr/bin/env python
from datetime import datetime
import requests
from bs4 import BeautifulSoup


class Shaarpy:

    _TOKEN = None
    _URL = None

    def _get_param_value_from_html(self, html, param_name):
        soup = BeautifulSoup(html, 'html.parser')
        return self._get_param_value(soup, param_name)

    def _get_param_value(self, soup, param_name):
        try:
            tag = soup.find('input', attrs={'name': param_name})
        except Exception as e:
            print("Can't find %s : %s " % (param_name, str(e)))
        if tag is None:
            print("Can't find %s" % param_name)
            return ''
        return tag['value']

    def login(self, login, password, url):
        self._URL = url

        # Get token from login page
        self._SESSION = requests.Session()
        r = self._SESSION.get("%s?do=login" % self._URL)
        self._TOKEN = self._get_param_value_from_html(r.content, 'token')

        # Login
        data = {"login": login,
                "password": password,
                "longlastingsession": "on",
                "token": self._TOKEN,
                "do": "login"}
        r = self._SESSION.post(self._URL, data)
        self._TOKEN = self._get_param_value_from_html(r.content, 'token')

    def post_link(self, url, tags, desc):

        # Submit URL to retrieve save form and already filled fields
        r = self._SESSION.get('%s?post=%s' % (self._URL, url))
        soup = BeautifulSoup(r.content, 'html.parser')
        self._TOKEN = self._get_param_value(soup, 'token')
        lf_linkdate = self._get_param_value(soup, 'lf_linkdate')
        lf_title = self._get_param_value(soup, 'lf_title')
        lf_description = soup.find('textarea',
                                   attrs={'name': 'lf_description'}).text
        lf_tags = soup.find('input', attrs={'name': 'lf_tags'})['value']

        # Merge
        tags += lf_tags.split()
        if lf_description != '':
            desc = "%s | %s:  %s" % (lf_description,
                                     datetime.now().isoformat(),
                                     desc)

        # Submit save form
        r = self._SESSION.post('%s?post=%s' % (self._URL, url), {
            'lf_linkdate': lf_linkdate,
            'lf_url': url,
            'lf_title': lf_title,
            'lf_description': desc,
            'lf_tags': ' '.join(set(tags)),
            'save_edit': 'Enregistrer',
            'token': self._TOKEN
            })
        soup = BeautifulSoup(r.content, 'html.parser')
        self._TOKEN = self._get_param_value(soup, 'token')
