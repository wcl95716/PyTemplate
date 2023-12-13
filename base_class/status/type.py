from enum import Enum
import random

from base_class.base.type import BaseClass


class Status(BaseClass):
    NEW = 0
    IN_PROGRESS = 1
    COMPLETED = 2
    CLOSED = 3

    # 创建静态函数， 可以获取一个测试用例子
    # Create a static method to get a  test status
    @staticmethod
    def get_test():
        # Get a random priority
        random_status = random.choice([Status.NEW, Status.IN_PROGRESS, Status.COMPLETED, Status.CLOSED])
        return Status(random_status)

    def __init__(self, status: int):
        self.__status = status

    def get_status(self):
        return self.__status
    
    
