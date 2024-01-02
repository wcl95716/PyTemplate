from datetime import datetime

from typing import Any



from fastapi import Depends, FastAPI, Response
from models.user.type import User

from services.common.user import service


class UserAPI(FastAPI):
    def __init__(self) -> None:
        super().__init__()
        self.add_api_route(
            "", self.add_user, methods=["Post"], summary="添加一个用户"
        )
        pass
    
    async def add_user(self, user: User) -> Response:
        service.add_user(user)
        return Response(status_code=200)
        pass
    