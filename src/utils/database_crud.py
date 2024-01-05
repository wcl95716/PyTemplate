import sys
sys.path.append("./src")

from models.common.id.type import ID
from models.common.update_time.type import UpdateTime


from typing import Any, List, Optional, Type, TypeVar, Dict, Generic, cast
from sqlmodel import SQLModel, Session, create_engine
from sqlalchemy.engine.base import Engine
from dbutils.pooled_db import PooledDB
import sqlalchemy
from typing import Optional, Type, TypeVar, Dict, Generic
from sqlmodel import SQLModel

import glob
import pathlib
import importlib.util


from typing import Type, TypeVar, Generic, Optional
from sqlmodel import SQLModel, Session, create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy import Select, select
from typing import TypeVar, List, Optional



T = TypeVar("T", bound=ID)
class DatabaseCRUD:
    _instance: Optional['DatabaseCRUD'] = None
    engine: Optional[Engine] = None
    # models: Dict[str, Type[SQLModel]] = {}

    def __new__(cls, *args:Any, **kwargs:Any) -> "DatabaseCRUD":
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
        try:
            new_instance = model_instance.__class__(**model_instance.model_dump())
            with Session(cls.engine) as session:
                session.add(new_instance)
                session.commit()
                # session.refresh(new_instance)
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
                        if key == "create_time" or key == "update_time":
                            continue
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
    
    @classmethod
    def delete(cls,id:int ,  T: Type[T]) -> bool:
        try:
            # new_instance = model_instance.__class__(**model_instance.model_dump())
            with Session(cls.engine) as session:
                existing_record = session.get(T, id)
                if existing_record:
                    session.delete(existing_record)
                    session.commit()
                    return True
                else:
                    print("Record not found for delete.")
                    return False
        except Exception as e:
            print(f"Error occurred: {e}")
            return False
        
    @classmethod
    def read_by_id(cls, id: int, T: Type[T]) -> Optional[T]:
        try:
            with Session(cls.engine) as session:
                instance = session.get(T, id)
                return instance
        except  Exception as e:
            print(f"Error occurred: {e}")
            return None
        pass
    
    @classmethod
    def read_by_uu_id(cls, uu_id: str, T: Type[T]) -> Optional[T]:
        try:
            with Session(cls.engine) as session:
                query = select(T).filter(T.uu_id == uu_id) # type: ignore
                instance = session.exec(query).first()  # type: ignore
                if instance is None:
                    return None
                print("instance",instance)
                file_record = instance[0] if instance else None
                return file_record  # type: ignore
        except  Exception as e:
            print(f"Error occurred: {e}")
            return None
        pass

    # @classmethod
    # def read_all(cls, T: Type[T]) -> Optional[List[T]]:
    #     try:
    #         with Session(cls.engine) as session:
    #             instances = session.query(T).all()
    #             return instances
    #     except Exception as e:
    #         print(f"Error occurred: {e}")
    #         return None
    
# 初始化 DatabaseCRUD
DatabaseCRUD.initialize("mysql+mysqlconnector://root:12345678@localhost:3308/panda_code_database")



