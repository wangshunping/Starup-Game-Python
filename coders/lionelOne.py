# coding: utf-8
'''
    Time: 2015.10.3
    Author: Lionel
    Content: coder Wangshunping
'''
from random import randint
from jobs.coder import Coder
from utils.my_color_print import *

class lionelOne(Coder):
    name = u'汪小小'
    salary = 7500

    @classmethod
    def work(cls, remain_difficulty):
        seed = randint(0, 9)
        if seed > 4:
            forward = randint(10, 100)
            print u"%s刚跑了8公里，精神状态良好，成功完成项目%s"\
                 %(cls.name, forward)
            remain_difficulty -= forward
        else:
            forward = randint(1, 5)
            print u"%s昨晚补番补到大半夜，严重睡眠不足，项目只推进了%s"\
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

