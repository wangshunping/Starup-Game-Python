#coding: utf-8
'''
    Time: 2015.10.4
    Author: Lionel
    Content: print with color
'''
'''
2017-08-01 ienlaw
添加windwos颜色支持
'''


import os
from termcolor import colored, cprint
from windows_color import *

if os.name in 'nt' :
    print_red_on_cyan = lambda i:printDarkRed(str(i)) if type(i) == type(int()) else printDarkRed(i)
    print_grey = lambda i:printDarkGray(str(i)) if type(i) == type(int()) else printDarkGray(i)
    print_red = lambda i:printRed(str(i)) if type(i) == type(int()) else printRed(i)
    print_green = lambda i:printGreen(str(i)) if type(i) == type(int()) else printGreen(i)
    print_yellow = lambda i:printYellow(str(i)) if type(i) == type(int()) else printYellow(i)
    print_blue = lambda i:printBlue(i) if type(i) == type(unicode()) else printBlue(str(i))
    print_magenta = lambda i:printPink(str(i)) if type(i) == type(int()) else printPink(i)
    print_cyan = lambda i:printSkyBlue(str(i)) if type(i) == type(int()) else printSkyBlue(i)
    print_white = lambda i:printWhite(str(i)) if type(i) == type(int()) else printWhite(i)
else:
    print_red_on_cyan = lambda x: cprint(x, 'red', 'on_cyan', end='')
    print_grey = lambda x:cprint(x, 'grey', end='')
    print_red = lambda x:cprint(x, 'red', end='')
    print_green = lambda x:cprint(x, 'green', end='')
    print_yellow = lambda x:cprint(x, 'yellow', end='')
    print_blue = lambda x:cprint(x, 'blue', end='')
    print_magenta = lambda x:cprint(x, 'magenta', end='')
    print_cyan = lambda x:cprint(x, 'cyan', end='')
    print_white = lambda x:cprint(x, 'white', end='')
