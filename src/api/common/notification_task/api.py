"""
This module provides the API endpoints for support work_orders.
"""
from datetime import datetime
import json

from fastapi.encoders import jsonable_encoder
from models.tables.notification_task.type import NotificationEnum, NotificationFilterEnum, NotificationTask, NotificationTaskBase, NotificationTaskFilterParams
from services.common.notification_task import service

from unittest.mock import Base

from pydantic import BaseModel


from fastapi import APIRouter, Body, Depends, FastAPI, Query, HTTPException, Response
from typing import Any, List, Optional, Union

from models.tables.work_order.type import WorkOrder, WorkOrderBase

class NotificationTaskAPI(FastAPI):
    def __init__(self) -> None:
        super().__init__()
        self.add_api_route("", self.create, methods=["POST"], summary="创建通知任务")
        self.add_api_route("/get", self.get_by_filter, methods=["GET"], summary="根据条件获取通知任务")
        pass
    
    async def create(self , task:NotificationTask = Body(..., description="任务")) -> Response:
        success: bool = service.insert_notification(task)
        return Response(status_code=200) if success else Response(status_code=500)
    
    async def get_by_filter(self , filter: NotificationTaskFilterParams = Depends() ) -> Response:
        tasks: List[NotificationTaskBase] = service.query_notification_task_by_filter_params(filter)
        return Response(
            content=json.dumps([task.model_dump() for task in tasks]),
            media_type="application/json",
        )
    
        pass 

    # async def get_by_filter(self , filter: NotificationEnum = Query(..., description="通知类型")) -> Response:
    #     print("filter ",filter , type(filter) )
    #     return Response(status_code=200)
    #     pass 