


from enum import Enum
from typing import Optional, Union
from sqlalchemy import JSON
from sqlmodel import SQLModel, Field 
from models.company.type import CompanyEnum
from models.id.type import ID
from models.priority.type import Priority
from models.record.type import Record
from models.status.type import Status

import json  # Add missing import statement

class NotificationEnum(Enum):
    WECHAT = 1
    WEBSITE = 2
    EMAIL = 3
    

from typing import Any  # Add missing import statement

class NotificationTask(Record, ID, Status, Priority, SQLModel, table = True):
    notification_type: NotificationEnum
    destination: Optional[str] = None  # Fix missing type parameters for dict
    company_id: CompanyEnum
    # id: Optional[int]  # Updated type annotation
    class Config:
        use_enum_values = True  # 配置 Pydantic 使用枚举的值
    
    def to_db_dict(self) -> dict[str,str]:  # Add return type annotation
        # 将模型转换为适合数据库插入的字典
        db_dict = self.model_dump()
        if db_dict['destination'] is not None:
            db_dict['destination'] = json.dumps(db_dict['destination'])  # Fix reference to json.dumps
        return db_dict
    pass
    