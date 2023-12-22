from pydantic import BaseModel
from models.id.type import ID

from models.update_time.type import UpdateTime

class Record(ID,UpdateTime,BaseModel):
    type:int
    content:str
    title:str 
    creator_id:str
    assigned_to_id:str
    pass


    
    
    
    
    
    
    
    

        
    
