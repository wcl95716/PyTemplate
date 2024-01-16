


from datetime import datetime
from enum import Enum
from typing import Optional, Union
from sqlalchemy import JSON, Integer
from sqlmodel import SQLModel, Field 
from pydantic import BaseModel, Field as PydanticField

import json
from models.common.filter_params.type import FilterParams
from models.common.priority.type import Priority

from models.common.record.type import Record, RecordFilter
from enum import Enum
from models.common.status.type import Status  # Add missing import statement
from models.common.id.type import ID, IDFilter  # Add missing import statement
from typing import Any  # Add missing import statement

class NotificationEnum(Enum):
    """
    NotificationEnum 定义了不同类型的通知方式。

    枚举值:
    - NoneValue: 表示没有指定通知方式。
    - WECHAT: 表示通过微信进行通知。
    - WEBSITE: 表示通过网站进行通知。
    - EMAIL: 表示通过电子邮件进行通知。
    """
    NoneValue = None
    WECHAT = 1
    WEBSITE = 2
    EMAIL = 3
    
    
# 添加过滤模型
class NotificationFilterEnum(str,Enum):
    """
    NotificationEnum 定义了不同类型的通知方式。

    枚举值:
    - NoneValue: 表示没有指定通知方式。
    - WECHAT: 表示通过微信进行通知。
    - WEBSITE: 表示通过网站进行通知。
    - EMAIL: 表示通过电子邮件进行通知。
    """
    NoneValue = None
    WECHAT = 1
    WEBSITE = 2
    EMAIL =3


class NotificationTaskBase( ID , Record, SQLModel):
    notification_type: NotificationEnum = Field(NotificationEnum.WECHAT ,index=True ,sa_type=Integer)
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


class NotificationTaskFilterParams(IDFilter,RecordFilter,FilterParams,BaseModel):
    
    # 描述
    notification_type:NotificationFilterEnum = Field(default=NotificationFilterEnum.NoneValue,description="通知类型" )
    
    class config:
        use_enum_values = True  # 配置 Pydantic 使用枚举的值
    pass

    def build_sql_query(self) -> tuple[str,list[Any]]:
        sql_fragments = []
        args = []

        # 添加来自其他过滤器的 SQL 片段和参数
        for filter_cls in [RecordFilter, IDFilter]:
            sql_fragment, filter_args = filter_cls.build_sql_query(self) # type: ignore
            sql_fragments.append(sql_fragment)
            args.extend(filter_args)
            
        sql =  " ".join(sql_fragments)
        
        if self.notification_type is not None and self.notification_type != NotificationFilterEnum.NoneValue :
            sql += " AND notification_type = %s"
            args.append(str(self.notification_type.value))
            
        return sql , args
        