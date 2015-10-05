from core.hire_system import HireSystem
from core.startup_game import StartUpGame

def test_thx():
    coders = HireSystem.staff()
    assert coders == None

def test_game_open():
    newGame = StartUpGame()
    returnInfo = newGame.opening()
    assert returnInfo == 'qwe'

if __name__ == '__main__':
    newGame = StartUpGame()
    returnInfo = newGame.opening()