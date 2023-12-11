from datetime import datetime

class UpdateTime:
    def __init__(self, create_time: datetime) -> None:
        # 在构造函数中使用参数 create_time 和 update_time，它们的类型应为 datetime.datetime
        self._create_time:datetime = create_time
        self._update_time:datetime = create_time
        
    def get_create_time(self) -> datetime:
        return self._create_time
    
    def get_update_time(self) -> datetime:
        return self._update_time
    
    def set_create_time(self, create_time: datetime) -> None:
        self.create_time = create_time
        
    def set_update_time(self, update_time: datetime) -> None:
        self._update_time = update_time
