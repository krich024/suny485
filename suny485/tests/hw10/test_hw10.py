import pytest
from suny485.projects.hw10.fruit_query import is_it_a_fruit

"""
Test cases for the types of inputs that are allowed to be added
Identifying what could happen if we use different list types
If I add in the wrong input, a error should appear.
If I capitalize the string, would it raise an error or pass?
"""

class TestFruitHappy(object):
    def test_happy_apple(self):
        assert is_it_a_fruit('apple') == True


class TestFruitUnhappy(object):
    def test_unhappy_fruit(self):
        assert is_it_a_fruit('orange') == False


class TestFruitTuples(object):
    def test_tuples_fruit(self):
        assert is_it_a_fruit(("apple", "grape")) == False


class TestFruitSet(object):
    def test_set_fruit(self):
        assert is_it_a_fruit({"apple", "pear"}) == False


class TestFruitBad(object):
    def test_bad_fruit(self):
        assert is_it_a_fruit('red') == False

class TestFruitGood(object):
    def test_good_fruit(self):
        assert is_it_a_fruit('grape') == True


class TestFruitInt(object):
    def test_fruit_int(self):
        assert is_it_a_fruit('3') == False


class TestFruitFloat(object):
    def test_fruit_float(self):
        assert is_it_a_fruit('2.0') == False


class TestFruitCap(object):
    def test_cap_fruit(self):
        assert is_it_a_fruit('Pear') == False
