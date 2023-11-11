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
KeyError:
    - inputs:
        - using ints as key (for listed ordered ex: apple is 1, banana is 2 etc.
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



class TestKeyIntFormal(object):
    def test_key_error(self):
        with pytest.raises(KeyError):
             get_formal_name(5)


class TestTypeError(object):
    def test_type_error(self):
        with pytest.raises(TypeError):
            get_formal_name(['apple', 'banana'])

    def test_set_error(self):
        with pytest.raises(TypeError):
            get_formal_name({'orange', 'strawberry'})


class TestFormalCap(object):
    def test_cap_fruit(self):
        with pytest.raises(KeyError):
            assert get_formal_name('Apple') == 'Malus domestica'


class TestFormalTuple(object):
    def test_formal_tuple(self):
        with pytest.raises(KeyError):
            get_formal_name(('mango', 'Mangifera indica'))
