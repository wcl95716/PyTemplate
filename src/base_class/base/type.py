from abc import ABC, abstractmethod
import sys
sys.path.append("./src")




# list[Record]  list[ChatRecord] 
class BaseClass(ABC):


    # 定义接口：@abstractmethod装饰器用于定义任何非抽象子类必须实现的方法。这类似于在其他编程语言中定义接口。
    # 强制实现：在抽象基类中使用@abstractmethod可以确保所有子类都实现这些方法。这对于保持一致的接口和预期行为非常重要。
    # 防止直接实例化：带有抽象方法的类不能被直接实例化。这样可以防止创建不完整或不符合要求的对象。
    # 设计模式和架构：在复杂的软件设计和架构中，抽象基类和抽象方法有助于提供清晰的层次结构和责任划分。这对于大型项目和团队合作尤其重要。
    @abstractmethod
    @classmethod
    def get_test(cls):
        pass
    
    # @abstractmethod
    def to_dict(self):
        pass
    pass 

    
    
    


