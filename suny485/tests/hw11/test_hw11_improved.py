import pytest
from suny485.projects.hw11.hw11_improved import get_formal_name
"""
Test Cases:
happy path:
    - inputs:
       - values that match the correct key
unhappy path:
    - inputs:
       - values that don't match the correct key
       - switching dict value and key value
       - using ints as key (for listed ordered ex: apple is 1, banana is 2 etc.
KeyError:
    - inputs:
        - tuples
        - dict key that doesn't belong to dict value
        - capitalizing key value that will not match with dict value
TypeError:
    - inputs:
        - list, set   

Try Except:
    - inputs:
       - every wrong key value prints the KeyError message given in code
       - every wrong str prints the TypeError message given in code
"""


class TestBadKey(object):
    def test_bad_key(self):
        expected_message = 'This Key does not exist in this dict'
        assert get_formal_name(10) == expected_message


class TestTypeError(object):
    def test_bad_type(self):
        error_message = "This Type doesn't belong to dict"
        assert get_formal_name(['']) == error_message


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


