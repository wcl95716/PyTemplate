from datetime import datetime


from sqlmodel import SQLModel, Field 


import time
from typing import Any, Optional

from models.common.id.type import ID
from models.common.priority.type import Priority
from models.common.record.type import Record
from models.common.status.type import Status


class Ticket(ID ,Record, Status, Priority, SQLModel, table = True,extend_existing=True   ):
    
    class Config:
        use_enum_values = True  # 配置 Pydantic 使用枚举的值
    pass
