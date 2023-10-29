import pytest
from suny485.projects.hw11.formal_fruit import get_formal_name

'''
Test Cases:
happy path:
    - inputs:
       - values that match the correct key
unhappy path:
    - inputs:
       - values that don't match the correct key
       - using ints as key (for listed ordered ex: apple is 1, banana is 2 etc.
KeyError:
    - inputs:
        - tuples
        - dict key that doesn't belong to dict value
        - capitalizing key value that will not match with dict value
TypeError:
    - inputs:
        - list, set   
'''

class TestFormalHappy(object):
    def test_happy_apple(self):
        assert get_formal_name('apple') == 'Malus domestica'
    def test_happy_strawberry(self):
        assert get_formal_name('strawberry') == 'Fragaria × ananassa'


class TestFormalUnhappy(object):
    def test_unhappy_keyerror_peach(self):
            assert get_formal_name('peach') != 'Citrullus lanatus'


class TestKeyIntFormal(object):
    def test_key_error(self):
        with pytest.raises(KeyError):
            assert get_formal_name('5') != 'Vitis vinifera'


class TestTypeError(object):
    def test_type_error(self):
        with pytest.raises(TypeError):
            assert get_formal_name(['apple','banana']) == ['Malus domestica', 'Musa acuminata']

    def test_set_error(self):
        with pytest.raises(TypeError):
            assert get_formal_name({'orange', 'strawberry'}) == {'Citrus × sinensis', 'Fragaria × ananassa'}


class TestFormalCap(object):
    def test_cap_fruit(self):
        with pytest.raises(KeyError):
            assert get_formal_name('Apple') == 'Malus domestica'


class TestFormalTuple(object):
    def test_formal_tuple(self):
        with pytest.raises(KeyError):
            assert get_formal_name(('mango', 'peach')) == True



