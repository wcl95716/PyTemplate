# id 类
# 属性为id
# 确保继承属性的类有一个唯一id

from typing import Any, Optional
import uuid
from sqlmodel import SQLModel, Field 


class ID(SQLModel):
    id: Optional[int] =  Field(None, description="数据库自动生成的ID",primary_key=True)
    uu_id: Optional[str] = Field(None, description="uuid 类初始化自动生成" , index=True)
    
    def __init__(self, **data: Any):
        # Set uu_id from data if present, otherwise generate a new UUID
        if data.get('uu_id') is None:
            # print("uu_id is None ",data)
            data['uu_id'] = str(uuid.uuid4())
        super().__init__(**data)
    
    def build_sql_query(self) -> tuple[str,list[Any]]:
        
        sql = ""
        args = []
        
        
        if self.id is not None :
            sql += " AND id = %s"
            args.append(str(self.id))
        
        if self.uu_id is not None:
            sql += " AND uu_id = %s"
            args.append(self.uu_id)
            
        return sql , args
        
    pass
