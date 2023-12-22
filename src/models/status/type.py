from enum import Enum
from typing import Literal
from pydantic import BaseModel


class StatusEnum(Enum):
    NEW = 0
    IN_PROGRESS = 1
    COMPLETED = 2
    CLOSED = 3


class Status(BaseModel):
    status: int
