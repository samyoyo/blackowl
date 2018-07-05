#!/usr/bin/env python
# -*- coding: utf-8 -*-
#description:Whois information for domain.

from core.lib import colors
from core.lib import completer
import readline

#requirements
import pythonwhois

#colors
C = colors.Palette()


class module_element(object):

    def __init__(self):
        self.title = "Whois Domain\n"
        self.require = {
            'domain':{'value':'', 'required':'yes'}
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

        domain = self.get_options('domain')
        if '://' in domain:
            domain = domain.split('://')[1]
        if domain[-1] == '/':
            domain = domain[:-1]

        try:
            print "{} Try loading domain: {}".format(C.WAR, domain)
            whois = pythonwhois.get_whois(domain)
            info = whois['raw'][0]
            info = info.split('>>>')[0]
            info = info.split('\n')
            flag = True
        except:
            print "{} Can't open URL".format(C.ERROR)
            flag = False

        if flag == True:
            for line in info:
                if line != '':
                    line = line.split(':')
                    if line[1] != '':
                        print " - {:20} : {}{}{}".format(line[0], C.GREEN, line[1], C.END)
