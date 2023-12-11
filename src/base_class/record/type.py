from base_class.id.type import ID
from base_class.user.type import User

from enum import Enum

class RecordType(Enum):
    TEXT = 1
    IMAGE = 2
    VIDEO = 3
    FILE = 4
    
class Record(ID):
    def __init__(self, id:str,records_type: RecordType, content:str ) -> None:
        # 调用父类的构造函数来初始化继承的属性
        ID.__init__(self, id)
        self._records_type = records_type
        self._content = content
        pass
    
    def get_records_type(self):
        return self._records_type
    
    def get_content(self):
        return self._content

        
    
