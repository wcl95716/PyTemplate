import sys

from models.ticket.type import Ticket
sys.path.append("./src")

from datetime import datetime
from typing import Any, Dict, List, Optional, Union
# from base_class.ticket.type import Ticket

from utils.database import DatabaseManager
from typing import Optional

def insert_ticket(
                 status:int,
                 priority:int,
                 type:int,
                 title:str ,
                 content:str, 
                 assigned_to_id:str,
                 creator_id:str,
                 create_time:datetime
) -> None:
    sql = "INSERT INTO ticket (status, priority, type, title, content, assigned_to_id, creator_id, create_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    args = (status, priority, type, title, content, assigned_to_id, creator_id, create_time)
    DatabaseManager.execute(sql, args)
    
    pass 

def update_ticket(ticket:Ticket) -> bool:
    sql = "UPDATE ticket SET status=%s, priority=%s, type=%s, title=%s, content=%s, assigned_to_id=%s, creator_id=%s, create_time=%s WHERE id=%s"
    args = (ticket.status, ticket.priority, ticket.type, ticket.title, ticket.content, ticket.assigned_to_id, ticket.creator_id, ticket.create_time, ticket.id)
    if DatabaseManager.execute(sql, args):
        return True
    return False


def delete_ticket(ticket_id:Optional[str])->bool:
    sql = "DELETE FROM ticket WHERE id=%s"
    args = (ticket_id)
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
def get_tickets_by_filter(input_id: Optional[str] = None, search_criteria: Optional[str] = None, status_filter: Optional[str] = None, start_date: Optional[str] = None, end_date: Optional[str] = None) -> List[Ticket]:
    # 构建 SQL 查询
    sql = "SELECT * FROM ticket WHERE 1=1"

    args: List[Union[int, str]] = []

    if status_filter is not None:
        sql += " AND status = %s"
        args.append(status_filter)
    
    if input_id is not None:
        sql += " AND id = %s"
        args.append(input_id)

    if search_criteria:
        sql += " AND (title LIKE %s OR content LIKE %s OR assigned_to_id LIKE %s)"
        args.extend(['%' + search_criteria + '%' for _ in range(3)])

    if start_date and end_date:
        sql += " AND create_time BETWEEN %s AND %s"
        args.extend([start_date, end_date])

    # 执行查询
    tickets = []
    result = DatabaseManager.query(sql, args)
    for row in result:
        this_id = row[0]
        status = row[1]
        priority = row[2]
        type = row[3]
        title = row[4]
        content = row[5]
        assigned_to_id = row[6]
        creator_id = row[7]
        create_time = row[8]
        update_time = row[9]
        
        print("this_id",this_id)
        # 创建 Ticket 对象并添加到列表
        ticket = Ticket(
            id=this_id,
            status=status,
            priority=priority,
            type=type,
            title=title,
            content=content,
            assigned_to_id=assigned_to_id,
            creator_id=creator_id,
            create_time=create_time,
            update_time=update_time
        )
        tickets.append(ticket)

    return tickets


