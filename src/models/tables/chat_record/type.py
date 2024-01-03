import time

from sqlmodel import SQLModel, Field
from models.common.id.type import ID

from models.common.record.type import Record 


class ChatRecord(ID, Record, SQLModel, table = True,extend_existing=True):
    pass
