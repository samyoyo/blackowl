#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core import menus
from core.lib import colors
from core.lib import completer

import os
import sys
import glob
import readline

#colors
C = colors.Palette()

#completer
comp = completer.Main()
readline.parse_and_bind("tab: complete")
readline.set_completer(comp.complete)


class Loader(object):

    def __init__(self, module_class):
        self.module_class = module_class
        self.title = module_class.title
        self.require = module_class.require
        self.export = module_class.export
        self.export_file = ''
        self.export_status = False


    def set_agv(self, argv):
        self.argv = argv


    def show_options(self):
        REQ = "{}[Is required]{}".format(C.RED, C.END)
        POS = "{}+{}".format(C.GREEN, C.END)
        NEG = "{}-{}".format(C.RED, C.END)
        WAR = "{}!{}".format(C.YELLOW, C.END)

	for line in self.require:
	    if self.require[line]['value'] == '':
	        value = 'No value'
	    else:
		value = self.require[line]['value']
	    if self.require[line]['required'] == 'yes':
	        if self.require[line]['value'] != '':
                    print " {}  {:10} : {}".format(POS, line, value)
		else:
                    print " {}  {:10} : {} {}".format(NEG, line, value, REQ)
	    else:
		if self.require[line]['value'] != '':
                    print " {}  {:10} : {}".format(POS, line, value)
		else:
                    print " {}  {:10} : {}".format(WAR, line, value)


    def set_options(self, name, value):
        if name in self.require:
            self.require[name]['value'] = value
        else:
            print "{}{} Option not found.{}".format(C.ERROR, C.RED, C.END)


    def check_require(self):
        for line in self.require:
            if self.require[line]['required'] == 'yes':
                if self.require[line]['value'] == '':
                    return False
        return True


    def run_module(self):
        check = self.check_require()
        if check == False:
            print "{}{} Please set the required parameters.{}".format(C.ERROR, C.RED, C.END)
        else:
            self.module_class.main()


    def export_data(self, argv=False):
        if len(self.export) == 0:
            print "{}{} Module empty result.{}".format(C.ERROR, C.RED, C.END)
        else:
            if self.export_file == "":
                if argv == False:
                    user_input = raw_input(": blackowl({}export file name ?{}) > ".format(C.YELLOW, C.END))
                else:
                    user_input = argv
                if os.path.exists("export/"+user_input):
                    self.export_file = "export/"+user_input
                elif os.path.exists(user_input):
                    self.export_file = user_input
                else:
                    print "{}{} Writing '{}' file.{}".format(C.OK, C.GREEN, user_input, C.END)
                    self.export_file = "export/"+user_input
                    self.export_data()

            elif self.export_status == False:
                file_open = open(self.export_file, "a+")
                file_open.write(self.title)
                for line in self.export:
                    try:
                        file_open.write("- " + line +"\n")
                    except:
                        print "{}{} Can't write element.{}".format(C.ERROR, C.RED, C.END)
                print "{}{} File writed : {}{}".format(C.OK, C.GREEN, self.export_file, C.END)
                file_open.close()
                self.export_status = True


def load(name):
    if 'use' in name:
        load_module(name)
    else:
        globals()[name]()


def show_modules():
    route = 'core/modules/'
    if not os.path.exists(route):
        print "{}{} Modules directory not found.{}".format(C.ERROR, C.RED, C.END)
    else:
        modules = glob.glob(route + '*.py')
        for module in modules:
            module_name = module.split('.py')[0]
            module_name = module_name.replace('core/modules/', '')
            if '__init__.py' not in module:
                description = "No module description found"
                if '#description:' in open(module).read():
                    description = open(module).read().split('#description:')[1]
                    description = description.split('.')[0]
                print " {}-{} {:17} : {}".format(C.GREEN, C.END, module_name, description)


def load_module(name):
    module_name = name.split('use')[1].strip() + '.py'
    module = 'core/modules/' + module_name
    if os.path.exists(module):
        print "{}{} Loading: {}{}".format(C.OK, C.GREEN, module, C.END)
        use_module(module)
    else:
        print "{}{} Module not found.{}".format(C.ERROR, C.RED, C.END)


def use_module(module, argv=False):
    action = 0
    module_name = module.split('.py')[0]
    module_class = ''
    while action == 0:
        if module_class == '':
            module_path = module_name.replace('/', '.')
            mod = __import__(module_path, fromlist=['module_element'])
            module_class = mod.module_element()
        load = Loader(module_class)
        try:
            user_input = raw_input(': blackowl({}{}{}) > '\
                    .format(C.YELLOW, module_name, C.END)).strip()
        except:
            print " ..."
            break

        if argv != False:
            load.set_agv(argv)
        if user_input == 'show_options':
            load.show_options()
        elif 'set' in user_input and '=' in user_input:
            value = user_input.split(' ', 1)[1].split('=')
            load.set_options(value[0], value[1])
        elif user_input == 'run':
            load.run_module()
        elif user_input == 'help':
            for cmd in menus.module_menu.items():
                print " {:13} : {}".format(cmd[0], cmd[1])
        elif user_input == 'clear':
            os.system('clear')
        elif user_input == 'export':
            load.export_data()
        elif user_input == 'exit':
            comp = completer.Main()
            readline.parse_and_bind("tab: complete")
            readline.set_completer(comp.complete)
            break

    print "{}{} Exit module: {}.py {}".format(C.OK, C.GREEN, module_name, C.END)


def generate_module_class():
    action = 0
    if not os.path.isfile('core/modules/example.py'):
        print "{}{} Not exist 'core/modules/example.py' file.{}".format(C.ERROR, C.RED, C.END)
    else:
        while action == 0:
            module_name = raw_input(': blackowl({}New module name ?{}) > '.format(C.YELLOW, C.END))
            if module_name == '':
                break
            module_name = str(module_name.replace(' ', '_').lower())
            if '.py' in module_name:
                module_name = module_name.split('.py')[0]
            if os.path.isfile('core/modules/' + module_name + '.py'):
                print "{}{} Please enter new module name.{}".format(C.ERROR, C.RED, C.END)
            else:
                module_description = raw_input(': blackowl({}New module description ?{}) > '.format(C.YELLOW, C.END))
                if module_description == '':
                    module_description = 'It was not specified'
                new_module_file = open('core/modules/' + module_name + '.py', 'w')
                example_module = open('core/modules/example.py').read()
                if '#description:' in example_module:
                    example_module = example_module.replace('#description:This is example.', '#description:' + str(module_description) + '.')
                new_module_file.write(example_module)
                new_module_file.close()
                print "{}{} Module has been written core/modules/{}.py {}".format(C.OK, C.GREEN, module_name, C.END)
                print "{} -  Now add argument on 'self.require' & write your code in 'def main()'.{}".format(C.GREEN, C.END)
                action = 1


def show_help():
    for cmd in menus.cmd_help.items():
        print " {:11} : {}".format(cmd[0], cmd[1])


def update_tool():
    print "{}{} Checking update ...{}".format(C.OK, C.GREEN, C.END)
    try:
        os.system('git pull')
    except:
        print "{}{} Can't start update, please use: $ git pull{}".format(C.ERROR, C.RED, C.END)


def clear_screen():
    os.system('clear')


def exit_blackowl():
    print "[OFF]"
    sys.exit()
