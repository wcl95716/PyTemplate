import sys

from sqlalchemy import Integer

sys.path.append("./src")
from models.company.type import CompanyEnum, CompanyInfo
from enum import Enum
from sqlmodel import SQLModel, Field 
from models.id.type import ID
from models.update_time.type import UpdateTime
from enum import Enum


class RecordEnum(Enum):
    TEXT = 1
    IMAGE = 2
    VIDEO = 3
    AUDIO = 4
    FILE = 5
    pass


class Record(ID, UpdateTime, SQLModel,extend_existing=True):
    type: RecordEnum = Field(RecordEnum.TEXT, description="记录类型" ,index=True,sa_type=Integer)
    content: str 
    title: str
    creator_id: str = Field(..., description="创建者ID",index=True)
    assigned_to_id: str = Field(..., description="被指派者ID",index=True)
    company_id: CompanyEnum
    
    class Config:
        use_enum_values = True  # 配置 Pydantic 使用枚举的值

    pass
