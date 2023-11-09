import pytest
from suny485.projects.hw12.hw12_code import compute_complexity
"""
Test Cases:
happy path:
    - input: 
        - char in the list
    - output:
        - returns 100.0 since all characters are complexifiers
unhappy path:
    - inputs:
        - non char that's not in the list return a float value
        - char in the list returns wrong value (wrong float or non float)
        - empty str
    - outputs:
        - returns 0.0
        - 50.0 if non char are added to char complexifiers
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


@pytest.mark.parametrize('empty_list', [([''], 0.0)])

def test_empty_list(empty_list):
    non_char, num_complexifiers = empty_list
    empty_complexifier = compute_complexity(non_char)
    assert empty_complexifier == num_complexifiers


@pytest.mark.parametrize('int_and_char', [('abc~@#', 50.0)])

def test_int_and_char(int_and_char):
    intchar, num_complexifiers = int_and_char
    int_char = compute_complexity(intchar)
    assert int_char == num_complexifiers

@pytest.mark.parametrize('nonchar_and_int', [('abc*(;', 0.0)])

def test_nonchar_and_int(nonchar_and_int):
    nonchar_int, num_complexifiers = nonchar_and_int
    char_int = compute_complexity(nonchar_int)
    assert char_int == num_complexifiers





