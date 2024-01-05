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



class RecordFilter(UpdateTimeFilter,CompanyInfoFilter, StatusFilter, PriorityFilter ,BaseModel):
    record_type: Optional[RecordFilterEnum] = PydanticField(None, description=RecordFilterEnum.__doc__,examples=[{"TEXT":1,"IMAGE":2,"VIDEO":3,"AUDIO":4,"FILE":5}] )
    content: Optional[str] = Field(None, description="记录内容")
    title: Optional[str] = Field(None, description="记录标题")
    creator_id: Optional[str] = Field( None, description="创建者ID",index=True)
    assigned_to_id: Optional[str] = Field( None, description="被指派者ID",index=True)
    
    class config:
        use_enum_values = True  # 配置 Pydantic 使用枚举的值

    pass

    def build_sql_query(self) -> tuple[str,list[Any]]:
        
        sql1 ,args1 = CompanyInfoFilter.build_sql_query(self)
        
        sql = ""
        sql += sql1
        
        args = []
        args.extend(args1)
        if self.assigned_to_id is not None:
            sql += " AND assigned_to_id = %s"
            args.append(self.assigned_to_id)
        
        if self.creator_id is not None:
            sql += " AND creator_id = %s"
            args.append(self.creator_id)
        
            
        if self.priority is not None:
            sql += " AND priority = %s"
            args.append(str(self.priority.value))

        if self.status is not None:
            sql += " AND status = %s"
            args.append(str(self.status.value))
            
        
        # 模糊搜索
        if self.title is not None:
            sql += " AND title LIKE %s"
            args.append(self.title)
        
        if self.record_type is not None:
            sql += " AND type = %s"
            args.append(str(self.record_type.value))
            
        if self.content is not None:
            sql += " AND content LIKE %s"
            args.append(self.content)
        
        
        return sql , args
        
