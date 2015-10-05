'''
    Time: 2015.10.2
    Author: Lionel
    Content: Company
'''

class Company(object):
    def __init__(self, name=None):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

