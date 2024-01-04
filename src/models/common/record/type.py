import sys
from typing import Optional
from models.common.company_info.type import CompanyInfo
from models.common.priority.type import Priority

from models.common.status.type import Status
sys.path.append("./src")

from sqlalchemy import Integer
from models.common.id.type import ID

from models.common.update_time.type import UpdateTime


from enum import Enum
from sqlmodel import SQLModel, Field 
from enum import Enum


class RecordEnum(str,Enum):
    TEXT = 1
    IMAGE = 2
    VIDEO = 3
    AUDIO = 4
    FILE = 5
    pass


class Record(UpdateTime,CompanyInfo, Status, Priority ,SQLModel):
    type: RecordEnum = Field(RecordEnum.TEXT, description="记录类型" ,index=True,sa_type=Integer)
    content: str 
    title: str
    creator_id: str = Field(..., description="创建者ID",index=True)
    assigned_to_id: str = Field(..., description="被指派者ID",index=True)
    
    class config:
        use_enum_values = True  # 配置 Pydantic 使用枚举的值

    pass


class RecordFilter(UpdateTime,CompanyInfo, Status, Priority ,SQLModel):
    type: Optional[RecordEnum] = Field(RecordEnum.TEXT, description="记录类型" ,index=True,sa_type=Integer)
    content: Optional[str] = Field(None, description="记录内容")
    title: Optional[str] = Field(None, description="记录标题")
    creator_id: Optional[str] = Field( None, description="创建者ID",index=True)
    assigned_to_id: Optional[str] = Field( None, description="被指派者ID",index=True)
    
    class config:
        use_enum_values = True  # 配置 Pydantic 使用枚举的值

    pass
