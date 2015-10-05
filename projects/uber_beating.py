'''
    Time: 2015.10.2
    Author: Lionel
    Content: Company named FiveCent
'''
from core.company import Company

class UberBeating(Company):
    def __init__(self):
        self.estimate_project_difficulty = 10000
        self.remain_difficulty = self.estimate_project_difficulty