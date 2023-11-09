import pytest
from suny485.projects.hw11.formal_fruit import get_formal_name

"""
Test Cases:
    - happy path:
        - key input equals to the correct value
    - unhappy path:
        - wrong key input does not equal to the correct value
        - using ints as key (for listed ordered ex: apple is 1, banana is 2 etc.
    KeyError:
    - inputs:
        - tuples
        - dict key that doesn't belong to dict value
        - capitalizing key value that will not match with dict value
TypeError:
    - inputs:
        - list, set   
"""

@pytest.mark.parametrize('happy', [('apple', 'Malus domestica')],
                         ids=['apple']
                         )
def test_input_apple(happy):
    name, sci_name = happy
    actual_name = get_formal_name(name)
    assert actual_name == sci_name


@pytest.mark.parametrize('unhappy', [('avocado', 'Punica granatum')],
                         ids= ['avocado'])

def test_input_unhappy(unhappy):
    name, sci_name = unhappy
    wrong_name = get_formal_name(name)
    assert wrong_name != sci_name


@pytest.mark.parametrize('int', [('5', 'Vitis vinifera')],
                         ids = ['5'])

def test_input_int(int):
    with pytest.raises(KeyError):
        name, sci_name = int
        int_name = get_formal_name(name)
        assert int_name != sci_name


@pytest.mark.parametrize("fruit_list, sci_list", [(['apple', 'banana'], ['Malus domestica', 'Musa acuminata'])])

def test_typeerror_input(fruit_list, sci_list):
    with pytest.raises(TypeError):
        assert get_formal_name(fruit_list) != sci_list


@pytest.mark.parametrize("fruit_set, sci_set", [({'orange', 'strawberry'}, {'Citrus × sinensis', 'Fragaria × ananassa'})],
                         )

def test_typeerror_set(fruit_set, sci_set):
    with pytest.raises(TypeError):
        assert get_formal_name(fruit_set) != sci_set


@pytest.mark.parametrize('cap', [('Apple', 'Malus domestica')], ids = ['Apple'])

def test_cap_input(cap):
    with pytest.raises(KeyError):
        name, sci_name = cap
        cap_name = get_formal_name(name)
        assert cap_name != sci_name

@pytest.mark.parametrize("tuple, output", [(('mango', 'Mangifera indica'), True)], ids = ['mango'])

def test_tuple_input(tuple, output):
    with pytest.raises(KeyError):
        assert get_formal_name(tuple) == output

