
from datetime import datetime
import sys
sys.path.append("./src")
import time
from typing import Any, Optional

from base_class.user.type import User

from base_class.id.type import ID
from base_class.priority.type import Priority
from base_class.status.type import Status
from base_class.update_time.type import UpdateTime

class Ticket(ID, UpdateTime,Status,Priority):
    # 获取一个测试用的记录
    @staticmethod
    def get_instance() -> 'Ticket':
        return Ticket(ID.get_UUID().get_id(),1,1,1,"new ticket","",User.get_instance().get_id(), User.get_instance().get_id(), datetime.now())
    
    def __init__(self, 
                 id:str,
                 status:int,
                 priority:int,
                 type:int,
                 title:str ,
                 content:str, 
                 assigned_to_id:str,
                 creator_id:str,
                 create_time:datetime,
                 update_time:Optional[datetime] = None):
        ID.__init__(self, id)
        Status.__init__(self, status)  # Change self to status
        Priority.__init__(self, priority)
        self.__type = type
        
        UpdateTime.__init__(self, create_time,update_time)
        self.__title = title
        self.__content = content
        self.__assigned_to_id = assigned_to_id
        self.__creator_id = creator_id
        
    def get_title(self) -> str:
        return self.__title
    
    def get_assigned_to_user(self) -> str:
        return self.__assigned_to_id
    
    def get_creator(self) -> str:
        return self.__creator_id
    
    def to_dict(self) -> dict[str, Any]:
        return {
            'id': self.get_id(),
            'status': self.get_status(),
            'priority': self.get_priority(),
            'type': self.get_type(),
            'title': self.get_title(),
            'content': self.get_content(),
            'assigned_to_id': self.get_assigned_to_user(),
            'creator_id': self.get_creator(),
            'create_time': self.get_create_time(),
            'update_time': self.get_update_time()
        }
    
    def get_content(self) -> str:
        return self.__content
    
    def get_type(self) -> int:
        return self.__type
    
    
    
    pass 

# # 帮我测试
# if __name__ == '__main__':
#     from base_class.update_time.type import UpdateTime
#     id = '1'
#     create_time = UpdateTime(datetime.now())
#     ticket = Ticket(id," " ," ",User.get_instance(),User.get_instance(), create_time.get_create_time())
#     print(ticket.get_id())
#     print(ticket.get_create_time())
#     print(ticket.__dict__)
#     pass