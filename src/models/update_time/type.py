from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class UpdateTime(BaseModel):
    create_time: datetime
    update_time: Optional[datetime]
