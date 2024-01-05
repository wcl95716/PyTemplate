import sys

from models.common.filter_params.type import FilterParams
sys.path.append("./src")

from enum import Enum
from typing import Any, Literal, Optional
from sqlmodel import SQLModel, Field 
from sqlalchemy import Column, Integer

class StatusEnum(Enum):
    """_summary_

    Args:
        Enum (_type_): _description_
        
        - NEW: 0 代表新建状态。
        - IN_PROGRESS: 1 代表进行中状态。
        - COMPLETED: 2 代表已完成状态。
        - CLOSED: 3 代表已关闭状态。
    """
    NoneValue = None
    NEW = 0
    IN_PROGRESS = 1
    COMPLETED = 2
    CLOSED = 3
    

class StatusFilterEnum(str,Enum):
    """_summary_

    Args:
        str (_type_): _description_
        Enum (_type_): _description_
        
        - NEW: 0 代表新建状态。
        - IN_PROGRESS: 1 代表进行中状态。
        - COMPLETED: 2 代表已完成状态。
        - CLOSED: 3 代表已关闭状态。
    """
    NoneValue = None
    NEW = 0
    IN_PROGRESS = 1
    COMPLETED = 2
    CLOSED = 3


class Status(SQLModel):
    # 使它生成的表中 为int类型
    status: StatusEnum = Field(StatusEnum.NEW,index=True,sa_type=Integer)
    
    class config:
        use_enum_values = True  # 配置 Pydantic 使用枚举的值



class StatusFilter(FilterParams,SQLModel):
    # 使它生成的表中 为int类型
    status: Optional[StatusFilterEnum] = Field(None,index=True,sa_type=Integer)
    
    class config:
        use_enum_values = True  # 配置 Pydantic 使用枚举的值
        
    def build_sql_query(self)-> tuple[str,list[Any]]:
        sql = ""
        args = []
        if self.status is not None and self.status != StatusFilterEnum.NoneValue:
            sql += " AND status = %s"
            args.append(str(self.status.value))
            
        return sql, args
        pass
    