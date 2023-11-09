import pytest
from suny485.projects.hw11.hw11_improved import get_formal_name

"""
Test Cases:
happy path:
    - inputs:
       - values that match the correct key
unhappy path:
    - inputs:
       - values that don't match the correct key
       - switching dict value and key value
       - using ints as key (for listed ordered ex: apple is 1, banana is 2 etc.
KeyError:
    - inputs:
        - tuples
        - dict key that doesn't belong to dict value
        - capitalizing key value that will not match with dict value
        - empty key
TypeError:
    - inputs:
        - list, set   
        - empty list, empty set

Try Except:
    - inputs:
       - every wrong key value prints the KeyError message given in code
       - every wrong str prints the TypeError message given in code
"""


@pytest.mark.parametrize('nonexistent_key', [('no_key', 'This Key does not exist in this dict')], ids = ['no_key'])

def test_keyerror_return_input(nonexistent_key):
    key, key_error = nonexistent_key
    key_input = get_formal_name(key)
    assert key_input == key_error

@pytest.mark.parametrize('list_type', [([''], 'This Type does not belong to dict')], ids = [('')])

def test_typeerror_message_input(list_type):
    type, type_error = list_type
    type_input = get_formal_name(type)
    assert type_input == type_error


@pytest.mark.parametrize('bad_input', [(5, 'This Key does not exist in this dict')])

def test_bad_input(bad_input):
    non_input, error_message = bad_input
    wrong_input = get_formal_name(non_input)
    assert wrong_input == error_message


@pytest.mark.parametrize('type_input', [({''}, 'This Type does not belong to dict')])

def test_type_input_error(type_input):
    set, error_message = type_input
    error_type = get_formal_name(set)
    assert error_type == error_message


@pytest.mark.parametrize('cap', [('Peach', 'Prunus persica')], ids = ['Peach'])

def test_input_cap(cap):
    name, sci_name = cap
    cap = get_formal_name(name)
    assert cap != sci_name


@pytest.mark.parametrize('set_error', [({'apple', 'banana'}, {'Malus domestica', 'Musa acuminata'})])

def test_seterror_input(set_error):
    set_name, sci_set = set_error
    formal_set = get_formal_name(set_name)
    assert formal_set != sci_set

@pytest.mark.parametrize('list_error', [(['orange', 'grape'], ['Citrus × sinensis', 'Fragaria × ananassa'])])

def test_listerror_input(list_error):
    list_name, sci_list = list_error
    actual_list = get_formal_name(list_name)
    assert actual_list != sci_list


@pytest.mark.parametrize('tuple_error', [(('pineapple', 'mango'), ('Ananas comosus', 'Mangifera indica'))])

def test_tupleerror_input(tuple_error):
    tuple_list, sci_tuple = tuple_error
    actual_tuple = get_formal_name(tuple_list)
    assert actual_tuple != sci_tuple


@pytest.mark.parametrize('switch', [('Prunus domestica', 'plum')], ids = ['Prunus domestica'])

def test_switch_input(switch):
    sci_name, name = switch
    switch_name = get_formal_name(sci_name)
    assert switch_name != name


@pytest.mark.parametrize('empty_key', [('', '')])

def test_empty_list(empty_key):
    name, empty_name = empty_key
    non_key = get_formal_name(name)
    assert non_key != empty_name


@pytest.mark.parametrize('empty_list', [([''], [''])])

def test_empty_list(empty_list):
    key_list, sci_list = empty_list
    actual_list = get_formal_name(key_list)
    assert actual_list != sci_list


@pytest.mark.parametrize('empty_set', [({''}, {''})])

def test_empty_set(empty_set):
    key_set, sci_set = empty_set
    actual_set = get_formal_name(key_set)
    assert actual_set != sci_set
