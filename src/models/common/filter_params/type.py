# id 类
# 属性为id
# 确保继承属性的类有一个唯一id
from abc import ABC, abstractmethod
from typing import Any

from sqlmodel import SQLModel




class FilterParams(SQLModel):
    @abstractmethod
    def build_sql_query(self)-> tuple[str,list[Any]]:
        pass