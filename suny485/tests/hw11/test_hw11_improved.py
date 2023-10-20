import pytest
from suny485.projects.hw11.hw11_improved import get_formal_name
"""
If I assign the function to be list, set, tuple then it will lead to me a unhappy path
It will do the same if I used int or float as a dict key
What would happen if I assign a dict key to the wrong value? A KeyError is raised (unhappy path)
If I switched the dict value and equal it to the key value, it will not be equal
"""


class TestHappyFormal(object):
    def test_happy_formal(self):
        assert get_formal_name('grape') == 'Vitis vinifera'


class TestUnHappyFormal(object):
    def test_unhappy_path(self):
        assert get_formal_name('apple') != 'Mangifera indica'


class TestFormalCap(object):
    def test_formal_cap(self):
        assert get_formal_name('Pineapple') != 'Ananas comosus'


class TestIntFormal(object):
    def test_formal_int(self):
        assert get_formal_name('10') != 'Citrullus lanatus'


class TestFloatFormal(object):
    def test_float_formal(self):
        assert get_formal_name('5.0') != 'Vitis vinifera'


class TestSetError(object):
    def test_set_error(self):
        assert get_formal_name({'apple', 'banana'}) != {'Malus domestica', 'Musa acuminata'}


class TestListError(object):
    def test_formal_list(self):
        assert get_formal_name(['orange', 'grape']) != ['Citrus × sinensis', 'Fragaria × ananassa']


class TestTupleError(object):
    def test_tuple_formal(self):
        assert get_formal_name(('pineapple', 'mango')) != ('Ananas comosus')


class TestSwitchFormal(object):
    def test_switch_formal(self):
        assert get_formal_name('Prunus domestica') != 'plum'
