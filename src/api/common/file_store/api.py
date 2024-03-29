"""
This module provides the API endpoints for support work_orders.
"""
import json
import os

from fastapi.responses import FileResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, UploadFile, File, HTTPException, Form
from fastapi.responses import JSONResponse

import os

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
        self.add_api_route("/upload_file", self.upload_file, methods=["POST"], summary="上传")
        pass
    
    async def create_record(self , upload_file: UploadFile ) -> Response:
        record = service.upload_file(upload_file)
        if record is None:
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
        # return StreamingResponse(file_like,  headers=headers , media_type=record.file_type)
    
        # 使用FileResponse以流的方式发送文件
        return FileResponse(file_path, headers={"Accept-Ranges": "bytes"})
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
    
    async def upload_file(self, file: UploadFile = File(...), total_chunks: int = Form(...), chunk_index: int = Form(...)) -> JSONResponse:
        try:
            # 定义文件路径，将文件名添加到上传文件夹路径后面
            file_path = f"./uploaded_files/{file.filename}"
            # 定义分片文件路径，使用分片索引作为后缀
            chunk_path = f"{file_path}.part{chunk_index}"

            # 如果文件不存在，创建一个空文件
            if not os.path.exists(file_path):
                with open(file_path, "wb") as f:
                    pass  # 创建一个空文件

            # 将分片写入分片文件
            with open(chunk_path, "wb") as f:
                f.write(await file.read())

            # 如果当前上传的分片是最后一个分片，则开始合并
            if chunk_index == total_chunks - 1:
                # 打开最终文件，将所有分片依次写入
                with open(file_path, "ab") as f:
                    for i in range(total_chunks):
                        chunk_path = f"{file_path}.part{i}"
                        with open(chunk_path, "rb") as chunk_file:
                            f.write(chunk_file.read())
                        os.remove(chunk_path)  # 合并完成后删除分片文件

            # 返回上传成功的响应
            return JSONResponse(status_code=201, content={"message": "Chunk uploaded successfully"})
        except Exception as e:
            # 如果出现错误，返回上传失败的响应
            raise HTTPException(status_code=500, detail=f"Failed to upload chunk: {str(e)}")