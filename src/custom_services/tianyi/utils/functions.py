


from datetime import datetime
from typing import Optional
import uuid
from custom_services.tianyi.utils.chat_action_function import UtilsHelper
from models.priority.type import PriorityEnum
from models.record.type import RecordEnum
from models.status.type import StatusEnum

from models.ticket.type import Ticket



def work_order_create(group_id:str, message: Optional[tuple[str,str,str]],group_messages:list[tuple[str,str,str]] ) -> Optional[tuple[str,str]]:
    # 编写创建工单的操作逻辑
    if message is None:
        return None

    ticket:Ticket = Ticket(
        type= RecordEnum.TEXT,
        content="",
        title= group_id+ " " +  message[0],
        creator_id = group_id +"/"+ message[0],
        assigned_to_id=""
    )
    
    print("ticket ",ticket)
    UtilsHelper.add_ticket_to_website(ticket)
    print("ticket1 ")
    result_ticket = UtilsHelper.get_tickets_by_filter(input_uuid= ticket.uu_id)
    # result_ticket = ticket
    print("ticket2 ", result_ticket.model_dump())
    if result_ticket is None:
        return None
    print("ticket3 ",result_ticket.model_dump_json())

    # UtilsHelper.add_ticket_init_chat(ticket_response, group_messages , message[0])
    result = (group_id, UtilsHelper.get_work_order_link(result_ticket.id, message[0]))
    print("result " , result)
    if result_ticket is not None:
        return (group_id, UtilsHelper.get_work_order_link(result_ticket.id, message[0]))
    else:
        return None
    
    
