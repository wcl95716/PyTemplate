"""
This module provides the API endpoints for support work_orders.
"""
from fastapi import Form
import requests
from typing import List
from models.tables.server_ip_map.type import ServerIPMap, ServerIPMapBase, ServerIPMapParams

class ServerIPMapClient:
    
    def __init__(self, base_url: str) -> None:
        self.base_url: str = base_url
        pass
    
    def create_record(self , record: ServerIPMapBase) -> bool:
        response =  requests.post(f"{self.base_url}/server_ip_map", json=record.model_dump(),verify=False)
        print(response)
        return response.status_code == 200
    
    def update_record(
        self, record: ServerIPMapBase
    ) -> bool:
        response = requests.put(f"{self.base_url}/server_ip_map", json=record.model_dump(),verify=False)
        return response.status_code == 200
        
        
    def delete_record(
        self, id:int 
    ) -> bool:
        response = requests.delete(f"{self.base_url}/server_ip_map", json={"id": id},verify=False)
        return response.status_code == 200
        pass
    
    def get_record_by_id(self , id:int) -> ServerIPMapBase:
        response = requests.get(f"{self.base_url}/server_ip_map/{id}",verify=False)
        return ServerIPMapBase(**response.json())
        pass
    
    # get_record_by_filter
    def get_record_by_filter(
        self, filter_params:ServerIPMapParams
    ) -> List[ServerIPMapBase]:
        response = requests.get(f"{self.base_url}/server_ip_map/get_by_filter", params=filter_params.model_dump(),verify=False)
        return [ServerIPMapBase(**item) for item in response.json()]
        pass
