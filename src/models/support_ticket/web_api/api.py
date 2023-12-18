"""
This module provides the API endpoints for support tickets.
"""
from fastapi import FastAPI, Query, HTTPException, APIRouter
from typing import List

# 创建一个 APIRouter
router = APIRouter()





# 将路由添加到 router 中
@router.get("/tickets", response_model=List[dict])
def get(self,
        id:str,
        search_criteria:str,
        status_filter:str,
        start_date:str,
        end_date:str
        ) -> Response:

    # 调用相应的方法获取数据
    tickets = ticket.get_tickets_by_filter(id, search_criteria, status_filter, start_date, end_date)

    # Convert Ticket objects to serializable format
    tickets_data = [ticket.to_dict() for ticket in tickets]

    return {'message': 'Data retrieved successfully', 'data': tickets_data}


    def delete(self) -> Response:
        """
        Delete a ticket by ID.
        """
        id = request.args.get('id')
        if ticket.delete_ticket(id):
            return {'message': 'Ticket deleted successfully', 'data': []}
        else:
            return {'message': 'Failed to delete ticket', 'data': []}


