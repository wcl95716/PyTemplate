from datetime import datetime

from typing import Any
import json



from fastapi import Depends, FastAPI, Response
from models.tables.user.type import User, UserBase, UserFilterParams

from services.common.user import service


class UserAPI(FastAPI):
    def __init__(self) -> None:
        super().__init__()
        self.add_api_route(
            "", self.add_user, methods=["Post"], summary="添加一个用户"
        )
        self.add_api_route(
            "", self.get_users_by_filter, methods=["Get"], summary="获取用户"
        )
        self.add_api_route(
            "",self.update, methods=["Put"] , summary = "更新用户信息"
        )
        pass
    
    async def add_user(self, user: User) -> Response:
    
        if service.add_user(user):
            return Response(status_code=200)
        else:
            return Response(status_code=500)
        pass
    
    # 修改用户信息
    async def update(self,user:User) -> Response:
        if service.update(user):
            return Response(status_code=200)
        else:
            return Response(status_code=500)
        pass
    
    async def get_users_by_filter(self,
            user_filter:UserFilterParams = Depends()
       ) -> Response:
        # user_filter = UserFilterParams(**user_filter.model_dump())
        users: list[User] = service.get_users_by_filter(user_filter)
        users_data: list[dict[str, Any]] = [user.model_dump() for user in users]
        return Response(
            content=json.dumps(users_data), 
            status_code=200)
        pass
    

    