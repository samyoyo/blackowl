#!/usr/bin/env python
# -*- coding: utf-8 -*-
#description:Search for subdomain.

from core.lib import colors
from core.lib import completer
import readline

#requirements
from bs4 import BeautifulSoup
import requests

#colors
C = colors.Palette()


class module_element(object):

    def __init__(self):
        self.title = "Subdomain Search\n"
        self.require = {
            'domain':{'value':'', 'required':'yes'},
            'limit_search':{'value':'', 'required':'no'}
        }

        self.export = []

        #completer
        comp = completer.Module(self.require)
        readline.parse_and_bind("tab: complete")
        readline.set_completer(comp.complete)


    def get_options(self, name):
        if name in self.require:
            return self.require[name]['value']
        else:
            return False


    def main(self):
        print "{}{} Running module: {}{}".format(C.OK, C.GREEN, self.title, C.END)
        server = "https://findsubdomains.com/subdomains-of/"
        server = server + self.get_options('domain')
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                'Accept-Encoding': 'none',
                'Accept-Language': 'en-US,en;q=0.8',
                'Connection': 'keep-alive'}
        try:
            print "{} Try loading domain: {}".format(C.WAR, self.get_options('domain'))
            req = requests.get(server, headers=headers)
            html = req.content
            flag = True
        except:
            print "{} Can't load URL".format(C.ERROR)
            flag = False

        if flag == True:
            soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
            soup = soup.findAll('a', attrs={'class':'desktop-hidden', 'href':'javascript:void(0);'})
            limit = self.get_options('limit_search')
            for i, link in enumerate(soup):
                if limit != '':
                    if i+1 >= int(limit):
                        link = link.getText()
                        print ' - {}'.format(link)
                        self.export.append(link)
                        break

                link = link.getText()
                print ' - {}'.format(link)
                self.export.append(link)
