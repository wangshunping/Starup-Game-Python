# coding: utf-8
'''
    Time: 2015.10.02
    Author: Lionel
    Cotent: start up Game Class.
            I am coding in a coffer bar with a girl.
            I love this kind of feel
'''
from utils.common_func import keyboard
from utils.my_color_print import *
from hire_system import HireSystem
from projects.uber_beating import UberBeating
from companies.fivecent import Fivecent


class StartUpGame(object):
    def __init__(self):
        self.week = 0
        self.__company = Fivecent()
        self.__project = UberBeating()
        self.__hire_sys = HireSystem(self)

    def opening(self):
        print u'『2015又是一幅好光景啊』'+u'，加班结束之后的你看了看四周，已是深夜。'
        print u'你握紧了拳头，心想'+u'『我不能再这么加班下去了，我要改变世界』'+u'，灌木丛里的野狗叫了一声，以示鼓励。'
        keyboard.next()
        print u'你决定一起开发一款屌炸天的应用，叫做：'
        self.__project.name = keyboard.input()
        print u'你决定给公司起名为：'
        self.__company.name = keyboard.input()
        print u"你成立了" + self.__company.name.decode('utf-8') +\
              u"你拿出了你毕生的积蓄%s作为%s的启动资金。"\
              %(self.__company.angel_fund, self.__project.name.decode('utf-8'))
        print u'点子和钱都有了，就差几个员工了'
        keyboard.next

    def hire_coders(self):
        self.__hire_sys.start_hire()

    def run(self):
        self.__mvp()

    def __mvp(self):
        print u"经过一番估计, 大家认为%s的开发难度为%s点困难度, 这可是个不小的工程，要加油干了。"\
              %(self.__project.name.decode('utf-8'), self.__project.estimate_project_difficulty)
        keyboard.next()
        while (self.__project.remain_difficulty > 0) and (self.__company.money > 0):
          self.work_one_week()
          keyboard.next()
        if self.__company.money > 0:
          print u"%s的第一版终于撸出来啦，他已经具备基本功能"%(self.__project.name)
          self.beta()
        else:
          print u'资金耗尽，项目失败...'

    def beta(self):
        print_magenta(u'作者正在开发中')

    def work_one_week(self):
        self.week += 1
        old_remain_difficulty = self.__project.remain_difficulty
        print u"第%s周开始了，键盘的敲击声响起"%self.week

        #: random events happen
        self.random_events()

        #: weekly work
        self.weekly_work()

        self.__hire_sys.fire_or_not()
        self.__hire_sys.hire_or_not()

        if (self.week%4 == 0):
            self.pay_salary()

        forword = round(old_remain_difficulty - self.__project.remain_difficulty, 0)
        print u"第",
        print_blue(self.week),
        print u"周结束了，成功完成了",
        print_blue(forword),
        print u"点困难度， 还剩下",
        print_blue(self.__project.remain_difficulty),
        print u"点困难度等待开发"

    def pay_salary(self):
        print '==================发薪水咯=========================='
        old_money = self.__company.money
        for coder in self.__hire_sys.coders:
          self.__company.money = coder.pay(self.__company.money)
        cost = old_money - self.__company.money
        print u"共计发出工资：",
        print_red(cost)
        print u"  ,",
        print_magenta(self.__company.name)
        print u'剩余资金',
        print_red(self.__company.money)
        print '===================================================='

    def random_events(self):
        pass

    def weekly_work(self):
        for coder in self.__hire_sys.coders:
            self.__project.remain_difficulty = coder.work(self.__project.remain_difficulty)
            if self.__project.remain_difficulty < 0:
                self.__project.remain_difficulty = 0
                break
