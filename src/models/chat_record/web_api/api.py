"""
This module provides the API endpoints for support tickets.
"""
from datetime import datetime
import json
import sys
sys.path.append("./src")
from unittest.mock import Base

from pydantic import BaseModel
from base_class.ticket.type import Ticket


from models.support_ticket.api import ticket_api

from fastapi import APIRouter, Body, FastAPI, Query, HTTPException, Response
from typing import Any, List, Optional

# 创建一个 APIRouter
# router = APIRouter()


class TicketClass(BaseModel):
    id:Optional[str]
    status:int
    priority:int
    type:int
    title:str 
    content:str 
    assigned_to_id:str
    creator_id:str
    create_time:datetime
    update_time:Optional[datetime]
    pass

class TicketAPI(FastAPI):
    
    def __init__(self) -> None:
        super().__init__()
        self.add_api_route("" ,self.get_tickets , methods=["GET"], summary="获取工单" )
        self.add_api_route("" ,self.delete_tickets , methods=["DELETE"], summary="删除工单" )
        self.add_api_route("" ,self.update_tickets , methods=["PUT"], summary="更新工单" )
        self.add_api_route("" ,self.create_ticket , methods=["POST"], summary="创建工单" )
        pass

    async def get_tickets(
        self,
        id: str = Query( None, description="Ticket ID"),
        search_criteria: str = Query( None , description="Search criteria"),
        status_filter: str = Query(None, description="Status filter"),
        start_date: str = Query(None, description="Start date"),
        end_date: str = Query(None, description="End date"),
    ) -> Response:
        
        """_summary_
        
        Args:\n
            id (str, optional): _description_. Defaults to Query( None, description="Ticket ID").\n
            search_criteria (str, optional): _description_. Defaults to Query( None , description="Search criteria").\n
            status_filter (str, optional): _description_. Defaults to Query(None, description="Status filter").\n
            start_date (str, optional): _description_. Defaults to Query(None, description="Start date").\n
            end_date (str, optional): _description_. Defaults to Query(None, description="End date").\n

        Returns:
            Response: _description_
        """
        # 调用相应的方法获取数据
        tickets = ticket_api.get_tickets_by_filter(id, search_criteria, status_filter, start_date, end_date)
        tickets_data:list[dict[str, Any]] = [ticket.to_dict() for ticket in tickets]
        def serialize_datetime(obj: datetime) -> str:
            if isinstance(obj, datetime):
                return obj.strftime("%Y-%m-%d %H:%M:%S")
        return Response(content=json.dumps(tickets_data,default=serialize_datetime ), media_type="application/json")

    
    async def delete_tickets(self, 
                       id_list:list[str] = Body( None, description="Ticket ID list")
                       ) -> Response:
        """_summary_

        Args:
            id_list (list[str], optional): _description_. Defaults to Body( None, description="Ticket ID list").

        Returns:
            Response: _description_
        """
        
        for id in id_list:
            ticket_api.delete_ticket(id)
        return Response(status_code=204)
    
    async def update_tickets(self, 
                          ticket:TicketClass = Body(description="Ticket object")
                       ) -> Response:
        
        ticket_api.update_ticket(Ticket(**ticket.dict()))
        return Response(status_code=204)

    
    # 创建工单
    async def create_ticket(self, 
                      ticket:TicketClass = Body(description="Ticket object")
                      ) -> Response:
        ticket_api.insert_ticket(
            status=ticket.status,  # Add the missing "status" argument
            priority=ticket.priority,
            type=ticket.type,
            title=ticket.title,
            content=ticket.content,
            assigned_to_id=ticket.assigned_to_id,
            creator_id=ticket.creator_id,
            create_time=ticket.create_time
        )
        return Response(status_code=201)
        pass


