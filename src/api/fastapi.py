import os
from typing import Any, Optional, Union
import uuid
from fastapi import Depends, FastAPI, Query, Response
from fastapi.responses import FileResponse, RedirectResponse
from pydantic import BaseModel, Field
from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import HTMLResponse


from api.common.chat_record.api import CharRecordAPI

from api.common.work_order.api import WorkOrderAPI

from api.common.user.api import UserAPI

from api.common.notification_task.api import NotificationTaskAPI

from api.common.file_store.api import FileStoreAPI

from api.common.gpt.api import GptAPI

from api.custom.wechat_receive.api import WechatReceiveAPI


fast_api = FastAPI()
fast_api.include_router(
    WorkOrderAPI().router, prefix="/work_order", tags=["WorkOrder Operations"]
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

fast_api.include_router(
    FileStoreAPI().router, prefix="/file_store", tags=[" File Store Operations"]
)

fast_api.include_router(
    GptAPI().router, prefix="/gpt", tags=[" gpt"]
)

fast_api.include_router(
    WechatReceiveAPI().router, prefix="/wechat", tags=[" 微信"]
)


@fast_api.get("/", include_in_schema=False)
async def root() -> RedirectResponse:
    return RedirectResponse(url="/docs")



@fast_api.get("/docs", include_in_schema=False)
async def custom_docs() -> HTMLResponse:
    return get_swagger_ui_html(openapi_url="/openapi.json", title="Custom Docs")


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

# 使用模型来定义 GET 请求的路由
@fast_api.get("/{file_name}")
async def get_uploaded_file(file_name: str) -> Response:
    # 定义域名根目录的路径，根据您的实际设置进行更改
    root_directory = "data/files"
    
    print("file_name ", file_name)
    # 拼接要返回的文件的完整路径
    file_path = os.path.join(root_directory, file_name)
    
    # 使用FileResponse返回文件
    return FileResponse(file_path)
