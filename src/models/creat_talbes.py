

from sqlalchemy import create_engine
import sys
sys.path.append("./src")


from sqlmodel import SQLModel


import pathlib
import importlib.util
import glob
from typing import Any

def import_all_modules_from_pattern(pattern: str) -> None:
    for module_path in glob.glob(pattern, recursive=True):
        # Convert file path to pathlib.Path object
        file = pathlib.Path(module_path)

        # Skip special modules starting with '__'
        if file.stem.startswith('__'):
            continue

        # Build module name
        module_name = file.stem

        # Import module dynamically
        spec = importlib.util.spec_from_file_location(module_name, module_path)
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)  # type: ignore

# Use the function to import all modules from a specified pattern
import_all_modules_from_pattern('./src/models/*/type.py')



engine = create_engine("mysql+mysqlconnector://root:12345678@localhost:3308/panda_code_database")

# 创建表，如果已存在则跳过
SQLModel.metadata.create_all(engine)