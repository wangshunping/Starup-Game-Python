#coding: utf-8
from core.hire_system import HireSystem

def test_load_coders():
    coders = HireSystem.load_coders()
    assert isinstance()

def test_load_coders_get_name():
    coders = HireSystem.load_coders()
    coders_name = map(lambda x:x.name, coders)
    assert isinstance(coders_name, list)


if __name__ == '__main__':
    coders = HireSystem.load_coders()