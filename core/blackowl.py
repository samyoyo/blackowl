#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.lib import colors
from core import mecanic
from core import menus


C = colors.Palette()
menu = menus.main_menu
banner = """
               y__               __y
               'MOOAooOOOOOOOooOOOM`
                 O\_@@/'O^O`\@@/OO
                 Os.~`\\\|///'~ sO
                 !Oooo_)\|/(_oooO!
                gOO\z\z) Y (z\z\OOs         |=----------------=[{} Black Owl {}]=---------------=|
               gObt_t_t_____t_t_tdOs        |=------------=[{} version: 10.05.18 {}]=-----------=|
              iOO` [ [ [ [ [ [ [ [YOb       |=-----=[{} by:'qwaszx' <qqwaszx(at)pm.me> {}]=-----=|
[]#####D=s_   OOO~P'P'P'P'P'P'P'P'POOb
[],    ~~[]   OOOz\z\z\z\z\z\z\z\z\OOO
[]]       ]   !OOO_t_t_t_t_t_t_t_t_OOO
[][]      []   VOO[ [ [ [ [ [ [ [ [OO!
[][[       [    OOOO/P'P'P'P'P'P'/OOO
[][] [     ]   ,_OOOOO~OOOOO~OYOOO0O
[[[[[[  ===[][~~,_gOOYmWWWmOmWWWWOO_____
 [] []   ====[~~~     \WOOOOOOW/  '~YYYY
 [][][] /              YOOOOOOY
  [][][                  VVVVV~
                          YYY~
""".format(C.YELLOW, C.END, C.YELLOW, C.END, C.YELLOW, C.END)


def user_put():
    print banner
    while 0 != 1:
        try:
            user_input = raw_input(": blackowl > ").split()
            user_input.append('')
        except:
            pass

        if user_input[0] in menu:
            if 'use' == user_input[0] and user_input[1] != '':
                mecanic.load(' '.join(user_input))
            else:
                mecanic.load(menu[user_input[0]])
