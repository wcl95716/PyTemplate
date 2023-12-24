


from enum import Enum
from pydantic import BaseModel
from models.priority.type import Priority
from models.record.type import Record
from models.status.type import Status
from models.ticket.type import Ticket


class NotificationEnum(Enum):
    WECHAT = 1
    WEBSITE = 2
    EMAIL = 3
    

class NotificationTask(Record, Status, Priority, BaseModel):
    notification_type: int
    
    pass
    