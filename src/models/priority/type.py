from enum import Enum
import random
from sqlmodel import SQLModel, Field 


class PriorityEnum(Enum):
    HIGHEST = 0
    URGENT = 1
    NORMAL = 2
    NOT_URGENT = 3
    NOT_NEEDED = 4


class Priority(SQLModel):
    priority: PriorityEnum = Field(PriorityEnum.NORMAL, description="优先级" ,index=True )

    class Config:
        use_enum_values = True  # 配置 Pydantic 使用枚举的值
        
