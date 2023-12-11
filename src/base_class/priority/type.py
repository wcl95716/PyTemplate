from enum import Enum


class Priority:
    HIGHEST = 0
    URGENT = 1
    NORMAL = 2
    NOT_URGENT = 3
    NOT_NEEDED = 4
    
    def __init__(self, priority_type: int):
        self._priority_type = priority_type

    def get_priority(self) -> int:
        return self._priority_type
    
    
