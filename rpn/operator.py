from enum import Enum
from typing import List
import operator

class OperatorRPN(Enum):
    PLUS = operator.add
    MINUS = operator.sub
    MULTIPLY = operator.mul
    DIVIDE = operator.truediv


    @classmethod
    def get_keys_lower(cls) -> List[str]:
        return [operator.name.lower() for operator in (cls)]
    
    @classmethod
    def get(cls, operator_str: str):
        if operator_str not in cls.get_keys_lower():
            raise OperatorNotExist
        
        for operator in (cls):
            if operator.name.lower() == operator_str:
                return operator


class OperatorNotExist(Exception):
    pass