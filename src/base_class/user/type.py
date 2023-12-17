
# id 类  
# 属性为id
# 确保继承属性的类有一个唯一id

from base_class.id.type import ID


class User(ID):

    # 获取一个测试用的记录
    @staticmethod
    def get_instance() -> "User":
        return User(ID.get_instance().get_id(),"test","test","test","test","test")
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
    
    def get_name(self) -> str:
        return self.__name
        pass  
    def get_phone(self) -> str:
        return self.__phone
        pass
    def get_email(self) -> str:
        return self.__email

    def get_avatar(self) -> str:
        return self.__avatar

    def get_password(self) -> str:
        return self.__password

    def to_dict(self) -> dict[str, str]:
        return self.__dict__

    @classmethod
    def from_dict(cls, user_dict: dict[str, str]) -> "User":
        return cls(**user_dict)

    pass 


