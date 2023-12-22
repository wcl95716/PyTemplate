import sys
import time

from pydantic import BaseModel
sys.path.append("./src")
from models.record.type import Record



class ChatRecord(Record,BaseModel):
    pass
    
    


