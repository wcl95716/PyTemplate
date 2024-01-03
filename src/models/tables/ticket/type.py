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
        json_schema_extra = {
            "example": {
                # "id": 1,
                # "uu_id": "string",
                "type": 1,
                "content": "string",
                "title": "string",
                "creator_id": "string",
                "assigned_to_id": "string",
                "status": 1,
                "priority": 1,
                # "create_time": "2021-07-31T09:51:42.000Z",
                # "update_time": "2021-07-31T09:51:42.000Z",
            },
            "update":{
                    "priority": 2,
                    "status": 0,
                    "type": 1,
                    "content": "string",
                    "title": "string",
                    "creator_id": "4444",
                    "assigned_to_id": "string",
                    "id": 1,
            }
        }
    pass
