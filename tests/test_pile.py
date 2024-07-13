import pytest
from rpn.pile import PileRPN, InvalidValuePileRPN


class TestPileRPN:

    @pytest.fixture(scope="class")
    def pile_rpn(self) -> PileRPN:
        return PileRPN()
    
    def test_is_empty(self, pile_rpn: PileRPN) -> None:
        assert pile_rpn.is_empty() == True
        pile_rpn.add('1')
        assert pile_rpn.is_empty() == False

    def test_add(self, pile_rpn: PileRPN) -> None:
        with pytest.raises(InvalidValuePileRPN):
            pile_rpn.add('v')
        
        pile_rpn.add('1')
        pile_rpn.add(3)
        pile_rpn.add(3,6)

    def test_get(self, pile_rpn: PileRPN) -> None:
        pile_rpn._pile = []
        assert pile_rpn.get() is None
        pile_rpn.add('1')
        assert pile_rpn.get() == '1'

    def test_clean(self, pile_rpn: PileRPN) -> None:
        pile_rpn._pile = ['2', '5', 6, 5]

        pile_rpn.clean()

        assert pile_rpn._pile == []
