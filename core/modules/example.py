#!/usr/bin/env python
# -*- coding: utf-8 -*-
#description:This is example.

from core.lib import colors
from core.lib import completer
import readline

#colors
C = colors.Palette()


class module_element(object):

    def __init__(self):
        self.title = "Example\n"
        self.require = {
            'enterprise':{'value':'', 'required':'yes'},
            'function':{'value':'', 'required':'no'}
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

        # ------------------------------- #
        # delete this and write your code #
        # ------------------------------- #
        enterprise = self.get_options('enterprise')
        function = self.get_options('function')
        print " Enterprise: {}\n Function: {}\n\n Passwords fond:".format(enterprise, function)
        passwords = [
                'user:123456 :: pass:12345',
                'user:qwerty :: pass:uiop',
                'user:qwaszx :: pass:xzsawq'
        ]
        for line in passwords:
            print " - " + line
            self.export.append(line)
        print "\n Please execute: export"
