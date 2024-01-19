


from datetime import datetime
from typing import Optional
import uuid
from services.custom.tianyi.utils.chat_action_function import UtilsHelper
from models.common.record.type import RecordEnum
from models.tables.work_order.type import WorkOrder



def work_order_create(group_id:str, message: Optional[tuple[str,str,str]],group_messages:list[tuple[str,str,str]] ) -> Optional[tuple[str,str]]:
    # 编写创建工单的操作逻辑
    if message is None:
        return None

    work_order:WorkOrder = WorkOrder(
        type= RecordEnum.TEXT,
        content="",
        title= group_id+ " " +  message[0],
        creator_id = group_id +"/"+ message[0],
        assigned_to_id=""
    )
    
    UtilsHelper.add_work_order_to_website(work_order)
    result_work_order = UtilsHelper.get_work_orders_by_filter(input_uuid= work_order.uu_id)

    if result_work_order is None:
        return None

    # UtilsHelper.add_work_order_init_chat(work_order_response, group_messages , message[0])
    res = UtilsHelper.get_work_order_link(result_work_order.id, message[0])
    if result_work_order is not None and res is not None:
        return (group_id, res)
    else:
        return None
    
    
