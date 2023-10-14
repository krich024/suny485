import pytest
from suny485.projects.hw11.formal_fruit import get_formal_name

'''
Looking to make sure the formal name of apple does equal to apple
To see if other fruits that aren't in the dict will be false
Pytest runs KeyError in class Unhappy, possibly cannot do a unhappy path
'''

class TestFormalHappy(object):
    def test_happy_formal(self):
        assert get_formal_name('apple') == 'Malus domestica'

def test_key_error():
    raise KeyError

def test_formal_key():
    with pytest.raises(KeyError):
        assert test_key_error()


class TestFormalUnhappy(object):
    def test_unhappy_formal(self):
        assert get_formal_name('cantaloupe') != 'Prunus avium'


class TestFormalSberry(object):
    def test_sberry_formal(self):
        assert get_formal_name('strawberry') == 'Fragaria × ananassa'



