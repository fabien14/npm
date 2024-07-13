import pytest
from rpn.operator import OperatorRPN


class TestOperatorRPN:
    
    def test_get_keys_lower(self) -> None:

        operator_list = OperatorRPN.get_keys_lower()
        assert operator_list == ['plus', 'minus', 'multiply', 'divide']

    def test_get(self) -> None:

        operator_selected = OperatorRPN.get("multiply")
        assert operator_selected == OperatorRPN.MULTIPLY