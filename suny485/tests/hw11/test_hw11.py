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
    def test_happy_formal(self):
        assert get_formal_name('apple') == 'Malus domestica'
    def test_happy_key(self):
        assert get_formal_name('strawberry') == 'Fragaria × ananassa'


class TestFormalUnhappy(object):
    def test_unhappy_formal(self):
        with pytest.raises(KeyError):
            assert get_formal_name('cantaloupe') != 'Prunus avium'
    def test_unhappy_key(self):
        with pytest.raises(KeyError):
            assert get_formal_name('peach') != 'Prunus avium'


class TestKeyIntFormal(object):
    def test_key_error(self):
        with pytest.raises(KeyError):
            assert get_formal_name('Persea americana') != '5'


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
