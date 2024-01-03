import sys
sys.path.append("./src")

from enum import Enum
from typing import Literal
from sqlmodel import SQLModel, Field 
from sqlalchemy import Column, Integer

class StatusEnum(Enum):
    NEW = 0
    IN_PROGRESS = 1
    COMPLETED = 2
    CLOSED = 3


class Status(SQLModel):
    # 使它生成的表中 为int类型
    status: StatusEnum = Field(StatusEnum.NEW, description="状态",index=True,sa_type=Integer)
    
    class config:
        use_enum_values = True  # 配置 Pydantic 使用枚举的值