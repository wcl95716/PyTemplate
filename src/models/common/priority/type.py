from enum import Enum
import random
from sqlalchemy import Integer
from sqlmodel import SQLModel, Field 


class PriorityEnum(str,Enum):
    HIGHEST = 0
    URGENT = 1
    NORMAL = 2
    NOT_URGENT = 3
    NOT_NEEDED = 4


class Priority(SQLModel,extend_existing=True):
    priority: PriorityEnum = Field(PriorityEnum.NORMAL, description="优先级" ,index=True,sa_type=Integer )

    class config:
        use_enum_values = True  # 配置 Pydantic 使用枚举的值
        
