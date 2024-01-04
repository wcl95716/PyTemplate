"""
This module provides the API endpoints for support work_orders.
"""
from datetime import datetime
import json

from fastapi.encoders import jsonable_encoder
from services.common.work_order import service

from unittest.mock import Base

from pydantic import BaseModel


from fastapi import APIRouter, Body, FastAPI, Query, HTTPException, Response
from typing import Any, List, Optional

from models.tables.work_order.type import WorkOrder, WorkOrderBase


def serialize_datetime(obj: datetime) -> str:
    if isinstance(obj, datetime):
        return obj.strftime("%Y-%m-%d %H:%M:%S")
class WorkOrderAPI(FastAPI):
    def __init__(self) -> None:
        super().__init__()
        self.add_api_route("", self.get_work_orders, methods=["GET"], summary="获取工单")
        self.add_api_route("", self.delete_work_orders, methods=["DELETE"], summary="删除工单")
        self.add_api_route("", self.update_work_orders, methods=["PUT"], summary="更新工单")
        self.add_api_route("", self.create_work_order, methods=["POST"], summary="创建工单")
        self.add_api_route("/get_work_order", self.get_work_order_by_id, methods=["GET"], summary="根据ID获取工单")
        pass

    async def get_work_orders(
        self,
        id: int = Query(None, description="WorkOrder ID"),
        uu_id: str = Query(None, description="WorkOrder UUID"),
        search_criteria: str = Query(None, description="Search criteria"),
        status_filter: str = Query(None, description="Status filter"),
        start_date: str = Query(None, description="Start date"),
        end_date: str = Query(None, description="End date"),
    ) -> Response:
        """_summary_

        Args:\n
            id (int, optional): _description_. Defaults to Query( None, description="WorkOrder ID").\n
            search_criteria (str, optional): _description_. Defaults to Query( None , description="Search criteria").\n
            status_filter (str, optional): _description_. Defaults to Query(None, description="Status filter").\n
            start_date (str, optional): _description_. Defaults to Query(None, description="Start date").\n
            end_date (str, optional): _description_. Defaults to Query(None, description="End date").\n

        Returns:
            Response: _description_
        """
        # 调用相应的方法获取数据
        work_orders: List[WorkOrderBase] = service.get_work_orders_by_filter(
            id, uu_id, search_criteria, status_filter, start_date, end_date
        )
        work_orders_data: list[dict[str, Any]] = [work_order.model_dump() for work_order in work_orders]


        return Response(
            content=json.dumps(work_orders_data, default=serialize_datetime),
            media_type="application/json",
        )

    async def delete_work_orders(
        self, id_list: list[int] = Body(None, description="WorkOrder ID list")
    ) -> Response:
        """_summary_

        Args:
            id_list (list[str], optional): _description_. Defaults to Body( None, description="WorkOrder ID list").

        Returns:
            Response: _description_
        """

        for id in id_list:
            service.delete_work_order(id)
        return Response(status_code=200)

    async def update_work_orders(
        self, work_order: WorkOrder = Body(description="WorkOrder object",example=WorkOrder.config.json_schema_extra["update"])
    ) -> Response:
        service.update_work_order(WorkOrder(**work_order.model_dump()))
        return Response(status_code=200)

    # 创建工单
    # 我需要排除掉一些字段，比如ID，创建时间，更新时间
    
    async def create_work_order(
        self, work_order: WorkOrder = Body(description="WorkOrder object", example=WorkOrder.config.json_schema_extra["example"] )
    ) -> Response:
        service.insert_work_order(work_order )
        return Response(status_code=200)
        pass
    
    async def get_work_order_by_id(self , id:int = Query(1, description="WorkOrder ID")) -> Response:
        work_order:Optional[WorkOrder] = service.get_work_order_by_id(id)
        if work_order is None:
            return Response(status_code=404)
        return Response(content=json.dumps(work_order.model_dump()), media_type="application/json")
        pass
