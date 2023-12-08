
# id 类  
# 属性为id
# 确保继承属性的类有一个唯一id

from base.id.type import ID


class User(ID):
    # 姓名 手机 邮箱 头像 密码
    def __init__(self,id:str,name:str,phone:str,email:str = "",avatar:str = "",password:str = "") -> None:
        # 调用父类的构造函数来初始化继承的属性
        ID.__init__(self, id)
        self._name = name
        self._phone = phone
        self._email = email
        self._avatar = avatar
        self._password = password
        pass
    
    def get_name(self):
        return self._name
        pass  
    def get_phone(self):
        return self._phone
        pass
    def get_email(self):
        return self._email
        pass
    def get_avatar(self):
        return self._avatar
        pass
    def get_password(self):
        return self._password
        pass
    def to_dict(self):
        return self.__dict__
        pass 
    
    @classmethod
    def from_dict(cls , user_dict:dict):
        return cls(**user_dict)
        pass

    pass 


