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
        - using complexifiers for words
        - empty str
    - outputs:
        - returns floats that are < 100.0
"""


@pytest.mark.parametrize('happy_char', [('~@', 100.0)])
def test_input_happy(happy_char):
    char, num_complexifiers = happy_char
    happy_char = compute_complexity(char)
    assert happy_char == num_complexifiers


@pytest.mark.parametrize('int', [('1', 0.0)])
def test_nonchar_input(int):
    char, num_complexifiers = int
    non_char = compute_complexity(char)
    assert non_char == num_complexifiers


@pytest.mark.parametrize('char_spelled', [('n@me', 25.0)])
def test_unhappy_input(char_spelled):
    char, num_complexifiers = char_spelled
    unhappy_char = compute_complexity(char)
    assert unhappy_char == num_complexifiers


@pytest.mark.parametrize('empty_str', [([''], 0.0)])
def test_empty_list(empty_str):
    non_char, num_complexifiers = empty_str
    empty_complexifier = compute_complexity(non_char)
    assert empty_complexifier == num_complexifiers


@pytest.mark.parametrize('letters_and_char', [('abc~@#', 50.0)])
def test_int_and_char(letters_and_char):
    intchar, num_complexifiers = letters_and_char
    int_char = compute_complexity(intchar)
    assert int_char == num_complexifiers


@pytest.mark.parametrize('nonchar_abc', [('abc*(;', 0.0)])
def test_nonchar_and_int(nonchar_abc):
    nonchar_int, num_complexifiers = nonchar_abc
    char_int = compute_complexity(nonchar_int)
    assert char_int == num_complexifiers
