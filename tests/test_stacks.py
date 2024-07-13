import pytest
from rpn.pile import PileRPN
from rpn.stacks import Stacks, StacksAlreadyExist, StacksNotExist


class TestStacks:

    @pytest.fixture(scope="class")
    def stacks(self) -> Stacks:
        return Stacks()
    
    def test_add(self, stacks) -> None:
        stacks._stacks['test-id-stacks'] = PileRPN()
        with pytest.raises(StacksAlreadyExist):
            stacks.add('test-id-stacks')

        stacks.add('test-id-stacks-good')

    def test_get(self, stacks) -> None:
        stacks._stacks = {}
        pile_rpn_test = PileRPN()
        stacks._stacks['test-id-stacks'] = pile_rpn_test

        assert stacks.get('test-id-stacks') == pile_rpn_test

    def test_delete(self, stacks) -> None:
        with pytest.raises(StacksNotExist):
            stacks.delete('test-id-failed')
        
        stacks._stacks['test-id-stacks'] = PileRPN()
        stacks.delete('test-id-stacks')
