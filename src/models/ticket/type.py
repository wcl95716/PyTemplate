from datetime import datetime
import sys

from pydantic import BaseModel
from models.priority.type import Priority
from models.record.type import Record

from models.status.type import Status
sys.path.append("./src")
import time
from typing import Any, Optional


class Ticket(Record,Status,Priority,BaseModel):

    pass

