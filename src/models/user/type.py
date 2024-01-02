from typing import Optional
# from pydantic import BaseModel, Field
from sqlmodel import SQLModel, Field 
from models.company.type import Company

from models.id.type import ID
from models.priority.type import Priority
from models.status.type import Status


# ID, Priority, Status ,Company , 
class User(ID, Priority, Status ,Company , SQLModel,table=True):
    name: str = Field(..., description="姓名 必须",index=True)
    phone: str =  Field(None, description="手机号 必须" , index=True)
    email: Optional[str] = Field(None, description="email 可以为空",index=True)
    avatar: Optional[str] = Field(None, description="头像 可以为空")
    displayPassword: Optional[str] = Field("12345678", description="密码 初始密码为12345678")
    password:  Optional[str] = Field(None, description="数据库进行的加密 密码")
    class Config:
        use_enum_values = True  # 配置 Pydantic 使用枚举的值
    pass


