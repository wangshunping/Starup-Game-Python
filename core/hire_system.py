#: coding: utf-8
'''
    Time: 2015.9.30
    Author: Lionel
    Content : hire System
'''
import os
from utils.common_func import keyboard
from utils.my_color_print import print_red_on_cyan
from random import randint

class HireSystem(object):
    def __init__(self, game):
        self.coders = []
        self.game = game
        self.min_coders = 1
        self.max_coders = 3
        self.avaliable_coders = self.load_coders()

    @classmethod
    def staff(cls):
        print_red_on_cyan(u'Many thanks to :'+','.join(map(lambda x: x.name, cls.load_coders())))

    @staticmethod
    def estimate():
        test_times = 1000
        coders_rank = []
        for coder in self.avaliable_coders:
            progress = 0
            salary = 0
            form = 1000000
            for x in range(test_times):
                to = coder.work(form)
                progress += (form - to)
                salary += coder.salary
                form = to
            coder_rank = {
                'avg_salary': salary/test_times,
                'avg_process': process/test_times,
                'coder': coder
            }
            coders_rank.append(coder_rank)
        """
        to Do: useless func
        """

    def start_hire(self):
        self.hire()
        print ''
        print ','.join(map(lambda x: x.name, self.coders)) + u'带着发家致富的梦想加入的团队。'
        keyboard.next()

    def hire_or_not(self):
        if not self.could_hire():
            return
        print ''
        print u'你有空余的工位, 你需要招募员工么'
        if keyboard.confirm():
            self.hire()

    def fire_or_not(self):
        if not self.could_fire():
            return
        print ''
        print u'你可以解雇让你不爽的员工'
        if keyboard.confirm():
            self.fire()

    def hire(self):
        print u"你可以最多可以雇佣%s名员工，请谨慎选择:" %(self.max_coders)
        keyboard.next()

        #: if has coder could hire
        if not self.could_hire():
            return

        #: if coder is too little
        while len(self.coders) < self.min_coders:
            print u'你至少需要%s名员工加入你的团队!' %(self.min_coders)
            self._hire()

        #: if exit hire
        while len(self.coders) < self.max_coders:
            print "------------------"
            print "当前雇佣程序员人数 %s" %len(self.coders)
            print "------------------"
            print u"是否结束雇佣，确认按 Y"
            if keyboard.confirm():
                break
            else:
                self._hire()

    def _hire(self):
        coder = self.avaliable_coders[randint(0, len(self.avaliable_coders)-1)]
        print '------'
        print u"%s: %s 薪水： %s"%(coder.job, coder.name, coder.salary)
        if keyboard.confirm():
            self.coders.append(coder)
            self.avaliable_coders.remove(coder)
            print u"%s加入了你的团队。"%(coder.name)


    def fire(self):
        if not self.could_fire():
            return
        for coder in self.coders:
            if not self.could_fire():
                return
            print '--------'
            print u"%s: %s 薪水： %s"%(coder.job, coder.name, coder.salary)
            if keyboard.confirm():
                self.coders.pop(self.coders.index(coder))
                print u"%s退出了你的团队。"%(coder.name)
            if len(self.coders) < self.min_coders:
                print u'你至少需要%s名员工加入你的团队!' %(self.min_coders)
                self.hire()
                return

    def could_hire(self):
        return len(self.coders) < self.max_coders

    def could_fire(self):
        return len(self.coders) > self.min_coders

    @classmethod
    def load_coders(cls):
        my_coders = []
        coder_list = os.listdir(os.getcwd()+'/coders')
        coder_list = [x.split('.')[0] for x in coder_list if ('init' not in x) and ('.pyc' not in x)]
        #print coder_list
        for coder in coder_list:
            tmp = __import__('coders.'+coder, {}, {}, [coder])

            my_coders.append(getattr(tmp, coder))
        return my_coders
