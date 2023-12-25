# id 类
# 属性为id
# 确保继承属性的类有一个唯一id

from typing import Any, Optional
import uuid
from pydantic import BaseModel


class ID(BaseModel):
    id: Optional[int] = None
    uu_id: str
    
    def __init__(self, **data: Any):
        # Set uu_id from data if present, otherwise generate a new UUID
        data['uu_id'] = str(uuid.uuid4())
        super().__init__(**data)
    pass
