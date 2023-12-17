from enum import Enum
import random

from base_class.base.type import BaseClass


class Priority(BaseClass):
    HIGHEST = 0
    URGENT = 1
    NORMAL = 2
    NOT_URGENT = 3
    NOT_NEEDED = 4
    
    # 创建静态函数， 可以获取一个测试用例子
    # Create a static method to get a random test priority
    @staticmethod
    def get_instance() -> 'Priority':
        # Get a random priority
        random_priority = random.choice([Priority.HIGHEST, Priority.URGENT, Priority.NORMAL, Priority.NOT_URGENT, Priority.NOT_NEEDED])
        return Priority(random_priority)

    def __init__(self, priority_type: int):
        self.__priority_type = priority_type

    def get_priority(self) -> int:
        return self.__priority_type
    
    
