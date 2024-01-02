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
    models: Dict[str, Type[SQLModel]] = {}

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DatabaseCRUD, cls).__new__(cls)
        return cls._instance

    @classmethod
    def initialize(cls, database_url: str) -> None:
        cls.engine = create_engine(database_url)

    @classmethod
    def create(cls, model_instance: T) -> bool:
        data = model_instance.dict() if hasattr(model_instance, 'dict') else model_instance.__dict__
        
        # 使用显式类型转换
        new_instance = cls.models[model_instance.__class__.__name__](**data)
        new_instance = cast(T, new_instance)
        
        try:
            with Session(cls.engine) as session:
                session.add(new_instance)
                session.commit()
                session.refresh(new_instance)
                return True
        except Exception as e:
            print(f"Error occurred: {e}")
            return False
        
    @classmethod
    def register_model(cls, model_name: str, model: Type[SQLModel]) -> None:
        cls.models[model_name] = model

# 初始化 DatabaseCRUD
DatabaseCRUD.initialize("mysql+mysqlconnector://root:12345678@localhost:3308/panda_code_database")

# 注册模型
# DatabaseCRUD.register_model('Ticket', Ticket)
# ... 注册其他模型 ...




def import_and_register_models(pattern: str) -> None:
    for module_path in glob.glob(pattern, recursive=True):
        file = pathlib.Path(module_path)
        if file.stem.startswith('__'):
            continue

        module_name = file.stem
        spec = importlib.util.spec_from_file_location(module_name, module_path)

        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)  # 执行模块以加载定义

            # 遍历模块中的所有属性，检查它们是否是 SQLModel 的子类
            for attribute_name in dir(module):
                attribute = getattr(module, attribute_name)
                
                if isinstance(attribute, type) and issubclass(attribute, SQLModel):
                    # 如果是 SQLModel 子类，则注册到 DatabaseCRUD
                    DatabaseCRUD.register_model(attribute_name, attribute)

# 示例使用
import_and_register_models('./src/models/*/type.py')




# from sqlalchemy import create_engine
# import sys
# sys.path.append("./src")


# from sqlmodel import SQLModel


# import pathlib
# import importlib.util
# import glob
# from typing import Any


# def import_all_modules_from_pattern(pattern: str) -> None:
#     for module_path in glob.glob(pattern, recursive=True):
#         # Convert file path to pathlib.Path object
#         file = pathlib.Path(module_path)

#         # Skip special modules starting with '__'
#         if file.stem.startswith('__'):
#             continue

#         # Build module name
#         module_name = file.stem

#         # Import module dynamically
#         spec = importlib.util.spec_from_file_location(module_name, module_path)
#         if spec and spec.loader:
#             module = importlib.util.module_from_spec(spec)
#             spec.loader.exec_module(module)  # type: ignore
#             # 遍历模块中的所有属性，检查它们是否是 SQLModel 的子类
#             for attribute_name in dir(module):
#                 attribute = getattr(module, attribute_name)
                
#                 if isinstance(attribute, type) and issubclass(attribute, SQLModel):
#                     # 如果是 SQLModel 子类，则注册到 DatabaseCRUD
#                     DatabaseCRUD.register_model(attribute_name, attribute)

# # Use the function to import all modules from a specified pattern
# import_all_modules_from_pattern('./src/models/*/type.py')


# engine = create_engine("mysql+mysqlconnector://root:12345678@localhost:3308/panda_code_database")

# # 创建表，如果已存在则跳过
# SQLModel.metadata.create_all(engine)