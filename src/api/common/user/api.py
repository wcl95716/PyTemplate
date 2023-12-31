from datetime import datetime

from typing import Any

from models.chat_record.type import ChatRecord


from fastapi import Depends, FastAPI, Response
from models.user.type import User, UserFilter

from services.common.user import service


class UserAPI(FastAPI):
    def __init__(self) -> None:
        super().__init__()
        self.add_api_route(
            "", self.add_user, methods=["Post"], summary="添加一个用户"
        )
        self.add_api_route(
            "", self.get_users_by_filter, methods=["GET"], summary="获取用户"
        )
        
        pass
    
    async def add_user(self, user: User) -> Response:
        service.add_user(user)
        return Response(status_code=200)
        pass
    
    async def get_users_by_filter(
        self, user_filter: UserFilter = Depends()
        ) -> Response:
        
        return Response(status_code=200)
        pass