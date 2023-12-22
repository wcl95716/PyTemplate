import datetime
import sys
import time

from pydantic import BaseModel

from models.record.type import Record
sys.path.append("./src")


class ChatRecord(Record,BaseModel):
    pass
    
    


