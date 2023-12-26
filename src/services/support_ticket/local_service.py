import json
from typing import Optional

import requests

from models.ticket.type import Ticket
from typing import Any, Dict, List, Optional, Union
from utils import local_logger



def insert_ticket_to_webapi(url:str,ticket_record: Ticket) -> bool:
        data = json.loads(ticket_record.model_dump_json())  # 假设这返回一个字典
        try:
            response = requests.post(url, json=data)
            if response.status_code == 201:  # 假设201是预期的成功响应
                ticket_info = response.json()
                local_logger.logger.info("Ticket created successfully: %s", ticket_info)
                return True
            else:
                local_logger.logger.error("Failed to create ticket: Status %s; Response: %s", response.status_code, response.text)
                return False
        except requests.RequestException as e:
            local_logger.logger.error("Error while sending request: %s", str(e))
            return False

def get_ticket_by_webapi(url:str,input_uuid:Optional[str]) -> Optional[Ticket]:
        params = {
            'uu_id': input_uuid
        }
        headers = {
            'accept': 'application/json'
        }

        response = requests.get(url, params=params, headers=headers)
        data = response.json()
        if len(data) == 0:
            return None
        ticket = Ticket(**data[0])
        
        return ticket
        pass