# id 类
# 属性为id
# 确保继承属性的类有一个唯一id
from sqlalchemy import Integer
from sqlmodel import SQLModel, Field 
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field as PydanticField



# 创建公司枚举类
class CompanyEnum(Enum):
    """_summary_

    Args:
        Enum (_type_): _description_
        
        - NONE: 0 代表无公司。
        - TIAN_YI: 1 代表天翼。
    """
    NONE = 0
    TIAN_YI = 1
    pass


class CompanyInfoFilterEnum(str,Enum):
    """_summary_

    Args:
        str (_type_): _description_
        Enum (_type_): _description_
        
        - NONE: 0 代表无公司。
        - TIAN_YI: 1 代表天翼。
    """
    
    NONE = 0
    TIAN_YI = 1
    pass



class CompanyInfo(SQLModel,extend_existing=True):
    company_id: CompanyEnum = Field(CompanyEnum.NONE,index=True,sa_type=Integer)
    company_name: Optional[str] = Field(None, description="公司名称", index=True)
    
    class config:
        use_enum_values = True  # 配置 Pydantic 使用枚举的值
    pass



class CompanyInfoFilter(SQLModel):
    company_id: Optional[CompanyInfoFilterEnum ]= Field(None)
    company_name: Optional[str] = Field(None, description="公司名称", index=True)
    
    class config:
        use_enum_values = True  # 配置 Pydantic 使用枚举的值
    pass
