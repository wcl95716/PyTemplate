from enum import Enum
from typing import Literal
from pydantic import BaseModel


class StatusEnum(Enum):
    NEW = 0
    IN_PROGRESS = 1
    COMPLETED = 2
    CLOSED = 3


class Status(BaseModel):
    status: StatusEnum
    class Config:
        use_enum_values = True  # 配置 Pydantic 使用枚举的值