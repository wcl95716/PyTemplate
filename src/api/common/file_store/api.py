"""
This module provides the API endpoints for support work_orders.
"""
import json
import os

from fastapi.responses import FileResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles

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
        self.add_api_route("/get_file/{id}", self.get_record_by_id, methods=["GET"], summary="获取")
        self.add_api_route("/get_file_uu_id/{uu_id}", self.get_record_by_uu_id, methods=["GET"], summary="获取")
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
    
    async def get_record_by_uu_id(self , uu_id:str ) -> Response:

        record:Optional[FileStore] = service.get_record_by_uu_id(uu_id)
        
        # 如果没有找到记录，则返回404响应
        if record is None:
            return Response(status_code=404)
        # 获取文件路径
        file_path = record.file_path
        # 以二进制读取模式打开文件
        file_like = open(file_path, mode="rb")
        
        # 准备响应头部，包括接受范围请求和内容长度
        headers = {
            "Accept-Ranges": "bytes",
            "Content-Length": str(record.file_size)
        }   
        
        # 返回一个StreamingResponse，将文件流式传输到客户端
        return StreamingResponse(file_like,  headers=headers , media_type=record.file_type)
        pass


    async def get_record_by_id(self , id:int ) -> Response:
        # 从服务中根据ID获取文件存储记录
        record:Optional[FileStore] = service.get_record_by_id(id)

        # 如果没有找到记录，则返回404响应
        if record is None:
            return Response(status_code=404)
        # 获取文件路径
        file_path = record.file_path
        # 以二进制读取模式打开文件
        file_like = open(file_path, mode="rb")
        
        # 准备响应头部，包括接受范围请求和内容长度
        headers = {
            "Accept-Ranges": "bytes",
            "Content-Length": str(record.file_size)
        }   
        
        # 返回一个StreamingResponse，将文件流式传输到客户端
        return StreamingResponse(file_like,  headers=headers , media_type=record.file_type)
        # return StaticFiles(directory=file_path)
        pass
