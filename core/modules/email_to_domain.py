#!/usr/bin/env python
# -*- coding: utf-8 -*-
#description:Get domain with email.

from core.lib import colors
from core.lib import completer
import readline
import re

#requirements
import requests

#colors
C = colors.Palette()


class module_element(object):

    def __init__(self):
        self.title = "Email Whois Gathering\n"
        self.require = {
            'email':{'value':'', 'required':'yes'}
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
        email = self.get_options('email')
        url = "https://whoisology.com/search_ajax/search?action=email&value="+email+"&page=1&section=admin"
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                'Accept-Encoding': 'none',
                'Accept-Language': 'en-US,en;q=0.8',
                'Connection': 'keep-alive'}

        try:
            print "{} Try loading email: {}".format(C.WAR, email)
            req = requests.get(url, headers=headers)
            content = req.content
            flag = True
        except:
            print "{} Can't open URL".format(C.ERROR)
            flag = False

        if content != '' and flag == True:
            regex = re.compile('whoisology\.com\/(.*?)">')
            regex = regex.findall(content)
            if len(regex) == 0:
                print "{} Empty domain result for email: {}{}{}".format(C.ERROR, C.RED, email, C.END)
            else:
                print "{} Domains found for email: {}\n".format(C.OK, C.GREEN, email, C.END)
                for line in regex:
                    if line.strip() != '':
                        if line not in self.export and '.' in line:
                            self.export.append(line)
                            print " - {}".format(line)
