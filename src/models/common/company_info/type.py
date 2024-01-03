# id 类
# 属性为id
# 确保继承属性的类有一个唯一id
from sqlalchemy import Integer
from sqlmodel import SQLModel, Field 
from enum import Enum
from typing import Optional
from pydantic import BaseModel



# 创建公司枚举类
class CompanyEnum(Enum):
    NONE = 1
    TIAN_YI = 2
    pass

class CompanyInfo(SQLModel,extend_existing=True):
    company_id: Optional[CompanyEnum] = Field(CompanyEnum.NONE, description="公司id", index=True,sa_type=Integer)
    company_name: Optional[str] = Field(None, description="公司名称", index=True)
    
    class config:
        use_enum_values = True  # 配置 Pydantic 使用枚举的值
    pass

