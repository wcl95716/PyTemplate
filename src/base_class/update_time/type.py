from datetime import datetime

from base_class.base.type import BaseClass


class UpdateTime(BaseClass):
    # 获取一个测试用的记录
    @staticmethod
    def get_instance() ->  'UpdateTime':
        return UpdateTime(datetime.now())

    def __init__(self, create_time: datetime) -> None:
        # 在构造函数中使用参数 create_time 和 update_time，它们的类型应为 datetime.datetime
        self.__create_time:datetime = create_time
        self.__update_time:datetime = create_time
        
    def get_create_time(self) -> datetime:
        return self.__create_time
    
    def get_update_time(self) -> datetime:
        return self.__update_time
    
    def set_create_time(self, create_time: datetime) -> None:
        self.create_time = create_time
        
    def set_update_time(self, update_time: datetime) -> None:
        self.__update_time = update_time
