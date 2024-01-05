"""
This module provides the API endpoints for support work_orders.
"""
import json
from models.common.id.type import ID
from models.tables.file_store.type import FileStore

from models.tables.notification_task.type import NotificationTask, NotificationTaskBase, NotificationTaskFilterParams


from fastapi import Body, Depends, FastAPI, Query, Response, UploadFile
from typing import List

from services.common.file_store import service
from typing import TypeVar, List, Optional

T = TypeVar("T", bound=ID)

class FileStoreAPI(FastAPI):
    def __init__(self) -> None:
        super().__init__()
        self.add_api_route("", self.create_record, methods=["POST"], summary="创建")
        self.add_api_route("", self.update_record, methods=["GET"], summary="更新")
        self.add_api_route("", self.delete_record, methods=["DELETE"], summary="删除")
        self.add_api_route("/get_record_by_id", self.get_record_by_id, methods=["GET"], summary="获取")
        pass
    
    async def create_record(self , upload_file: UploadFile ) -> Response:
        print("asdas ")
        record = service.upload_file(upload_file)
        if record is None:
            return Response(status_code=500) 
        service.insert_record(record)
        return Response(status_code=200)
    
    async def update_record(
        self, record: FileStore = Body(description="更新")
    ) -> Response:
        service.update_record(record)
        return Response(status_code=200)
        
    async def delete_record(
        self, id:int = Query(... , description="id")
    ) -> Response:

        service.delete_record(id)
        return Response(status_code=200)
    
    async def get_record_by_id(self , id:int = Query(0, description="WorkOrder ID")) -> Response:
        record:Optional[FileStore] = service.get_record_by_id(id)
        if record is None:
            return Response(status_code=404)
        return Response(content=json.dumps(record.model_dump()), media_type="application/json")
        pass
