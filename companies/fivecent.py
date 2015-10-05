'''
    Time: 2015.10.2
    Author: Lionel
    Content: Company named FiveCent
'''
from core.company import Company

class Fivecent(Company):
    def __init__(self):
        self.angel_fund = 200000
        self.money = self.angel_fund