"""
This module provides the API endpoints for support work_orders.
"""
import json
from models.common.id.type import ID
from models.tables.file_store.type import FileStore

from models.tables.notification_task.type import NotificationTask, NotificationTaskBase, NotificationTaskFilterParams


from fastapi import Body, Depends, FastAPI, Query, Response
from typing import List
from models.tables.server_ip_map.type import ServerIPMap, ServerIPMapParams

from services.common.server_ip_map import service
from typing import TypeVar, List, Optional

T = TypeVar("T", bound=ID)

class ServerIPMapAPI(FastAPI):
    def __init__(self) -> None:
        super().__init__()
        self.add_api_route("", self.create_record, methods=["POST"], summary="创建")
        self.add_api_route("", self.update_record, methods=["PUT"], summary="更新")
        self.add_api_route("", self.delete_record, methods=["DELETE"], summary="删除")
        self.add_api_route("", self.get_record_by_id, methods=["GET"], summary="获取")
        self.add_api_route("/get_by_filter", self.get_record_by_filter, methods=["GET"], summary="获取")
        pass
    
    async def create_record(self , record: ServerIPMap = Body(..., description="创建")) -> Response:
        success: bool = service.insert(record)
        return Response(status_code=200) if success else Response(status_code=500)
    
    async def update_record(
        self, record: ServerIPMap = Body(description="更新")
    ) -> Response:
        service.update(record)
        return Response(status_code=200)
        
    async def delete_record(
        self, id:int = Query(... , description="id")
    ) -> Response:

        service.delete(id)
        return Response(status_code=200)
    
    async def get_record_by_id(self , id:int = Query(0, description="WorkOrder ID")) -> Response:
        record:Optional[ServerIPMap] = service.get_by_id(id)
        if record is None:
            return Response(status_code=404)
        return Response(content=json.dumps(record.model_dump()), media_type="application/json")
        pass
    
    # get_record_by_filter
    async def get_record_by_filter(
        self, filter_params:ServerIPMapParams = Depends()
    ) -> Response:
        records:List[ServerIPMap] = service.get_by_filter(filter_params)
        return Response(content=json.dumps([record.model_dump() for record in records]), media_type="application/json")
        pass
