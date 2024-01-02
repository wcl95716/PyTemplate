import time

from sqlmodel import SQLModel, Field 

from models.record.type import Record


class ChatRecord(Record, SQLModel, table = True):
    pass
