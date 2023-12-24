import sys
sys.path.append("./src")
from enum import Enum
from pydantic import BaseModel
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


class Record(ID, UpdateTime, BaseModel):
    type: RecordEnum
    content: str
    title: str
    creator_id: str
    assigned_to_id: str
    
    class Config:
        use_enum_values = True  # 配置 Pydantic 使用枚举的值

    pass
