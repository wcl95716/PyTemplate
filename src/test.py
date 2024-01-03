from enum import Enum
import json
from pydantic import BaseModel
from sqlalchemy import Integer
from sqlmodel import Field, SQLModel

class StatusEnum(Enum):
    NEW = 0
    IN_PROGRESS = 1
    COMPLETED = 2
    CLOSED = 3

class MyEnum(Enum):
    FIRST = 1
    SECOND = 2
    
class StatusModel(SQLModel):
    enum_field: MyEnum = Field(MyEnum.FIRST, description="状态",index=True,sa_type=Integer)
    class config:
        use_enum_values = True 
        
# class StatusModel(SQLModel):
#     enum_field: MyEnum = Field(MyEnum.FIRST, description="状态",index=True,sa_type=Integer)
#     class config:
#         use_enum_values = True

class MyModel(SQLModel):
    enum_field: MyEnum = Field(MyEnum.FIRST, description="状态",index=True,sa_type=Integer)
    class config:
        use_enum_values = True

new_model = MyModel(**{'enum_field': 1})

print(new_model)  # 输出: MyEnum.FIRST
print(new_model.enum_field)  # 输出: MyEnum.FIRST

new_model2 = StatusModel(**{'enum_field': 1})
print(new_model2)
print(new_model2.enum_field)