from abc import ABC, abstractmethod
import sys
sys.path.append("./src")

# list[Record]  list[ChatRecord] 
class BaseClass(ABC):

    @classmethod
    @abstractmethod
    def get_test():
        pass
    
    def to_dict(self):
        pass
    pass 

    
    
    


