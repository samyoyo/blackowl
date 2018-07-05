#!/usr/bin/env python
from core import menus

import os
import glob
import readline

class Main(object):

    def __init__(self):
        self.commands = [c[0] + ' ' for c in menus.main_menu.items()]
        self.modules = self.get_list_modules()

    def get_list_modules(self):
        route = 'core/modules/'
        list_modules = []
        if not os.path.exists(route):
            list_modules = ['Not modules']
        else:
            modules = glob.glob(route + '*.py')
            for module in modules:
                module_name = module.split('.py')[0]
                module_name = module_name.replace('core/modules/', '')
                if '__init__.py' not in module:
                    list_modules.append(module_name)
            return list_modules

    def complete(self, text, state):
        line = readline.get_line_buffer()
        options = [ c for c in self.commands if c.startswith(text)] + [None]
        if 'use' in line:
            options = [ m for m in self.modules if m.startswith(text)] + [None]
        return options[state]

class Module(object):

    def __init__(self, require):
        self.commands = [c[0] + ' ' for c in menus.module_menu.items()]
        self.requirements = self.get_list_requirements(require)

    def get_list_requirements(self, require):
        list_requirements = []
        for r in require.items():
            list_requirements.append(r[0])
        return list_requirements

    def complete(self, text, state):
        line = readline.get_line_buffer()
        options = [ c for c in self.commands if c.startswith(text)] + [None]
        if 'set' in line:
            options = [ m for m in self.requirements if m.startswith(text)] + [None]
        return options[state]

