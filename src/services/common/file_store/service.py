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


from utils.database import DatabaseManager
from utils.database_crud import DatabaseCRUD

table_name = "filestore"

from fastapi import UploadFile
import hashlib
import os

def upload_file(upload_file: UploadFile) -> Optional[FileStore] :
    try:
        # 初始化文件大小和哈希值
        file_size = 0
        hasher = hashlib.md5()
        
        # 指定文件保存路径
        save_path = "data/upload_file"
        os.makedirs(save_path, exist_ok=True)  # 确保目录存在
        #前缀添加时间戳
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = time + upload_file.filename if upload_file.filename else ""
        with open(os.path.join(save_path, file_name), "wb") as dest_file:
            while True:
                chunk = upload_file.file.read(65536)  # 以64KB块读取文件
                if not chunk:
                    break
                
                # 更新文件大小
                file_size += len(chunk)
                
                # 更新哈希值
                hasher.update(chunk)
                
                # 写入文件
                dest_file.write(chunk)
        
        # 计算文件哈希值
        file_hash = hasher.hexdigest()
        
        # 创建FileStore对象
        record = FileStore (
            file_name=upload_file.filename,
            file_path=os.path.join(save_path, file_name),
            file_size=file_size,
            file_type=upload_file.content_type,
            file_hash=file_hash,
            file_extension=file_name.split(".")[-1]
        )

        # 在这里，你可以将record对象插入数据库或执行其他操作
        return record
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


    return []




