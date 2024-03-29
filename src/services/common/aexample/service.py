from datetime import datetime
import json
from typing import Optional

import requests
from models.tables.file_store.type import FileStore, FileStoreFilterParams

from models.tables.work_order.type import WorkOrder, WorkOrderBase
from typing import Any, Dict, List, Optional, Union
from utils import local_logger


from utils.database_pymysql_util import DatabaseManager
from utils.database_sqlmodel_util import DatabaseCRUD

table_name = "filestore"

def insert( record: FileStore) -> None:
    DatabaseCRUD.create(record)
    pass

def updater(record: FileStore) -> bool:
    return DatabaseCRUD.update(record)

def delete(id: int) -> bool:
    return DatabaseCRUD.delete(id , FileStore)

def get_by_id(work_order_id: int) -> Optional[WorkOrder]:
    return DatabaseCRUD.read_by_id(work_order_id, WorkOrder)

def get_by_filter(
    filter_params:FileStoreFilterParams
) -> List[FileStore]:


    return []




