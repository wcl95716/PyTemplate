from datetime import datetime


from pydantic import BaseModel
from models.priority.type import Priority
from models.record.type import Record

from models.status.type import Status

import time
from typing import Any, Optional


class Ticket(Record, Status, Priority, BaseModel):
    
    class Config:
        use_enum_values = True  # 配置 Pydantic 使用枚举的值
    pass
