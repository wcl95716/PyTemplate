import time

from sqlmodel import SQLModel, Field
from models.common.id.type import ID

from models.common.record.type import Record 


class ChatRecordBase(ID, Record, SQLModel):
    class config:
        use_enum_values = True
    pass


class ChatRecord( ChatRecordBase, table = True,extend_existing=True):
    pass
