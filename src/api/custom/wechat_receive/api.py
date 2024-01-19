"""
This module provides the API endpoints for support work_orders.
"""
import json

from fastapi import Body, Depends, FastAPI, Query, Response
from typing import Any, List


class WechatReceiveAPI(FastAPI):
    def __init__(self) -> None:
        super().__init__()
        self.add_api_route("", self.get_res, methods=["POST"], summary="接收企业微信消息")
        pass

    
    async def get_res(self,
                      # data: dict[str, Any]     
                  ) -> Response:
        # print("data " ,data)
        return  Response(status_code=200 , content="success")
        
# @api_bp.route('/msg_cb', methods=['POST'])
# def message_callback():
#     if request.method == 'POST':
#         # 解析JSON数据
#         data = request.get_json()
#         # print("data ",data)

#         # 返回成功响应
#         return jsonify({"status": "success"})
