from rpn.pile import PileRPN
from rpn.operator import OperatorRPN

class CalculatorRPN:
    def apply(self, pile: PileRPN, operator: OperatorRPN) -> PileRPN:
        if pile.is_empty() or len(pile.to_list()) < 2:
            raise InvalidPileNumberItems
        
        element2 = int(pile.get())
        element1 = int(pile.get())
        
        pile.add(operator.value[1](element2, element1))

        return pile

class InvalidPileNumberItems(Exception):
    pass
