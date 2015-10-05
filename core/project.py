'''
    Time: 2015.10.2
    Author: Lionel
    Content: Project
'''
class Project(object):
    def __init__(self, name=None):
        self.__name = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

