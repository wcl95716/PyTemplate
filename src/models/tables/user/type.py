from typing import Optional
# from pydantic import BaseModel, Field
from sqlmodel import SQLModel, Field 
from models.common.company_info.type import CompanyInfo, CompanyInfoFilter

from models.common.id.type import ID
from models.common.priority.type import Priority
from models.common.status.type import Status


# ID, Priority, Status ,CompanyInfo , 
class UserBase(ID, Priority, Status ,CompanyInfo , SQLModel):
    name: str = Field(..., description="姓名 必须",index=True)
    phone: str =  Field(None, description="手机号 必须" , index=True)
    email: Optional[str] = Field(None, description="email 可以为空",index=True)
    avatar: Optional[str] = Field(None, description="头像 可以为空")
    displayPassword: Optional[str] = Field("12345678", description="密码 初始密码为12345678")
    password:  Optional[str] = Field(None, description="数据库进行的加密 密码")
    class config:
        use_enum_values = True  # 配置 Pydantic 使用枚举的值
    pass


class User(UserBase,table=True,extend_existing=True):
    name: str = Field(..., description="姓名 必须",index=True)
    phone: str =  Field(None, description="手机号 必须" , index=True)
    email: Optional[str] = Field(None, description="email 可以为空",index=True)
    avatar: Optional[str] = Field(None, description="头像 可以为空")
    displayPassword: Optional[str] = Field("12345678", description="密码 初始密码为12345678")
    password:  Optional[str] = Field(None, description="数据库进行的加密 密码")
    class config:
        use_enum_values = True  # 配置 Pydantic 使用枚举的值
    pass



# 创建一个用于过滤的模型
# 包含一些可选的参数
class UserFilterParams(ID,CompanyInfoFilter,SQLModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    
    class config:
        use_enum_values = True  # 配置 Pydantic 使用枚举的值
    pass



