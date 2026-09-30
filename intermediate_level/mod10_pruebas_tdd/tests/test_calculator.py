import pytest

from mod10_pruebas_tdd.calculator import calculate_total


# tdd test
@pytest.fixture
def sample_prices():
    return [10, 20, 30]


def test_calculate_total(sample_prices):
    assert calculate_total(sample_prices) == 60


@pytest.mark.parametrize(
    "prices, expected",
    [
        ([5], 5),
        ([1.5, 2.5], 4),
        ([], 0),
    ],
)
def test_calculate_total_cases(prices, expected):
    assert calculate_total(prices) == expected
