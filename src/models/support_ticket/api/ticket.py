
import sys
sys.path.append("./src")

from datetime import datetime
from typing import Any, Dict
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


if __name__ == '__main__':
    tickets = get_tickets()
    for ticket in tickets:
        print(ticket.to_dict())
    pass
