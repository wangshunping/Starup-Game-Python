# coding: utf-8
'''
    Time: 2015.10.4
    Author: Lionel
    Content: coder PC
'''
from random import randint
from jobs.coder import Coder
from utils.my_color_print import *

class pc(Coder):
    name = u'PC哥'
    salary = 10000

    @classmethod
    def work(cls, remain_difficulty):
        seed = randint(0, 9)
        if seed > 4:
            forward = randint(10, 100)
            print u"%s一边上学一边写代码，项目进度推进了%s"\
                 %(cls.name, forward)
            remain_difficulty -= forward
        else:
            forward = randint(1, 5)
            print u"%s撸了一个C++模板，然而并没有什么卵用%s"\
                %(cls.name, forward)
            remain_difficulty -= forward
        return remain_difficulty

    @classmethod
    def pay(cls, company_money):
        print_blue(cls.name)
        print u"领取了" ,
        print_red(cls.salary)
        print u"元工资，现阶段对生活毫无追求的他把所有工资存进了余额宝"
        company_money -= cls.salary
        return company_money

