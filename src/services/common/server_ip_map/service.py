from datetime import datetime
import json
from typing import Optional

import requests
from models.tables.server_ip_map.type import ServerIPMap, ServerIPMapParams

from models.tables.work_order.type import WorkOrder, WorkOrderBase
from typing import Any, Dict, List, Optional, Union
from utils import local_logger


from utils.database_pymysql_util import DatabaseManager
from utils.database_sqlmodel_util import DatabaseCRUD

table_name = "serveripmap"

def insert( record: ServerIPMap) -> bool :
    return DatabaseCRUD.create(record)
    pass

def update(record: ServerIPMap) -> bool:
    return DatabaseCRUD.update(record)

def delete(id: int) -> bool:
    return DatabaseCRUD.delete(id , ServerIPMap)

def get_by_id(work_order_id: int) -> Optional[ServerIPMap]:
    return DatabaseCRUD.read_by_id(work_order_id, ServerIPMap)

def get_by_filter(
    filter_params:ServerIPMapParams
) -> List[ServerIPMap]:
    sql = f"SELECT * FROM {table_name} WHERE 1=1 "
    sql1,args =  filter_params.build_sql_query()
    sql += sql1
    print(sql)
    print(args)
    res = DatabaseManager.query_to_dict(sql, args)
    result_list:list[ServerIPMap] = []
    for row in res:
        record = ServerIPMap(**row)
        result_list.append(record)
        pass
    return result_list
    return []


# def get_record_by_filter(
#     filter_params:FileStoreFilterParams
# ) -> List[FileStore]:
#     sql = f"SELECT * FROM {table_name} WHERE 1=1 "
#     sql1,args =  filter_params.build_sql_query()
#     sql += sql1
#     res = DatabaseManager.query_to_dict(sql, args)
#     tasks:list[FileStore] = []
#     for row in res:
#         task = FileStore(**row)
#         tasks.append(task)
#         pass
#     return tasks
#     return []


