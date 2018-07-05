#!/usr/bin/env python

class Palette:
    #colors
    RED = '\033[1;31m'
    YELLOW = '\033[33m'
    GREEN = '\033[32m'
    BOLD = '\033[1m'
    END = '\033[0m'

    # extras
    ERROR = "[{}X{}]".format(RED, END)
    OK = "[{}+{}]".format(GREEN, END)
    WAR = "[{}!{}]".format(YELLOW, END)
