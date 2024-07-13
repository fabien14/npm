import pytest
from rpn.stacks import Stacks
from rpn.operator import OperatorRPN
from rpn.calculator import CalculatorRPN, InvalidPileNumberItems
from typing import List

class TestCalculatorRPN:

    @pytest.fixture(scope="class")
    def calculator(self) -> CalculatorRPN:
        return CalculatorRPN()
    
    def _calcul_apply(self, calculator: CalculatorRPN, operator: OperatorRPN, result_expected: List[float|int]) -> None:
        stacks = Stacks()
        stacks.add('test')
        stacks.get('test').add('2')
        
        with pytest.raises(InvalidPileNumberItems):
            calculator.apply(stacks.get('test'), operator)

        stacks.get('test').add('3')
        calculator.apply(stacks.get('test'), operator)
        
        assert stacks.get('test').to_list() == result_expected

        stacks.delete('test')
    
    def test_apply_plus(self, calculator: CalculatorRPN) -> None:
        self._calcul_apply(calculator, OperatorRPN.PLUS, [5])

    def test_apply_minus(self, calculator: CalculatorRPN) -> None:
        self._calcul_apply(calculator, OperatorRPN.MINUS, [1])

    def test_apply_divide(self, calculator: CalculatorRPN) -> None:
        self._calcul_apply(calculator, OperatorRPN.DIVIDE, [1.5])

    def test_apply_multiply(self, calculator: CalculatorRPN) -> None:
        self._calcul_apply(calculator, OperatorRPN.MULTIPLY, [6])