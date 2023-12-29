


from datetime import datetime
from typing import Optional
import uuid
from custom.tianyi.utils.chat_action_function import UtilsHelper
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
    
    UtilsHelper.add_ticket_to_website(ticket)
    result_ticket = UtilsHelper.get_tickets_by_filter(input_uuid= ticket.uu_id)

    if result_ticket is None:
        return None

    # UtilsHelper.add_ticket_init_chat(ticket_response, group_messages , message[0])
    res = UtilsHelper.get_work_order_link(result_ticket.id, message[0])
    if result_ticket is not None and res is not None:
        return (group_id, res)
    else:
        return None
    
    
