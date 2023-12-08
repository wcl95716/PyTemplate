from base.id.type import ID
from base.user.type import User

from enum import Enum

    
class Record(ID):
    TEXT = 1
    IMAGE = 2
    VIDEO = 3
    FILE = 4
    LINK = 5

    # 获取一个测试用的记录
    @staticmethod
    def get_test():
        return Record(ID.get_test(), Record.TEXT, "This is a test record")

    def __init__(self, id:str,records_type: int, content:str ) -> None:
        # 调用父类的构造函数来初始化继承的属性
        ID.__init__(self, id)
        self.__records_type = records_type
        self.__content = content
        pass
    
    def get_records_type(self):
        return self.__records_type
    
    def get_content(self):
        return self.__content

        
    
