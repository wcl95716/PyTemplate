from typing import Any, Optional, Union
import uuid
from fastapi import Depends, FastAPI, Query
from pydantic import BaseModel, Field


from api.common.chat_record.api import CharRecordAPI

from api.common.support_ticket.api import TicketAPI

from api.common.user.api import UserAPI

from api.common.notification_task.api import NotificationTaskAPI


fast_api = FastAPI()
fast_api.include_router(
    TicketAPI().router, prefix="/ticket", tags=["Ticket Operations"]
)
fast_api.include_router(
    CharRecordAPI().router, prefix="/chat_record", tags=["Chat Record Operations"]
)

fast_api.include_router(
    UserAPI().router, prefix="/user", tags=[" User Operations"]
)

fast_api.include_router(
    NotificationTaskAPI().router, prefix="/notification_task", tags=[" Notification Task Operations"]
)





@fast_api.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello, World!"}

# 创建一个基本模型来定义输入参数
class QueryParams(BaseModel):
    param1: str = Query(..., description="Description for param1")
    param2: int = Query(..., description="Description for param2")

# 使用模型来定义 GET 请求的路由
@fast_api.get("/items")
async def get_items(query_params: QueryParams =  Depends()) -> dict[str, Union[str, int]]:
    # param1 = query_params.param1
    # param2 = query_params.param2

    # 在这里使用 param1 和 param2 来执行操作，例如从数据库中检索数据

    return {"param1": "param1", "param2": 2}


# @api_bp.route('/msg_cb', methods=['POST'])
# def message_callback():
#     if request.method == 'POST':
#         # 解析JSON数据
#         data = request.get_json()
#         # print("data ",data)

#         # 获取消息内容
#         message_content = data.get('content', '')

#         # 处理消息，这里简单打印消息内容
#         print("Received message:", message_content)
        
#         sendMsg(message_content,"Panda")

#         # 返回成功响应
#         return jsonify({"status": "success"})
