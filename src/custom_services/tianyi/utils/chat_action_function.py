
import json
from typing import Any
import requests
import datetime
from enum import Enum
from models.ticket.type import Ticket

from utils import local_logger
from urllib.parse import quote

class ChatActionsEnum(Enum):
    WORK_ORDER_CREATE = r""
    WORK_ORDER_UPDATE = r"工单更新"
    EXECUTE_TASK = r"执行任务"
    OTHER_ACTION = r"其他动作"
    SEND_LOG_FILE = r"发送日志文件"
    
    
class UtilsHelper:
    
    page_url = "http://47.116.201.99:4000/user_chat_page"
    ticket_url = "http://47.116.201.99:4000/test/"
    
    @staticmethod
    def get_tickets_by_filter(input_uuid:str) -> Ticket:
        
        url = 'http://47.103.45.149:25432/ticket'
        params = {
            'uu_id': input_uuid
        }
        headers = {
            'accept': 'application/json'
        }

        response = requests.get(url, params=params, headers=headers)

        print(response.json())  # 打印响应的正文内容
        data = json.loads(response.json())
        ticket = Ticket(**data)
        return ticket
        pass
        
    @staticmethod
    def add_ticket_to_website(ticket_record: Ticket) -> None:
        url = 'http://47.103.45.149:25432/ticket'
        response = requests.post(url, json=ticket_record)
        # 检查响应状态码
        if response.status_code == 200:
            # 如果响应状态码为200，表示成功添加工单
            ticket_info = response.json()
            # print("Success:", ticket_info)
            
            local_logger.logger.info("add_ticket_to_website ticket_info : %s", ticket_info)
            return None
        else:
            # 如果响应状态码不是200，表示添加工单时出现错误
            error_info = response.json()
            local_logger.logger.info ("Error:", error_info)
            return None
    
    @staticmethod
    def add_ticket_init_chat(ticket_record: Ticket, group_message: list[tuple[Any, ...]], sender_name: str) -> None:
        url = f'{UtilsHelper.ticket_url}add_chat_record'
        ticket_id = ticket_record.id
        
        # 生成随机的消息ID、工单ID、发送者、消息内容和消息时间
        message_id = ""
        sender = '系统消息'  
        content = "你好，有什么可以帮你的?可以在此留言"

        message_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
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
                message_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
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
    def get_work_order_link(ticket_id: int, customer_id: str) -> str:
        original_string = customer_id
        encoded_string = quote(original_string, encoding='utf-8')
        return f"@{customer_id}" +'{ENTER}' + f"工单id: {ticket_id}  工单消息通知  {UtilsHelper.page_url}?ticket_id={ticket_id}&customer_id={encoded_string}"
    
    

