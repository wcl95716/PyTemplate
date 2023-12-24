# id 类
# 属性为id
# 确保继承属性的类有一个唯一id

from enum import Enum
from typing import Optional
from pydantic import BaseModel

from models.id.type import ID


# 创建公司枚举类
class CompanyEnum(Enum):
    COMPANY = 1
    TIAN_YI = 2
    pass

class Company(ID,BaseModel):
    company_id: CompanyEnum
    company_name: Optional[str] = None
    
    class Config:
        use_enum_values = True  # 配置 Pydantic 使用枚举的值
    pass
