
from datetime import datetime
import sys
import time
sys.path.append("./src")

from base_class.id.type import ID
from base_class.priority.type import Priority
from base_class.status.type import Status
from base_class.update_time.type import UpdateTime

class Ticket(UpdateTime,Priority,ID):

    # 获取一个测试用的记录
    @staticmethod
    def get_test():
        return Ticket(ID.get_UUID().get_id(), Priority.get_test(), Status.get_test(), UpdateTime(datetime.now()))
    
    def __init__(self, id:str ,priority: Priority, create_time: UpdateTime):
        ID.__init__(self, id)
        Priority.__init__(self, priority.get_priority())
        UpdateTime.__init__(self, create_time.get_create_time())
    pass 

# 帮我测试
if __name__ == '__main__':
    from base_class.priority.type import Priority
    from base_class.status.type import Status
    from base_class.update_time.type import UpdateTime
    id = '1'
    priority = Priority(Priority.NORMAL)
    create_time = UpdateTime(datetime.now())
    ticket = Ticket(id, priority, create_time)
    print(ticket.get_id())
    print(ticket.__dict__)
    pass