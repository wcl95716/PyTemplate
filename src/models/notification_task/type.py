


from enum import Enum
from typing import Optional
from pydantic import BaseModel
from models.id.type import ID
from models.priority.type import Priority
from models.record.type import Record
from models.status.type import Status
from models.ticket.type import Ticket


class NotificationEnum(Enum):
    WECHAT = 1
    WEBSITE = 2
    EMAIL = 3
    

class NotificationTask(Record, ID, Status, Priority, BaseModel):
    notification_type: int
    destination: dict[str, str]
    # id: Optional[int]  # Updated type annotation
    pass
    