from datetime import datetime
from typing import Any, Optional

from pydantic import BaseModel


class UpdateTime(BaseModel):
    create_time: Optional[datetime] = None
    update_time: Optional[datetime] = None

    def __init__(self, **data: Any):
        super().__init__(**data)
        if self.create_time is None:
            self.create_time = datetime.now()
        if self.update_time is None:
            self.update_time = datetime.now()


