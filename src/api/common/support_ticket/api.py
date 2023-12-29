"""
This module provides the API endpoints for support tickets.
"""
from datetime import datetime
import json
from services.common.support_ticket import service

from unittest.mock import Base

from pydantic import BaseModel


from fastapi import APIRouter, Body, FastAPI, Query, HTTPException, Response
from typing import Any, List, Optional

from models.ticket.type import Ticket



class TicketAPI(FastAPI):
    def __init__(self) -> None:
        super().__init__()
        self.add_api_route("", self.get_tickets, methods=["GET"], summary="获取工单")
        self.add_api_route("", self.delete_tickets, methods=["DELETE"], summary="删除工单")
        self.add_api_route("", self.update_tickets, methods=["PUT"], summary="更新工单")
        self.add_api_route("", self.create_ticket, methods=["POST"], summary="创建工单")
        pass

    async def get_tickets(
        self,
        id: int = Query(None, description="Ticket ID"),
        uu_id: str = Query(None, description="Ticket UUID"),
        search_criteria: str = Query(None, description="Search criteria"),
        status_filter: str = Query(None, description="Status filter"),
        start_date: str = Query(None, description="Start date"),
        end_date: str = Query(None, description="End date"),
    ) -> Response:
        """_summary_

        Args:\n
            id (int, optional): _description_. Defaults to Query( None, description="Ticket ID").\n
            search_criteria (str, optional): _description_. Defaults to Query( None , description="Search criteria").\n
            status_filter (str, optional): _description_. Defaults to Query(None, description="Status filter").\n
            start_date (str, optional): _description_. Defaults to Query(None, description="Start date").\n
            end_date (str, optional): _description_. Defaults to Query(None, description="End date").\n

        Returns:
            Response: _description_
        """
        # 调用相应的方法获取数据
        tickets: List[Ticket] = service.get_tickets_by_filter(
            id, uu_id, search_criteria, status_filter, start_date, end_date
        )
        tickets_data: list[dict[str, Any]] = [ticket.model_dump() for ticket in tickets]
        def serialize_datetime(obj: datetime) -> str:
            if isinstance(obj, datetime):
                return obj.strftime("%Y-%m-%d %H:%M:%S")

        return Response(
            content=json.dumps(tickets_data, default=serialize_datetime),
            media_type="application/json",
        )

    async def delete_tickets(
        self, id_list: list[str] = Body(None, description="Ticket ID list")
    ) -> Response:
        """_summary_

        Args:
            id_list (list[str], optional): _description_. Defaults to Body( None, description="Ticket ID list").

        Returns:
            Response: _description_
        """

        for id in id_list:
            service.delete_ticket(id)
        return Response(status_code=200)

    async def update_tickets(
        self, ticket: Ticket = Body(description="Ticket object")
    ) -> Response:
        service.update_ticket(Ticket(**ticket.dict()))
        return Response(status_code=200)

    # 创建工单
    async def create_ticket(
        self, ticket: Ticket = Body(description="Ticket object")
    ) -> Response:
        print("ticket ", ticket)
        service.insert_ticket(ticket )
        return Response(status_code=200)
        pass
