
import sys
sys.path.append("./src")

from datetime import datetime
from typing import Any, Dict, List, Optional, Union
from base_class.ticket.type import Ticket

from utils.database import DatabaseManager

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

def get_tickets() -> list[Ticket]:
    sql = "SELECT * FROM ticket"
    result = DatabaseManager.query(sql)
    tickets = []
    for row in result:
        id:str = row[0]
        status:int = row[1]
        priority:int = row[2]
        type:int = row[3]
        title:str = row[4]
        content:str = row[5]
        assigned_to_id:str = row[6]
        creator_id:str = row[7]
        create_time:datetime = row[8]
        ticket = Ticket(id,status,priority,type,title,content,assigned_to_id,creator_id,create_time)
        tickets.append(ticket)
    return tickets


def update_ticket(ticket:Ticket) -> bool:
    sql = "UPDATE ticket SET status=%s, priority=%s, type=%s, title=%s, content=%s, assigned_to_id=%s, creator_id=%s, create_time=%s WHERE id=%s"
    args = (ticket.__status, ticket.get_priority(), ticket.__type, ticket.get_title(), ticket.get_content(), ticket.get_assigned_to_user(), ticket.get_creator(), ticket.get_create_time(), ticket.get_id())
    if DatabaseManager.execute(sql, args):
        return True
    return False


def delete_ticket(ticket_id:str)->bool:
    sql = "DELETE FROM ticket WHERE id=%s"
    args = (ticket_id)
    if DatabaseManager.execute(sql, args):
        return True
    return False


def get_ticket(ticket_id:str)-> Optional[Ticket]:
    sql = "SELECT * FROM ticket WHERE id=%s"
    args = (ticket_id)
    result = DatabaseManager.query(sql, args)
    if not result:
        return None
    
    id:str = result[0][0]
    status:int = result[0][1]
    priority:int = result[0][2]
    type:int = result[0][3]
    title:str = result[0][4]
    content:str = result[0][5]
    assigned_to_id:str = result[0][6]
    creator_id:str = result[0][7]
    create_time:datetime = result[0][8]
    ticket = Ticket(id,status,priority,type,title,content,assigned_to_id,creator_id,create_time)
    return ticket
    pass
    
# 根据条件获取tickets
# 例如 search_criteria:str , status:int ,start_date:str  , end_date:str
# 其中 search_criteria 为 title, content, assigned_to_id 的模糊搜索
# status 为工单状态
# start_date 为开始日期
# end_date 为结束日期
# 返回类型为 list[Ticket]
# 根据条件获取 tickets
# 根据条件获取 tickets
def get_tickets_by_filter(search_criteria: Optional[str], status_filter: Optional[int], start_date: Optional[str], end_date: Optional[str]) -> List[Ticket]:
    # 构建 SQL 查询
    sql = "SELECT * FROM ticket WHERE 1=1"

    args: List[Union[int, str]] = []

    if status_filter is not None:
        sql += " AND status = %s"
        args.append(status_filter)

    if search_criteria:
        if search_criteria == "title":
            sql += " AND title LIKE %s"
        elif search_criteria == "content":
            sql += " AND content LIKE %s"
        elif search_criteria == "assigned_to_id":
            sql += " AND assigned_to_id LIKE %s"
        elif search_criteria == "creator_id":
            sql += " AND creator_id LIKE %s"
        args.append('%' + str(search_criteria) + '%')

    if start_date and end_date:
        sql += " AND create_time BETWEEN %s AND %s"
        args.extend([start_date, end_date])

    # 执行查询
    tickets = []
    result = DatabaseManager.query(sql, args)

    for row in result:
        id = row[0]
        status = row[1]
        priority = row[2]
        type = row[3]
        title = row[4]
        content = row[5]
        assigned_to_id = row[6]
        creator_id = row[7]
        create_time = row[8]

        # 创建 Ticket 对象并添加到列表
        ticket = Ticket(id, status, priority, type, title, content, assigned_to_id, creator_id, create_time)
        tickets.append(ticket)

    return tickets


if __name__ == '__main__':
    tickets = get_tickets_by_filter("1", None, None,None)
    for ticket in tickets:
        print(ticket.to_dict())
    
    
    pass
