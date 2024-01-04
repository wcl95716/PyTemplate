


from enum import Enum
from typing import Optional, Union
from sqlalchemy import JSON, Integer
from sqlmodel import SQLModel, Field 

import json
from models.common.priority.type import Priority

from models.common.record.type import Record
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
    
    