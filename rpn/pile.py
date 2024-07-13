from typing import Optional, List
from .utils import is_int, is_float

class Pile:
    def __init__(self) -> None:
        self._pile = []

    def is_empty(self) -> bool:
        return self._pile == []
    
    def add(self, value: str) -> None:
        self._pile.append(value)

    def get(self) -> Optional[str]:
        if self._pile:
            return self._pile.pop()
        
        return None
    
    def clean(self) -> None:
        self._pile = []
    
class PileRPN(Pile):
    def __init__(self) -> None:
        super().__init__()
    
    def add(self, value: str | int) -> None:
        if is_int(value) or is_float(value):
            self._pile.append(value)
        else:
            raise InvalidValuePileRPN
        
    def to_list(self) -> List[str]:
        return self._pile

class InvalidValuePileRPN(Exception):
    pass