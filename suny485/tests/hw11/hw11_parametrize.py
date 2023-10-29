import pytest
from suny485.projects.hw11.formal_fruit import get_formal_name

"""
Test Cases:
    - happy path:
        - key input equals to the correct value
    - unhappy path:
        - wrong key input does not equal to the correct value
"""

@pytest.mark.parametrize('str', [('apple', 'Malus domestica')]
                         )
def test_input_apple(str):
    name, sci_name = str
    actual_name = get_formal_name(name)
    assert actual_name == sci_name


@pytest.mark.parametrize('unhappy', [('avocado', 'Punica granatum')])

def test_input_unhappy(unhappy):
    name, sci_name = unhappy
    wrong_name = get_formal_name(name)
    assert wrong_name != sci_name
