


import sys


sys.path.append("./src")

from datetime import datetime
from base_class.id.type import ID
from base_class.ticket.type import Ticket
from base_class.update_time.type import UpdateTime
from base_class.user.type import User


class TicketRecord(Ticket):

    def __init__(self, id:str ,title:str , assigned_to_user:User, create_time: datetime ):
        Ticket.__init__(self, id, title, assigned_to_user, create_time)
        pass
    
    
    
    pass
        
        
# 帮我测试
if __name__ == '__main__':
    id = '1'
    create_time = UpdateTime(datetime.now())
    ticket = TicketRecord(id," " ,User.get_instance(), create_time.get_create_time())
    print(ticket.get_id())
    print(ticket.get_create_time())
    print(ticket.__dict__)
    pass