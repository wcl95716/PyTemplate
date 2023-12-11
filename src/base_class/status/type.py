from enum import Enum

class Status:
    NEW = 0
    IN_PROGRESS = 1
    COMPLETED = 2
    CLOSED = 3
    def __init__(self, status: int):
        self._status = status

    def get_status(self):
        return self._status
    
    
