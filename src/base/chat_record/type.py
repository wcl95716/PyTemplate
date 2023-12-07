import datetime
import sys
import time
sys.path.append("./src")

# id 类  
# 属性为id
# 确保继承属性的类有一个唯一id

from base.id.type import ID
from base.record.type import Record
from base.user.type import User

# list[Record]  list[ChatRecord] 
class ChatRecord(Record):
    def __init__(self,record:Record, user:User,to_user:User) -> None:
        # 调用父类的构造函数来初始化继承的属性
        Record.__init__(self, record.get_id(),record.get_records_type(), record.get_content())
        self._user = user
        self._to_user = to_user
        pass
        pass
    
    
# 创建一个测试类
class Test:
    def __init__(self) -> None:
        pass
    
    def test(self):
        # 创建一个Record
        record = Record(1,1,"test")
        # 创建一个User
        user = User(2,"user")
        
        touser = User(3,"touser")
        # 创建一个ChatRecord
        chat_record = ChatRecord(record,user,touser)
        # 测试
        print(chat_record.get_id())
        print(chat_record.get_records_type())
        print(chat_record.get_content())
        
        print(chat_record.__dict__)
        pass
    
    pass

if __name__ == "__main__":
    test = Test()
    test.test()
    pass
    
    


