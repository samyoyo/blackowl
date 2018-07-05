#!/usr/bin/env python
# -*- coding: utf-8 -*-
#description:Obtain IP geolocation information.

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
        self.title = "IP Geolocation\n"
        self.require = {
            'ip':{'value':'', 'required':'no'}
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
        ip = self.get_options('ip')
        server = "http://ip-api.com/json/"
        server = server + ip if ip != '' else server
        try:
            print "{} Try loading ip: {}".format(C.WAR, ip)
            req = requests.get(server)
            content = json.loads(req.content)
            flag = True
        except:
            print "{} Can't open URL".format(C.ERROR)
            flag = False

        if flag == True:
            if content['status'] == 'fail':
                print "{} Not information".format(C.ERROR)
            else:
                print "{} Information obtained: {}\n".format(C.OK, content['query'])
                google_maps = "http://google.com/maps/place/{0},{1}/@{0},{1},16z".format(content['lat'], content['lon'])
                result = {
                    'IP': content['query'],
                    'Country': '{}, {}'.format(content['country'], content['countryCode']),
                    'Region':'{}, {}'.format(content['regionName'], content['region']),
                    'City':'{}, {}'.format(content['city'], content['zip']),
                    'Latitude':content['lat'],
                    'Longitude':content['lon'],
                    'Google Maps':google_maps,
                    'Timezone':content['timezone'],
                    'ISP':content['isp'],
                    'Organization':content['org'],
                    'AS':content['as']
                }
                for item in result.items():
                    print " {}{:15}{}: {}".format(C.BOLD, item[0], C.END, item[1])
                    self.export.append( "{}{:15}{}: {}".format(C.BOLD, item[0], C.END, item[1]) )
