"""
This module provides the API endpoints for support work_orders.
"""
import json



from fastapi import Body, Depends, FastAPI, Query, Response
from typing import List

from typing import TypeVar, List, Optional
from services.external.gpt_api import service

class GptAPI(FastAPI):
    def __init__(self) -> None:
        super().__init__()
        self.add_api_route("", self.get_res, methods=["GET"], summary="更新")
        pass

    
    async def get_res(self,
                  user_id: str = Query(..., description="User ID"),
                  user_message: str = Query(..., description="User Message")
                  ) -> Response:
        ai_res = service.get_ai_response(user_id, user_message)
        return  Response(status_code=200 , content=ai_res)
        
