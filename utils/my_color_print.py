#coding: utf-8
'''
    Time: 2015.10.4
    Author: Lionel
    Content: print with color
'''
from termcolor import colored, cprint


print_red_on_cyan = lambda x: cprint(x, 'red', 'on_cyan', end='')

print_grey = lambda x:cprint(x, 'grey', end='')
print_red = lambda x:cprint(x, 'red', end='')
print_green = lambda x:cprint(x, 'green', end='')
print_yellow = lambda x:cprint(x, 'yellow', end='')
print_blue = lambda x:cprint(x, 'blue', end='')
print_magenta = lambda x:cprint(x, 'magenta', end='')
print_cyan = lambda x:cprint(x, 'cyan', end='')
print_white = lambda x:cprint(x, 'white', end='')