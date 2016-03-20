# coding: utf-8
'''
    Time: 2015.10.4
    Author: Lionel
    Content: coder bingbing
'''
from random import randint
from jobs.coder import Coder
from utils.my_color_print import *

class bingbing(Coder):
    name = u'小兵兵'
    salary = 15000

    @classmethod
    def work(cls, remain_difficulty):
        seed = randint(0, 9)
        if seed > 4:
            forward = randint(10, 100)
            print u"%s灵感大发，成功将项目推进#%s"\
                 %(cls.name, forward)
            remain_difficulty -= forward
        else:
            forward = randint(1, 5)
            print u"%s进入了拖延症晚期，项目难度增加%s"\
                %(cls.name, forward)
            remain_difficulty -= forward
        return remain_difficulty

    @classmethod
    def pay(cls, company_money):
        print_blue(cls.name)
        print u"领取了" ,
        print_red(cls.salary)
        print u"元工资，然后一路向西去了东莞"
        company_money -= cls.salary
        return company_money

