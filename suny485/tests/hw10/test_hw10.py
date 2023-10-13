import pytest
from suny485.projects.hw10.fruit_query import is_it_a_fruit

"""
Checking to make sure that apple appears in the list
Have a test case that doesn't have a fruit name in the code and check if it can return False
Since the list is made of strings only, there shouldn't be tuples so I can create a test file providing that there's no tuples
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


