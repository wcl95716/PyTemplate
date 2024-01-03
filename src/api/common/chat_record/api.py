from datetime import datetime

from typing import Any

from models.tables.chat_record.type import ChatRecord, ChatRecordBase


from fastapi import FastAPI, Response

from services.common.chat_record import service
import json
from fastapi import FastAPI, Response


class CharRecordAPI(FastAPI):
    def __init__(self) -> None:
        super().__init__()
        self.add_api_route(
            "", self.get_record_by_creator_id, methods=["GET"], summary="获取一个用户的聊天记录"
        )
        self.add_api_route(
            "", self.add_chat_record_wrapper, methods=["POST"], summary="添加一条聊天记录"
        )
        pass

    async def add_chat_record_wrapper(self, chat_record: ChatRecordBase) -> Response:
        success: bool = service.add_chat_record(chat_record)

        return Response(status_code=200) if success else Response(status_code=500)

    async def get_record_by_creator_id(self, creat_id: str) -> Response:
        result: list[ChatRecord] = service.get_chat_records_by_creator_id(creat_id)
        result_json_list: list[dict[str, Any]] = [item.model_dump() for item in result]
        def serialize_datetime(obj: datetime) -> str:
            if isinstance(obj, datetime):
                return obj.strftime("%Y-%m-%d %H:%M:%S")

        return Response(
            content=json.dumps(result_json_list, default=serialize_datetime),
            media_type="application/json",
        )
        