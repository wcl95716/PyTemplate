from datetime import datetime
import hashlib
import json
from typing import Optional
from fastapi import UploadFile

import requests
from models.tables.file_store.type import FileStore, FileStoreFilterParams

from models.tables.work_order.type import WorkOrder, WorkOrderBase
from typing import Any, Dict, List, Optional, Union
from utils import local_logger


from utils.database_pymysql_util import DatabaseManager
from utils.database_sqlmodel_util import DatabaseCRUD
from utils.file_operations_utils import calculate_file_hash, calculate_file_size

table_name = "filestore"

from fastapi import UploadFile
import hashlib
import os

def upload_file(upload_file: UploadFile) -> Optional[FileStore] :
    try:

        
        # 指定文件保存路径
        save_path = "data/upload_file"
        os.makedirs(save_path, exist_ok=True)  # 确保目录存在
        #前缀添加时间戳
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        
        file_name = time + upload_file.filename if upload_file.filename else ""
        file_path = os.path.join(save_path, file_name)
        with open(file_path, "wb") as dest_file:
            dest_file.write(upload_file.file.read())
            pass
        
        file_hash = calculate_file_hash(file_path)
        file_size = calculate_file_size(file_path)
        
        # 创建FileStore对象
        record = FileStore (
            file_name=upload_file.filename,
            file_path=file_path,
            file_size=file_size,
            file_type=upload_file.content_type,
            file_hash=file_hash,
            file_extension=file_name.split(".")[-1]
        )
        res = get_record_by_filter(FileStoreFilterParams(file_hash = file_hash))
        if len(res) > 0 and res[0].file_size == record.file_size and res[0].file_extension == record.file_extension:
            # 删除 file_path 的文件
            os.remove(record.file_path)
            return res[0]
        # 在这里，你可以将record对象插入数据库或执行其他操作
        if insert_record(record):
            return record
        else:
            return None
    except Exception as e:
        # 处理异常
        print(e)
        return None
        pass
    
    return None


def insert_record( record: FileStore) -> bool:
    return DatabaseCRUD.create(record)
    pass

def update_record(record: FileStore) -> bool:
    return DatabaseCRUD.update(record)

def delete_record(id: int) -> bool:
    return DatabaseCRUD.delete(id , FileStore)

def get_record_by_id(id: int) -> Optional[FileStore]:
    return DatabaseCRUD.read_by_id(id, FileStore)

def get_record_by_uu_id(uu_id: str) -> Optional[FileStore]:
    record = DatabaseCRUD.read_by_uu_id(uu_id, FileStore)
    if record is None:
        return None
    return record

def get_record_by_filter(
    filter_params:FileStoreFilterParams
) -> List[FileStore]:
    sql = f"SELECT * FROM {table_name} WHERE 1=1 "
    sql1,args =  filter_params.build_sql_query()
    sql += sql1
    res = DatabaseManager.query_to_dict(sql, args)
    tasks:list[FileStore] = []
    for row in res:
        task = FileStore(**row)
        tasks.append(task)
        pass
    return tasks
    return []




