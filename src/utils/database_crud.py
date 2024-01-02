import sys
sys.path.append("./src")

from typing import Any, Optional, Type, TypeVar, Dict, Generic, cast
from sqlmodel import SQLModel, Session, create_engine
from sqlalchemy.engine.base import Engine
from dbutils.pooled_db import PooledDB
import sqlalchemy
from typing import Optional, Type, TypeVar, Dict, Generic
from sqlmodel import SQLModel

import glob
import pathlib
import importlib.util


T = TypeVar("T", bound=SQLModel)

from typing import Type, TypeVar, Generic, Optional
from sqlmodel import SQLModel, Session, create_engine
from sqlalchemy.engine.base import Engine





class DatabaseCRUD(Generic[T]):
    _instance: Optional['DatabaseCRUD'] = None
    engine: Optional[Engine] = None
    # models: Dict[str, Type[SQLModel]] = {}

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DatabaseCRUD, cls).__new__(cls)
        return cls._instance

    @classmethod
    def initialize(cls, database_url: str) -> None:
        cls.engine = create_engine(database_url)
        
    # @classmethod
    # def register_model(cls, model_name: str, model: Type[SQLModel]) -> None:
    #     cls.models[model_name] = model

    @classmethod
    def create(cls, model_instance: T) -> bool:
        # data = model_instance.dict() if hasattr(model_instance, 'dict') else model_instance.__dict__
        
        # # 使用显式类型转换
        # new_instance = cls.models[model_instance.__class__.__name__](**data)
        # new_instance = cast(T, new_instance)
        
        try:
            new_instance = model_instance.__class__(**model_instance.model_dump())
            with Session(cls.engine) as session:
                session.add(new_instance)
                session.commit()
                session.refresh(new_instance)
                return True
        except Exception as e:
            print(f"Error occurred: {e}")
            return False
    
    @classmethod
    def update(cls, model_instance: T) -> bool:
        try:
            new_instance = model_instance.__class__(**model_instance.model_dump())
            with Session(cls.engine) as session:
                existing_record = session.get(new_instance.__class__, model_instance.id)
                print("existing_record",existing_record)
                if existing_record:
                    # 更新字段值
                    for key, value in new_instance.model_dump().items():
                        setattr(existing_record, key, value)
                    
                    # 提交更改到数据库
                    session.commit()
                    return True
                else:
                    print("Record not found for update.")
                    return False
        except Exception as e:
            print(f"Error occurred: {e}")
            return False


# 初始化 DatabaseCRUD
DatabaseCRUD.initialize("mysql+mysqlconnector://root:12345678@localhost:3308/panda_code_database")



