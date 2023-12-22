from enum import Enum
import random
from pydantic import BaseModel


class PriorityEnum(Enum):
    HIGHEST = 0
    URGENT = 1
    NORMAL = 2
    NOT_URGENT = 3
    NOT_NEEDED = 4


class Priority(BaseModel):
    priority: int
