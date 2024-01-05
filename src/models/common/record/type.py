import sys
sys.path.append("./src")
from typing import Any, Optional
from models.common.company_info.type import CompanyInfo, CompanyInfoFilter
from models.common.priority.type import Priority, PriorityFilter

from models.common.status.type import Status, StatusFilter


from sqlalchemy import Integer
from models.common.id.type import ID

from models.common.update_time.type import UpdateTime, UpdateTimeFilter


from enum import Enum
from sqlmodel import SQLModel, Field 
from pydantic import BaseModel, Field as PydanticField
from enum import Enum

class RecordEnum(Enum):
    """
    RecordEnum 用于表示不同类型的记录。
    
    - TEXT: 1 代表文本记录。
    - IMAGE: 2 代表图像记录。
    - VIDEO: 3 代表视频记录。
    - AUDIO: 4 代表音频记录。
    - FILE: 5 代表文件记录。
    """
    TEXT = 1
    IMAGE = 2
    VIDEO = 3
    AUDIO = 4
    FILE = 5
    pass


class RecordFilterEnum(str,Enum):
    """
    RecordEnum 用于表示不同类型的记录。
    
    - TEXT: 1 代表文本记录。
    - IMAGE: 2 代表图像记录。
    - VIDEO: 3 代表视频记录。
    - AUDIO: 4 代表音频记录。
    - FILE: 5 代表文件记录。
    """
    TEXT = 1
    IMAGE = 2
    VIDEO = 3
    AUDIO = 4
    FILE = 5
    pass 



class Record(UpdateTime,CompanyInfo, Status, Priority ,SQLModel):
    record_type: RecordEnum = Field(RecordEnum.TEXT,index=True,sa_type=Integer)
    content: str 
    title: str
    creator_id: str = Field(..., description="创建者ID",index=True)
    assigned_to_id: Optional[str] = Field(..., description="被指派者ID",index=True)
    
    class config:
        use_enum_values = True  # 配置 Pydantic 使用枚举的值

    pass



class RecordFilter(UpdateTimeFilter,CompanyInfoFilter, StatusFilter, PriorityFilter ,SQLModel):
    record_type: Optional[RecordFilterEnum] = PydanticField(None, description=RecordFilterEnum.__doc__,examples=[{"TEXT":1,"IMAGE":2,"VIDEO":3,"AUDIO":4,"FILE":5}] )
    content: Optional[str] = Field(None, description="记录内容")
    title: Optional[str] = Field(None, description="记录标题")
    creator_id: Optional[str] = Field( None, description="创建者ID",index=True)
    assigned_to_id: Optional[str] = Field( None, description="被指派者ID",index=True)
    
    class config:
        use_enum_values = True  # 配置 Pydantic 使用枚举的值

    pass

    def build_sql_query(self) -> tuple[str,list[Any]]:
        
        sql_fragments = []
        args = []

        # 添加来自其他过滤器的 SQL 片段和参数
        for filter_cls in [UpdateTimeFilter, CompanyInfoFilter]:
            sql_fragment, filter_args = filter_cls.build_sql_query(self)
            sql_fragments.append(sql_fragment)
            args.extend(filter_args)
        
        # 使用字典映射字段到 SQL 片段
        field_to_sql = {
            "assigned_to_id": "assigned_to_id = %s",
            "creator_id": "creator_id = %s",
            "title": "title LIKE %s",
            "record_type": "type = %s",
            "content": "content LIKE %s"
        }

        # 生成 SQL 片段和参数
        for field, sql in field_to_sql.items():
            value = getattr(self, field)
            if value is not None:
                sql_fragments.append(" AND " + sql)
                args.append(str(value.value) if hasattr(value, "value") else value)

        # 组合所有 SQL 片段
        full_sql = " ".join(sql_fragments)

        return full_sql, args
