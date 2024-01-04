import sys

from api.common.work_order.client_api import WorkOrderClient
from models.common.record.type import RecordEnum
from models.tables.work_order.type import WorkOrder
sys.path.append("./src")

import json
from typing import Any, Optional
from enum import Enum
import requests
from utils import local_logger
from urllib.parse import quote
from datetime import datetime

class ChatActionsEnum(Enum):
    WORK_ORDER_CREATE = r""
    WORK_ORDER_UPDATE = r"工单更新"
    EXECUTE_TASK = r"执行任务"
    OTHER_ACTION = r"其他动作"
    SEND_LOG_FILE = r"发送日志文件"
    
    
class UtilsHelper:
    
    page_url = "http://47.116.201.99:4000/user_chat_page"
    ticket_url = "http://47.116.201.99:4000/test/"
    # web_api = "http://47.103.45.149:25432/work_order"
    web_api = "http://127.0.0.1:25432"
    @staticmethod
    def get_tickets_by_filter(input_uuid: Optional[str]) -> Optional[WorkOrder]:
        ticket_client = WorkOrderClient(UtilsHelper.web_api)
        res: list[WorkOrder] = ticket_client.get_tickets(uu_id=input_uuid)
        if len(res) == 0:
            return None
        return res[0]
        pass
        
    @staticmethod
    def add_ticket_to_website(ticket_record: WorkOrder) -> bool:

        ticket_client = WorkOrderClient(UtilsHelper.web_api)
        res = ticket_client.create_ticket(ticket_record)
        return res == 200
    
    @staticmethod
    def add_ticket_init_chat(ticket_record: WorkOrder, group_message: list[tuple[Any, ...]], sender_name: str) -> None:
        url = f'{UtilsHelper.ticket_url}add_chat_record'
        ticket_id = ticket_record.id
        
        # 生成随机的消息ID、工单ID、发送者、消息内容和消息时间
        message_id = ""
        sender = '系统消息'  
        content = "你好，有什么可以帮你的?可以在此留言"

        message_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message_type = 0

        chatMessage = {
            "message_id": message_id,
            "ticket_id": ticket_id,
            "sender": sender,
            "content": content,
            "message_time": message_time,
            "message_type": message_type,
            "chat_profile": 1001,
            "avatar_url": "http://47.116.201.99:8001/test/uploads/79cd180e87d345be9fd60123183fec4a_16211702261434_.pic.jpg",
        }
        response = requests.post(url, json=chatMessage)
        if group_message is None:
            return
        num_messages = len(group_message)
        # 设置要取的最后十条消息的数量
        num_to_keep = 5
        last_ten_messages = group_message[-num_to_keep:] if num_messages >= num_to_keep else group_message

        try:
            for message in last_ten_messages:
                message_id = ""
                sender = message[0]  
                if sender != sender_name:
                    continue  
                    
                content = message[1]
                message_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                message_type = 0
                chatMessage = {
                    "message_id": message_id,
                    "ticket_id": ticket_id,
                    "sender": sender,
                    "content": content,
                    "message_time": message_time,
                    "message_type": message_type,
                    "chat_profile": 1000,
                    "avatar_url": "http://47.116.201.99:8001/test/uploads/94645ce7df1b4fcb8123f93b040dbcb1_617e9a689d4bc7779c46e2ab93791df.png"
                }
                response = requests.post(url, json=chatMessage)
                pass
        except Exception as e:
            local_logger.logger.info("add_ticket_init_chat error : %s", str(e))
            pass
            
    
    @staticmethod
    def get_work_order_link(ticket_id: Optional[int], customer_id: str) -> Optional[str]:
        if ticket_id is None:
            return None
        original_string = customer_id
        encoded_string = quote(original_string, encoding='utf-8')
        return f"@{customer_id}" +'{ENTER}' + f"工单id: {ticket_id}  工单消息通知  {UtilsHelper.page_url}?ticket_id={ticket_id}&customer_id={encoded_string}"
    
    

# 测试 add_ticket_to_website
def test() ->None:
    work_order:WorkOrder = WorkOrder(
        type= RecordEnum.TEXT,
        content="",
        title= "6666666666",
        creator_id = "adsasdasdasd",
        assigned_to_id="",
    )
    # print("work_order ",work_order.dict())
    # UtilsHelper.add_ticket_to_website(work_order)
    asd =  UtilsHelper.get_tickets_by_filter(input_uuid="810a034c-f425-4eb7-985c-3b80f5f76548")
    print("asd ",asd)
    pass


if __name__ == '__main__':
    test()
    pass