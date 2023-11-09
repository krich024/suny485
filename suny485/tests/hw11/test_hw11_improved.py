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
KeyError:
    - inputs:
        - tuples
        - dict key that doesn't belong to dict value
        - capitalizing key value that will not match with dict value
        - empty key
        - int
TypeError:
    - inputs:
        - list, set  
        - empty list, empty set

Try Except:
    - inputs:
       - every wrong key value prints the KeyError message given in code
       - every wrong str prints the TypeError message given in code
"""


class TestKeyError(object):
    def test_error_key(self):
        expected_message = 'This Key does not exist in this dict'
        assert get_formal_name(expected_message)


class TestTypeError(object):
    def test_error_type(self):
        error_message = "This Type does not belong to dict"
        assert get_formal_name(error_message)


class TestBadInput(object):
    def test_bad_input(self):
        assert get_formal_name(5) == 'This Key does not exist in this dict'

class TestTypeInput(object):
    def test_type_input(self):
        assert get_formal_name({''}) == 'This Type does not belong to dict'


class TestHappyFormal(object):
    def test_happy_formal(self):
        assert get_formal_name('grape') == 'Vitis vinifera'


class TestUnHappyFormal(object):
    def test_unhappy_path(self):
        assert get_formal_name('apple') != 'Mangifera indica'


class TestFormalCap(object):
    def test_formal_cap(self):
        assert get_formal_name('Pineapple') != 'Ananas comosus'


class TestSetError(object):
    def test_set_error(self):
        assert get_formal_name({'apple', 'banana'}) != {'Malus domestica', 'Musa acuminata'}


class TestListError(object):
    def test_formal_list(self):
        assert get_formal_name(['orange', 'grape']) != ['Citrus × sinensis', 'Fragaria × ananassa']


class TestTupleError(object):
    def test_tuple_formal(self):
        assert get_formal_name(('pineapple', 'mango')) != ('Ananas comosus', 'Mangifera indica')


class TestSwitchFormal(object):
    def test_switch_formal(self):
        assert get_formal_name('Prunus domestica') != 'plum'


class TestEmptyFormal(object):
    def test_empty_formal(self):
        assert get_formal_name('') != ''


class TestEmptyList(object):
    def test_empty_list(self):
        assert get_formal_name(['']) != ['']

class TestEmptySet(object):
    def test_empty_set(self):
        assert get_formal_name({''}) != {''}
