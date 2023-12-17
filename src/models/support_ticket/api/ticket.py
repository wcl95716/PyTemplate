
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

def update_ticket(ticket:Ticket)->bool:
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

def get_ticket(ticket_id:str)-> Ticket:
    sql = "SELECT * FROM ticket WHERE id=%s"
    args = (ticket_id)
    result = DatabaseManager.query(sql, args)
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
    


if __name__ == '__main__':
    tickets = get_tickets()
    for ticket in tickets:
        print(ticket.to_dict())
    pass
