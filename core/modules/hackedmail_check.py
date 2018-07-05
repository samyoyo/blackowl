#!/usr/bin/env python
# -*- coding: utf-8 -*-
#description:Check if email as been hacked.

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
        self.title = "Hackedmail Check\n"
        self.require = {
            'email':{'value':'', 'required':'yes'},
            'search_paste':{'value':'', 'required':'no'}
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
        search_paste = self.get_options('search_paste')
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                'Accept-Encoding': 'none',
                'Accept-Language': 'en-US,en;q=0.8',
                'Connection': 'keep-alive'}
        try:
            print "{} Try loading email: {}".format(C.WAR, email)
            req = requests.get('https://haveibeenpwned.com/api/v2/breachedaccount/{}'.format(email), headers=headers, verify=True)
            flag = True
        except:
            print "{} Can't open URL".format(C.ERROR)
            flag = False

        if flag == True:
            if len(req.content) == 0:
                print "No pwnage found!"
            else:
                print "{} Email: {}".format(C.OK, email)
                print "Breaches you were pwned in:\n"
                json_loads = json.loads(req.content.decode('ascii', 'ignore'))
                for i, item in enumerate(json_loads):
                    result = """ {}{}{}:
    - Domain:         {}
    - Date:           {}
    - Fabricated:     {}
    - Verified:       {}
    - Retired:        {}
    - Spam:           {}
    """.format(C.BOLD, item['Title'], C.END, item['Domain'], item['BreachDate'],
item['IsFabricated'], item['IsVerified'], item['IsRetired'], item['IsSpamList'])
                    print result
                    self.export.append(result)

                print "Pwned on {}{}{} breached\n".format(C.GREEN, i+1, C.END)
                if search_paste != '':
                    print "{} Search 'paste'\n".format(C.OK)
                    req = requests.get('https://haveibeenpwned.com/api/v2/pasteaccount/{}'.format(email), headers=headers)
                    if req.status_code != 200:
                        print "{} Not found".format(C.ERROR)
                    else:
                        json_loads = json.loads(req.content.decode('ascii', 'ignore'))
                        for item in json_loads:
                            if item['Source'] == 'Pastebin':
                                pastebin = "https://pastebin.com/raw/{}".format(item['Id'])
                                print ' - ' + pastebin
                                self.export.append(pastebin)
