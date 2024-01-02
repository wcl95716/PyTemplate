from datetime import datetime
from typing import Any, Optional

from sqlmodel import SQLModel, Field 


class UpdateTime(SQLModel):
    create_time: Optional[datetime] = Field(datetime.now(), description="自动生成的ID")
    update_time: Optional[datetime] = Field(datetime.now(), description="日期")

    def __init__(self, **data: Any):
        super().__init__(**data)
        if self.create_time is None:
            self.create_time = datetime.now()
        if self.update_time is None:
            self.update_time = datetime.now()


