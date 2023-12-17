
from datetime import datetime
import sys
sys.path.append("./src")
import time
from typing import Any

from base_class.user.type import User

from base_class.id.type import ID
from base_class.priority.type import Priority
from base_class.status.type import Status
from base_class.update_time.type import UpdateTime

class Ticket(ID, UpdateTime):
    # 获取一个测试用的记录
    @staticmethod
    def get_instance() -> 'Ticket':
        return Ticket(ID.get_UUID().get_id(),"new ticket", User.get_instance(), datetime.now())
    
    def __init__(self, id:str ,title:str , assigned_to_user:User, create_time:datetime ):
        ID.__init__(self, id)
        UpdateTime.__init__(self, create_time)
        self.__title = title
        self.__assigned_to_user = assigned_to_user
        
    def get_title(self) -> str:
        return self.__title
    
    def get_assigned_to_user(self) -> User:
        return self.__assigned_to_user
    
    def to_dict(self) -> dict[str, Any]:
        return self.__dict__
    
    
    pass 

# 帮我测试
if __name__ == '__main__':
    from base_class.update_time.type import UpdateTime
    id = '1'
    create_time = UpdateTime(datetime.now())
    ticket = Ticket(id," " ,User.get_instance(), create_time.get_create_time())
    print(ticket.get_id())
    print(ticket.get_create_time())
    print(ticket.__dict__)
    pass