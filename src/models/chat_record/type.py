import time

from pydantic import BaseModel

from models.record.type import Record


class ChatRecord(Record, BaseModel):
    pass
