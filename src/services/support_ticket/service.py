from datetime import datetime
from typing import Optional

from models.ticket.type import Ticket
from typing import Any, Dict, List, Optional, Union


from utils.database import DatabaseManager

table_name = "ticket"

def insert_ticket(ticket: Ticket) -> None:
    # 获取对象的所有属性及其值
    attrs = vars(ticket)
    
    # 特别处理 'destination' 字段，将其转换为 JSON 字符串
    # 构建列名和占位符
    columns = ', '.join(attrs.keys())
    placeholders = ', '.join(['%s'] * len(attrs))

    # 构建SQL语句
    sql = f"INSERT INTO {table_name}  ({columns}) VALUES ({placeholders})"
    # 构建参数元组
    args = tuple(attrs.values())
    DatabaseManager.execute(sql, args)
    
    pass


def update_ticket(ticket: Ticket) -> bool:
    sql = "UPDATE ticket SET status=%s, priority=%s, type=%s, title=%s, content=%s, assigned_to_id=%s, creator_id=%s, create_time=%s WHERE id=%s"
    args = (
        ticket.status,
        ticket.priority,
        ticket.type,
        ticket.title,
        ticket.content,
        ticket.assigned_to_id,
        ticket.creator_id,
        ticket.create_time,
        ticket.id,
    )
    if DatabaseManager.execute(sql, args):
        return True
    return False


def delete_ticket(ticket_id: Optional[str]) -> bool:
    sql = "DELETE FROM ticket WHERE id=%s"
    args = ticket_id
    if DatabaseManager.execute(sql, args):
        return True
    return False


# 根据条件获取tickets
# 例如 search_criteria:str , status:int ,start_date:str  , end_date:str
# 其中 search_criteria 为 title, content, assigned_to_id 的模糊搜索
# status 为工单状态
# start_date 为开始日期
# end_date 为结束日期
# 返回类型为 list[Ticket]
# 根据条件获取 tickets
# 根据条件获取 tickets
def get_tickets_by_filter(
    input_id: Optional[int] = None,
    input_uuid:Optional[str] = None,
    search_criteria: Optional[str] = None,
    status_filter: Optional[str] = None,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
) -> List[Ticket]:
    # 构建 SQL 查询
    sql = "SELECT * FROM ticket WHERE 1=1"

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
    tickets = []
    result = DatabaseManager.query_to_dict(sql, args)
    for row in result:
        ticket = Ticket(**row)
        tickets.append(ticket)

    return tickets
