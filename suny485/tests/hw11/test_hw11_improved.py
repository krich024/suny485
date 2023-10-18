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
        assert get_formal_name('cranberry') != 'Punica granatum'


class TestFormalCap(object):
    def test_formal_cap(self):
        assert get_formal_name('Pineapple') != 'Ananas comosus'


class TestIntFloatFormal(object):
    def test_formal_int_float(self):
        assert get_formal_name('10') != 'Citrullus lanatus'
        assert get_formal_name('5.0') != 'Vitis vinifera'


class TestListError(object):
    def test_list_error(self):
        assert get_formal_name({'apple', 'banana'}) != {'Malus domestica', 'Musa acuminata'}
        assert get_formal_name(['orange', 'strawberry']) != ['Citrus × sinensis', 'Fragaria × ananassa']
        assert get_formal_name(('grape', 'pineapple')) != ('Vitis vinifera', 'Ananas comosus')


class TestSwitchFormal(object):
    def test_switch_formal(self):
        assert get_formal_name('Prunus domestica') != 'plum'
        assert get_formal_name('Persea americana') != 'avocado'
        assert get_formal_name('Citrus × paradisi') != 'grapefruit'






