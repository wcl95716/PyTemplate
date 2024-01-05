from datetime import datetime
import json
from typing import Optional

import requests
from models.tables.file_store.type import FileStore, FileStoreFilterParams

from models.tables.work_order.type import WorkOrder, WorkOrderBase
from typing import Any, Dict, List, Optional, Union
from utils import local_logger


from utils.database import DatabaseManager
from utils.database_crud import DatabaseCRUD

table_name = "filestore"

def insert_record( record: FileStore) -> bool:
    return DatabaseCRUD.create(record)
    pass

def update_record(record: FileStore) -> bool:
    return DatabaseCRUD.update(record)

def delete_record(id: int) -> bool:
    return DatabaseCRUD.delete(id , FileStore)

def get_record_by_id(work_order_id: int) -> Optional[FileStore]:
    return DatabaseCRUD.read_by_id(work_order_id, FileStore)



def get_record_by_filter(
    filter_params:FileStoreFilterParams
) -> List[FileStore]:


    return []




