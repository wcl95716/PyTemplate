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
    filter_params:ServerIPMapParams = ServerIPMapParams(
        server_mac_address = record.server_mac_address
    )
    result_list = get_by_filter(filter_params)  
    if(len(result_list) > 0):
        return False
    return DatabaseCRUD.create(record)
    pass

def update(record: ServerIPMap) -> bool:
    local_logger.logger.info(f"update record is {record}")
    if (record.id == None): 
        if record.server_mac_address == None:
            local_logger.logger.info("server_mac_address is None")
            return False
        
        filter_params:ServerIPMapParams = ServerIPMapParams(
            server_mac_address = record.server_mac_address,
            id = record.id
        )
        result_list = get_by_filter(filter_params)
        if(len(result_list) == 0):
            return insert(record)
        record.id = result_list[0].id
    
    return DatabaseCRUD.update(record)

def delete(id: int) -> bool:
    return DatabaseCRUD.delete(id , ServerIPMap)

def get_by_id(work_order_id: int) -> Optional[ServerIPMap]:
    record = DatabaseCRUD.read_by_id(work_order_id, ServerIPMap)
    # print(f"record is {record.model_dump()}")
    if record is None:
        return None
    # record =  ServerIPMap(**record.model_dump())
    return record
def get_by_filter(
    filter_params:ServerIPMapParams
) -> List[ServerIPMap]:
    sql = f"SELECT * FROM {table_name} WHERE 1=1 "
    sql1,args =  filter_params.build_sql_query()
    sql += sql1
    local_logger.logger.info(f"sql {sql} , args {args}")
    res = DatabaseManager.query_to_dict(sql, args)
    result_list:list[ServerIPMap] = []
    for row in res:
        record = ServerIPMap(**row)
        result_list.append(record)
        pass
    return result_list


