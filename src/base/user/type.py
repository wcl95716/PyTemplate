
# id 类  
# 属性为id
# 确保继承属性的类有一个唯一id

from base.id.type import ID


class User(ID):
    def __init__(self,id:str,name:str) -> None:
        # 调用父类的构造函数来初始化继承的属性
        ID.__init__(self, id)
        self._name = name
        pass
    
    def get_name(self):
        return self._name
        pass  
    
    
    
    pass 


