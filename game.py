#coding: utf-8

""" LionelOne.

Usage:
  game.py staff
  game.py start
  game.py (-h | --help)
  game.py --version

Options:
  start         Let's Begin the Game
  staff         Thanks to all contributors
  -h --help     Show this screen.
  --version     Show version.
"""
from docopt import docopt
from core.hire_system import HireSystem
from core.startup_game import StartUpGame

def start():
    '''start up game'''
    game = StartUpGame()
    game.opening()
    game.hire_coders()
    game.run()

def staff():
    ''' Thanks to all contrubutors coder '''
    HireSystem.staff()

if __name__ == '__main__':
    arguments = docopt(__doc__, version=u'南山启示录 V0.1')

    if arguments['start']:
        start()
    if arguments['staff']:
        staff()
    else:
        ## whatever
        start()

