import sys
import time

from pydantic import BaseModel
sys.path.append("./src")
from models.record.type import Record


class ChatRecord(Record,BaseModel):
    pass
    
    
if __name__ == "__main__":

    print( ChatRecord.model_json_schema() )

