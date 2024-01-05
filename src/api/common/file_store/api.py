"""
This module provides the API endpoints for support work_orders.
"""
import json

from fastapi.responses import FileResponse
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
        # self.add_api_route("", self.update_record, methods=["GET"], summary="更新")
        self.add_api_route("", self.delete_record, methods=["DELETE"], summary="删除")
        self.add_api_route("/get_file", self.get_record_by_id, methods=["GET"], summary="获取")
        self.add_api_route("/get_file_uu_id", self.get_record_by_uu_id, methods=["GET"], summary="获取")
        pass
    
    async def create_record(self , upload_file: UploadFile ) -> Response:
        record = service.upload_file(upload_file)
        if record is None:
            return Response(status_code=500) 
        if service.insert_record(record) is False:
            return Response(status_code=500)
        return Response(status_code=200 ,  content=json.dumps(record.model_dump()) , media_type="application/json") 
    
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
    
    async def get_record_by_uu_id(self , uu_id:str = Query(0, description="uu_id")) -> Response:
        print("uu_id",uu_id)
        record:Optional[FileStore] = service.get_record_by_uu_id(uu_id)
        print("record",record)
        if record is None:
            return Response(status_code=404)
        file_path = record.file_path
        print("file_path",file_path)
        return FileResponse(file_path)
        pass


    async def get_record_by_id(self , id:int = Query(0, description="uu_id")) -> Response:
        record:Optional[FileStore] = service.get_record_by_id(id)
        print("record",record)
        if record is None:
            return Response(status_code=404)
        file_path = record.file_path
        print("file_path",file_path)
        return FileResponse(file_path)
        pass
