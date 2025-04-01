import pytest
from src import calculator

def test_add():
    assert calculator.add(1, 2) == 3
    assert calculator.add(0, 5) == 5
    assert calculator.add(-2, 9) == 7
    assert calculator.add(5, -8) == -3

def test_addwrong():
    assert calculator.add_wrong(1, 2) == 3
    assert calculator.add_wrong(0, 5) == 3
    assert calculator.add_wrong(-2, 9) == 7
    assert calculator.add_wrong(0, 0) == 0

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (0, 5, 5),
        (-2, 9, 7),
        (5, -8, -3),
    ],
)
def test_add_parametrized(a, b, expected):
    assert calculator.add(a, b) == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 4, 6),
        (0, 5, -5),
        (-2, -9, 7),
        (5, -8, 13),
    ],
)
def test_subtract(a, b, expected):
    assert calculator.subtract(a, b) == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (6, 7, 42),
        (0, 5, 0),
        (-2, 9, -18),
        (5, -8, -40),
    ],
)
def test_multiply(a, b, expected):
    assert calculator.multiply(a, b) == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (6, 7, 42),
        (0, 5, 1),
        (-2, 9, -17),
        (5, -8, -39),
    ],
)
def test_multiplywrong(a, b, expected):
    assert calculator.multiply_wrong(a, b) == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (9, 3, 3),
        (10, 2, 5),
        (-8, 4, -2),
        (15, -3, -5),
    ],
)
def test_divide(a, b, expected):
    assert calculator.divide(a, b) == expected

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        calculator.divide(10, 0)

        #gigggzggkuasdsasadasdadsasdaasdsadsadasd
        