
# id 类  
# 属性为id
# 确保继承属性的类有一个唯一id

from base.base.type import BaseClass
from base.id.type import ID


class User(ID):

    # 获取一个测试用的记录
    @staticmethod
    def get_test():
        return User(ID.get_test(),"test","test","test","test","test")
        pass

    # 姓名 手机 邮箱 头像 密码
    def __init__(self,id:str,name:str,phone:str,email:str = "",avatar:str = "",password:str = "") -> None:
        # 调用父类的构造函数来初始化继承的属性
        ID.__init__(self, id)
        self.__name = name
        self.__phone = phone
        self.__email = email
        self.__avatar = avatar
        self.__password = password
        pass
    
    def get_name(self):
        return self.__name
        pass  
    def get_phone(self):
        return self.__phone
        pass
    def get_email(self):
        return self.__email
        pass
    def get_avatar(self):
        return self.__avatar
        pass
    def get_password(self):
        return self.__password
        pass
    def to_dict(self):
        return self.__dict__
        pass 
    
    @classmethod
    def from_dict(cls , user_dict:dict):
        return cls(**user_dict)
        pass

    pass 


