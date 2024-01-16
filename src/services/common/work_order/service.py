from datetime import datetime
import json
from typing import Optional

import requests

from models.tables.work_order.type import WorkOrder, WorkOrderBase
from typing import Any, Dict, List, Optional, Union
from utils import local_logger


from utils.database import DatabaseManager
from utils.database_crud import DatabaseCRUD

table_name = "workorder"

def insert_work_order(work_order: WorkOrder) -> None:
    DatabaseCRUD.create(work_order)
    pass


def update_work_order(work_order: WorkOrder) -> bool:
    return DatabaseCRUD.update(work_order)


def delete_work_order(work_order_id: int) -> bool:
    return DatabaseCRUD.delete(work_order_id, WorkOrder)


def get_work_order_by_id(work_order_id: int) -> Optional[WorkOrder]:
    return DatabaseCRUD.read_by_id(work_order_id, WorkOrder)

# 根据条件获取work_orders
# 例如 search_criteria:str , status:int ,start_date:str  , end_date:str
# 其中 search_criteria 为 title, content, assigned_to_id 的模糊搜索
# status 为工单状态
# start_date 为开始日期
# end_date 为结束日期
# 返回类型为 list[WorkOrder]
# 根据条件获取 work_orders
# 根据条件获取 work_orders
def get_work_orders_by_filter(
    input_id: Optional[int] = None,
    input_uuid:Optional[str] = None,
    search_criteria: Optional[str] = None,
    status_filter: Optional[str] = None,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
) -> List[WorkOrderBase]:
    # 构建 SQL 查询
    sql = f"SELECT * FROM {table_name} WHERE 1=1"

    args: List[Union[int, str]] = []

    if status_filter is not None:
        sql += " AND status = %s"
        args.append(status_filter)

    if input_id is not None:
        sql += " AND id = %s"
        args.append(input_id)
        
    if input_uuid is not None:
        sql += " AND uu_id = %s"
        args.append(input_uuid)

    if search_criteria:
        sql += " AND (title LIKE %s OR content LIKE %s OR assigned_to_id LIKE %s)"
        args.extend(["%" + search_criteria + "%" for _ in range(3)])

    if start_date and end_date:
        sql += " AND create_time BETWEEN %s AND %s"
        args.extend([start_date, end_date])

    # 执行查询
    work_orders = []
    result = DatabaseManager.query_to_dict(sql, args)
    for row in result:
        work_order = WorkOrderBase(**row)
        work_orders.append(work_order)

    return work_orders




