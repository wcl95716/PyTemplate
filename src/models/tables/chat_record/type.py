import time

from sqlmodel import SQLModel, Field
from models.common.id.type import ID

from models.common.record.type import Record 


class ChatRecordBase(ID, Record, SQLModel):
    """_summary_
    用于存储聊天记录结构
    Args:
        ID (_type_): _description_
        Record (_type_): _description_
        SQLModel (_type_): _description_
        
    """
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
    """_summary_
        用于存储聊天记录结构
        
    Args:
    
        
    """
    pass
