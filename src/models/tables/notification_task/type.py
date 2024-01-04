


from datetime import datetime
from enum import Enum
from typing import Optional, Union
from sqlalchemy import JSON, Integer
from sqlmodel import SQLModel, Field 
from pydantic import BaseModel, Field as PydanticField

import json
from models.common.priority.type import Priority

from models.common.record.type import Record, RecordFilter
from enum import Enum
from models.common.status.type import Status  # Add missing import statement
from models.common.id.type import ID  # Add missing import statement

class NotificationEnum(Enum):
    WECHAT = 1
    WEBSITE = 2
    EMAIL = 3
    

from typing import Any  # Add missing import statement

class NotificationTaskBase( ID , Record, SQLModel):
    notification_type: NotificationEnum = Field(NotificationEnum.WECHAT, description="通知类型" ,index=True ,sa_type=Integer)
    destination: Optional[str] = None  # Fix missing type parameters for dict
    # id: Optional[int]  # Updated type annotation
    class config:
        use_enum_values = True  # 配置 Pydantic 使用枚举的值
    
    def to_db_dict(self) -> dict[str,str]:  # Add return type annotation
        # 将模型转换为适合数据库插入的字典
        db_dict = self.model_dump()
        if db_dict['destination'] is not None:
            db_dict['destination'] = json.dumps(db_dict['destination'])  # Fix reference to json.dumps
        return db_dict
    pass

class NotificationTask( NotificationTaskBase, table = True):
    class config:
        use_enum_values = True  # 配置 Pydantic 使用枚举的值
    
    def to_db_dict(self) -> dict[str,str]:  # Add return type annotation
        # 将模型转换为适合数据库插入的字典
        db_dict = self.model_dump()
        if db_dict['destination'] is not None:
            db_dict['destination'] = json.dumps(db_dict['destination'])  # Fix reference to json.dumps
        return db_dict
    pass
    
# 添加过滤模型

class NotificationFilterEnum(str,Enum):
    NoneValue = None
    WECHAT = 1
    WEBSITE = 2
    EMAIL =3

    
    
# class NotificationTaskFilterParams(ID,RecordFilter,BaseModel):
#     start_date: Optional[str] = None  # Updated type annotation
#     end_date: Optional[str] = None  # Updated type annotation
    
#     # 描述
#     notification_type: Optional[NotificationFilterEnum] = PydanticField(None, description="通知类型",examples=[{"name":"WECHAT","value":1},{"name":"WEBSITE","value":2},{"name":"EMAIL","value":3}] )
    
#     class config:
#         use_enum_values = True  # 配置 Pydantic 使用枚举的值
#     pass


class NotificationTaskFilterParams(ID,RecordFilter,BaseModel):
    start_date: Optional[str] = None  # Updated type annotation
    end_date: Optional[str] = None  # Updated type annotation
    
    # 描述
    notification_type:NotificationFilterEnum = Field(default=NotificationFilterEnum.NoneValue,description="通知类型" )
    
    class config:
        use_enum_values = True  # 配置 Pydantic 使用枚举的值
    pass

    def build_sql_query(self) -> tuple[str,list[Any]]:
        sql1 ,args1 = RecordFilter.build_sql_query(self)
        
        sql = ""
        args = []
        
        args.extend(args1)
        sql += sql1
        
        if self.notification_type is not None and self.notification_type != NotificationFilterEnum.NoneValue :
            sql += " AND notification_type = %s"
            args.append(str(self.notification_type.value))
        
        if self.start_date and self.end_date:
            sql += " AND create_time BETWEEN %s AND %s"
            args.append(str(self.start_date))
            args.append(str(self.end_date))
            
        return sql , args
        