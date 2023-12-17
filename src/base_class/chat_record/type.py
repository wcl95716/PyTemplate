import datetime
import sys
import time
sys.path.append("./src")

# id 类  
# 属性为id
# 确保继承属性的类有一个唯一id

from base_class.id.type import ID
from base_class.record.type import Record
from base_class.user.type import User

# list[Record]  list[ChatRecord] 
class ChatRecord(Record):

    # 获取一个测试用的记录
    @staticmethod
    def get_instance() -> 'ChatRecord':
        return ChatRecord(Record.get_instance(), User.get_instance(), User.get_instance())
    
    def __init__(self,record:Record, user:User,to_user:User) -> None:
        # 调用父类的构造函数来初始化继承的属性
        Record.__init__(self, record.get_id(),record.get_records_type(), record.get_content())
        self.__user = user
        self.__to_user = to_user
        pass
    
    
    


