from rpn.pile import PileRPN

class Stacks:
    def __init__(self) -> None:
        self._stacks = {}

    def add(self, stacks_id: str) -> None:
        if stacks_id in self._stacks.keys():
            raise StacksAlreadyExist
        
        self._stacks[stacks_id] = PileRPN()

    def get(self, stacks_id: str) -> list:
        if stacks_id not in self._stacks.keys():
            raise StacksNotExist
        
        return self._stacks.get(stacks_id)
    
    def delete(self, stacks_id: str) -> None:
        if stacks_id not in self._stacks.keys():
            raise StacksNotExist
        
        del self._stacks[stacks_id]


class StacksAlreadyExist(Exception):
    pass

class StacksNotExist(Exception):
    pass