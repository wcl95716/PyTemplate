import json
from typing import Optional, Dict, Any, List
import requests

from models.tables.work_order.type import WorkOrder

class WorkOrderClient:
    def __init__(self, base_url: str) -> None:
        self.base_url: str = base_url

    def get_work_orders(self, 
                    id: Optional[int] = None,
                    uu_id: Optional[str] = None,
                    search_criteria: Optional[str] = None,
                    status_filter: Optional[str] = None,
                    start_date: Optional[str] = None,
                    end_date: Optional[str] = None,
                    ) -> List[WorkOrder]:
        query_params = {
            "id": id,
            "uu_id": uu_id,
            "search_criteria": search_criteria,
            "status_filter": status_filter,
            "start_date": start_date,
            "end_date": end_date
        }
        # Remove None values
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = requests.get(f"{self.base_url}/work_order", params=query_params)
        result: List[WorkOrder] = [WorkOrder(**item) for item in response.json()]
        return result

    def delete_work_orders(self, id_list: List[str]) -> int:
        response = requests.delete(f"{self.base_url}/work_order", json={"id_list": id_list})
        return response.status_code

    def update_work_orders(self, work_order_data: WorkOrder) -> int:
        data = json.loads(work_order_data.model_dump_json())  # 假设这返回一个字典
        response = requests.put(f"{self.base_url}/work_order", json=data)
        return response.status_code

    def create_work_order(self, work_order_data: WorkOrder) -> int:
        data = json.loads(work_order_data.model_dump_json())  # 假设这返回一个字典
        response = requests.post(f"{self.base_url}/work_order", json=data)
        return response.status_code
