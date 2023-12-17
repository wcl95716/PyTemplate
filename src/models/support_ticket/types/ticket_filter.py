


import sys
sys.path.append("./src")

from datetime import datetime
from base_class.id.type import ID
from base_class.ticket.type import Ticket
from base_class.update_time.type import UpdateTime
from base_class.user.type import User


class TicketFilter:
    def __init__(self, search_criteria:str , status:int ,start_date:str  , end_date:str ):
        self.search_criteria = search_criteria
        self.status = status
        self.start_date = start_date
        self.end_date = end_date
        pass 
    