
# id 类  
# 属性为id
# 确保继承属性的类有一个唯一id




from base_class.base.type import BaseClass


class ID(BaseClass):
        
    # 创建静态函数 用于获取一个随机的ID 唯一的uuid
    @classmethod
    def get_UUID(cls) -> 'ID':
        import uuid
        return ID(uuid.uuid4().hex)
        pass
    
    #创建静态函数， 可以获取一个测试用的ID
    count = 0
    @classmethod
    def get_test(cls) -> 'ID':
        ID.count += 1
        return ID(ID.count)
    
        pass
    
    def __init__(self,id) -> None:
        self.__id = id
        pass
    
    def get_id(self): 
        return self.__id   
        pass     
    
    
    pass 


