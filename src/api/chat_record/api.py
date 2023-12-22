
from datetime import datetime
import sys
from typing import Any

from models.chat_record.type import ChatRecord
sys.path.append("./src")

from fastapi import FastAPI, Response

from services.chat_record import service
import json
from fastapi import FastAPI, Response
from models.chat_record.type import ChatRecord


class CharRecordAPI(FastAPI):
    
    def __init__(self) -> None:
        super().__init__()
        self.add_api_route("" ,self.get_record_by_creator_id , methods=["GET"], summary="获取一个用户的聊天记录" )
        pass
    
    async def get_record_by_creator_id(self, creat_id: str) -> Response:
        result: list[ChatRecord] =  service.get_chat_records_by_creator_id(creat_id)
        result_json_list:list[dict[str, Any]] =  [ item.model_dump() for item in result]
        def serialize_datetime(obj: datetime) -> str:
            if isinstance(obj, datetime):
                return obj.strftime("%Y-%m-%d %H:%M:%S")
        return Response(content=json.dumps(result_json_list,default=serialize_datetime ), media_type="application/json")
    
