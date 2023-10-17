import pytest
from suny485.projects.hw11.formal_fruit import get_formal_name

'''
The code should have a key that is equal to the value given in the dict
If I add a nonexistent key that is equal to a nonexistent value, it should raise a KeyError
If I create a test case for a list, tuple, set etc, it will raise a TypeError
Raises KeyError for tuple, Raises TypeError for list and set
'''

class TestFormalHappy(object):
    def test_happy_formal(self):
        assert get_formal_name('apple') == 'Malus domestica'
        assert get_formal_name('strawberry') == 'Fragaria × ananassa'


class TestFormalUnhappy(object):
    def test_unhappy_formal(self):
        with pytest.raises(KeyError):
            assert get_formal_name('cantaloupe') != 'Prunus avium'


class TestKeyFormal(object):
    def test_key_error(self):
        with pytest.raises(KeyError):
            assert get_formal_name('Persea americana') != '5'


class TestTypeError(object):
    def test_type_error(self):
        with pytest.raises(TypeError):
            assert get_formal_name(['apple','banana']) == False
            assert get_formal_name({'orange', 'strawberry'}) == True


class TestFormalCap(object):
    def test_cap_fruit(self):
        with pytest.raises(KeyError):
            assert get_formal_name('Apple') == 'Malus domestica'


class TestFormalTuple(object):
    def test_formal_tuple(self):
        with pytest.raises(KeyError):
            assert get_formal_name(('mango', 'peach')) == True
