import pytest
from suny485.projects.hw11.hw11_improved import get_formal_name

"""
Test Cases:
    unhappy path:
        - input:
            - capitalizes key input doesn't match to value
            - keyerror if the key input doesn't exist
            - typeerror if given a empty set
"""

@pytest.mark.parametrize('cap', [('Peach', 'Prunus persica')])

def test_input_cap(cap):
    name, sci_name = cap
    cap = get_formal_name(name)
    assert cap != sci_name

@pytest.mark.parametrize('keyerror', [('4', 'Fragaria × ananassa')])

def test_keyerror_input(keyerror):
    name, sci_name = keyerror
    keyerror = get_formal_name('4')
    assert keyerror != sci_name

@pytest.mark.parametrize('typeerror', [{'pineapple', '['']'}])

def test_typeerror_input(typeerror):
    name, sci_name = typeerror
    typeerror = get_formal_name({''})
    assert typeerror != sci_name





