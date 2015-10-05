#coding: utf-8
'''
    Date: 2015.09.30
    Author: Lionel
    Content: common function using in game
'''

import sys
from utils.my_color_print import *

class keyboard:
    @staticmethod
    def next():
        print_green(u'(---敲击任意键继续---)')
        raw_input()

    @staticmethod
    def confirm():
        print_green(u'(---按Y确认, 按其他键跳过---)')
        user_input = raw_input().strip()
        if str(user_input).lower() == 'y':
            return True
        else:
            return False

    @staticmethod
    def input():
        print_green(u'(---请输入---)')
        user_input = raw_input().strip()
        return user_input