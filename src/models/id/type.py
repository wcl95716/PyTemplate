
# id 类  
# 属性为id
# 确保继承属性的类有一个唯一id

from typing import Optional
from pydantic import BaseModel



class ID(BaseModel):
    id: Optional[int]
    pass