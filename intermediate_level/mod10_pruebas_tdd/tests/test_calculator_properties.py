from hypothesis import given
from hypothesis import strategies as st

from mod10_pruebas_tdd.calculator import calculate_total


@given(st.lists(st.floats(allow_nan=False, allow_infinity=False)))
def test_calculate_total_property(prices):
    assert calculate_total(prices) == sum(prices)
