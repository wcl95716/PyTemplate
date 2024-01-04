from enum import Enum
import random
from typing import Optional
from sqlalchemy import Integer
from sqlmodel import SQLModel, Field 


class PriorityEnum(Enum):
    """_summary_

    Args:
        Enum (_type_): _description_
        
        - HIGHEST: 0 代表最高优先级。
        - URGENT: 1 代表紧急优先级。
        - NORMAL: 2 代表正常优先级。
        - NOT_URGENT: 3 代表不紧急优先级。
        - NOT_NEEDED: 4 代表不需要优先级。
    """
    HIGHEST = 0
    URGENT = 1
    NORMAL = 2
    NOT_URGENT = 3
    NOT_NEEDED = 4
    

class PriorityFilterEnum(str,Enum):
    """_summary_

    Args:
        Enum (_type_): _description_
        
        - HIGHEST: 0 代表最高优先级。
        - URGENT: 1 代表紧急优先级。
        - NORMAL: 2 代表正常优先级。
        - NOT_URGENT: 3 代表不紧急优先级。
        - NOT_NEEDED: 4 代表不需要优先级。
    """
    HIGHEST = 0
    URGENT = 1
    NORMAL = 2
    NOT_URGENT = 3
    NOT_NEEDED = 4


class Priority(SQLModel,extend_existing=True):
    priority: PriorityEnum = Field(PriorityEnum.NORMAL ,index=True,sa_type=Integer )

    class config:
        use_enum_values = True  # 配置 Pydantic 使用枚举的值
        


    
class PriorityFilter(SQLModel):
    priority: Optional[PriorityFilterEnum]= Field(None ,index=True,sa_type=Integer)

    class config:
        use_enum_values = True  # 配置 Pydantic 使用枚举的值
        