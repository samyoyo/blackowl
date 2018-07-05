#!/usr/bin/env python
# -*- coding: utf-8 -*-
#description:CMS Detection.

from core.lib import colors
from core.lib import completer
import readline
import json

#requirements
import requests

#colors
C = colors.Palette()


class module_element(object):

    def __init__(self):
        self.title = "CMS Gathering\n"
        self.require = {
            'website':{'value':'', 'required':'yes'}
        }

        self.export = []

        #completer
        comp = completer.Module(self.require)
        readline.parse_and_bind("tab: complete")
        readline.set_completer(comp.complete)

        self.cms_dirs = {
            'wordpress':['/wp-includes/', '/wp-admin/', '/wordpress/', '/wp-json/', '/wp-content/' ],
            'joomla':['/administrator/', '/static/frontend/', '/includes/'],
            'magento':['/static/frontend/', '/frontend/default/']
        }

        self.cms_content = {
            'Blogger':['content="blogger', "content='blogger"],
            'WordPress':['content="WordPress', "content='WordPress"],
            'Ghost':['content="Ghost', "content='Ghost"],
            'ASCiiDOC':['content="AsciiDoc"', "content='AsciiDoc"],
            'Drupal':['content="Drupal', "content='Drupal"],
            'Browser CMS':['content="BrowserCMS', "content='BrowserCMS"],
            'joomla':['content="Joomla!', "content='Joomla!", 'joomla' ]
        }

        self.status_code = [200, 403, 301, 302]


    def get_options(self, name):
        if name in self.require:
            return self.require[name]['value']
        else:
            return False


    def main(self):
        print "{}{} Running module: {}{}".format(C.OK, C.GREEN, self.title, C.END)
        website = self.get_options('website')
        header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                'Accept-Encoding': 'none',
                'Accept-Language': 'en-US,en;q=0.8',
                'Connection': 'keep-alive'}

        if not '://' in website:
            website = 'http://' + website
        if website[-1:] == '/':
            website = website[:-1]

        try:
            print "{} Try loading website: {}".format(C.WAR, website)
            req = requests.get(website, headers=header)
            content = req.content.decode('utf8')
            flag = True
        except:
            print "{} Can't load URL".format(C.ERROR)
            flag = False

        if flag == True:
            print "{} Checking Content".format(C.OK)
            traces = 0
            for line in self.cms_content:
                for path in self.cms_content[line]:
                    if path in content:
                        traces += 1
                result = "{:13} : {}{}{} matches found".format(line, C.GREEN, traces, C.END)
                self.export.append(result)
                print ' - ' + result
                traces = 0

            print "{} Checking Directories".format(C.OK)
            for line in self.cms_dirs:
                for path in self.cms_dirs[line]:
                    url = website + path
                    req = requests.get(url)
                    if req.status_code in self.status_code:
                        result = "possibly use: {}{}{} with: {}".format(C.GREEN, line, C.END, url)
                        self.export.append(result)
                        print ' - ' + result
