import json
from typing import Optional

import requests
from api.support_ticket.client_api import TicketClient

from models.ticket.type import Ticket
from typing import Any, Dict, List, Optional, Union
from utils import local_logger


def insert_ticket_to_webapi(url:str,ticket_record: Ticket) -> bool:
    ticket_client = TicketClient(url)
    ticket_client.create_ticket(ticket_record)
    return True
    pass

def get_ticket_by_webapi(url:str,input_uuid:Optional[str]) -> Optional[Ticket]:
        
        ticket_client = TicketClient(url)
        res =  ticket_client.get_tickets( uu_id=input_uuid)
        if len(res) == 0:
            return None
        return res[0]
        pass