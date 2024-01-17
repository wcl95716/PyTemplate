from typing import Any, Optional, Union
import uuid
from fastapi import Depends, FastAPI, Query
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, Field
from fastapi import FastAPI


app = FastAPI(docs_url=None, redoc_url=None)

@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")


# 其他路由和业务逻辑...



from api.common.chat_record.api import CharRecordAPI

from api.common.work_order.api import WorkOrderAPI

from api.common.user.api import UserAPI

from api.common.notification_task.api import NotificationTaskAPI

from api.common.file_store.api import FileStoreAPI


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





@fast_api.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")

@fast_api.get("/docs", include_in_schema=False)
async def custom_docs():
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
