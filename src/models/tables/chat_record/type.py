import time

from sqlmodel import SQLModel, Field
from models.common.id.type import ID

from models.common.record.type import Record 


class ChatRecordBase(ID, Record, SQLModel):
    class config:
        use_enum_values = True
        # 创建Schema用例
        
        schema_extra = {
            "example": {
                    "priority": 2,
                    "status": 0,
                    "type": 1,
                    "content": "string",
                    "title": "string",
                    "creator_id": "string",
                    "assigned_to_id": "string",
                },
            "example2": {
                    "priority": 2,
                    "status": 0,
                    "type": 1,
                    "content": "string",
                    "title": "string",
                    "creator_id": "string",
                    "assigned_to_id": "string",
                }
        }
        
    pass


class ChatRecord( ChatRecordBase, table = True,extend_existing=True):
    pass
