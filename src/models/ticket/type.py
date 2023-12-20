
from datetime import datetime
import sys

from pydantic import BaseModel
sys.path.append("./src")
import time
from typing import Any, Optional

from base_class.user.type import User

from base_class.id.type import ID
from base_class.priority.type import Priority
from base_class.status.type import Status
from base_class.update_time.type import UpdateTime

class Ticket(BaseModel):
    id:Optional[int]
    status:int
    priority:int
    type:int
    title:str 
    content:str 
    assigned_to_id:str
    creator_id:str
    create_time:datetime
    update_time:Optional[datetime]
    pass