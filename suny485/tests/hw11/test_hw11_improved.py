import pytest
from suny485.projects.hw11.formal_fruit_improved import real_fruit_name

"""
Checking for any of the formal fruit names exist in this set
"""


class TestOneFormalFruit(object):
    def test_one_formal_fruit(self):
        assert real_fruit_name('Malus domestica') == 'apple'


class TestWrongFormalFruit(object):
    def test_wrong_formal_fruit(self):
        assert real_fruit_name('apple') == False
