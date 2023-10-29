import pytest
from suny485.projects.hw12.hw12_code import compute_complexity
"""
Test Cases:
happy path:
    - inputs: 
        - char in the list "data" return expected value (float)
unhappy path:
    - inputs:
        - non char that's not in the list return a float value
        - char in the list returns wrong value (wrong float or non float)
"""

@pytest.mark.parametrize('happy_char', [('~@', 100.0)])

def test_input_happy(happy_char):
    char, num_complexifiers = happy_char
    happy_char = compute_complexity(char)
    assert happy_char == num_complexifiers


@pytest.mark.parametrize('non_char', [('1', 0.0)])

def test_nonchar_input(non_char):
    char, num_complexifiers = non_char
    non_char = compute_complexity(char)
    assert non_char == num_complexifiers


@pytest.mark.parametrize('unhappy_char', [('#&_', 25.0)])

def test_unhappy_input(unhappy_char):
    char, num_complexifiers = unhappy_char
    unhappy_char = compute_complexity(char)
    assert unhappy_char != num_complexifiers


