import datetime
import os
import schedule
from external.PyOfficeRobot.PR.Dumogu.WeChatType import WeChat


from utils import local_logger
from utils.download_file import download_file_to_folder
from typing import Callable, List, Tuple
from external.PyOfficeRobot.PR.Dumogu.WeChatType import WeChat
from external.PyOfficeRobot import PyOfficeRobot 



# type: ignore 
wx: WeChat = WeChat() # type: ignore 


def get_chat_group_list () -> list[str]:
    RollTimes = 1
    def roll_to(RollTimes:int = 0 ) -> int:
        for i in range(RollTimes):
            wx.SessionList.WheelUp(wheelTimes=3, waitTime=0.1 * i)
        return 0

    rollresult = roll_to(RollTimes)
    group_list: list[str] = wx.GetSessionList()  # type: ignore 
    local_logger.logger.info(f" group_list {group_list}")
    return group_list
    pass

# type: ignore 
def send_message(who:str, message: str) -> None:
    wx.GetSessionList()    # type: ignore
    wx.ChatWith(who,RollTimes=1)  # type: ignore # 打开`who`聊天窗口
    # for i in range(10):
    wx.SendMsg(message, who)  # type: ignore # 向`who`发送消息：你好~
    pass 


# 发送文件
def send_file_from_url(who:str , file_url:str) -> None:
    file_path = download_file_to_folder(file_url)
    """
    发送任意类型的文件
    :param who:
    :param file: 文件路径
    :return:
    """
    wx.ChatWith(who,RollTimes=1)  # type: ignore # 打开聊天窗口
    # wx.SendFiles(file)
    wx.SendFiles(file_path)  # type: ignore # 添加who参数：雷杰
    pass 


def get_chat_messages(who:str) -> List[Tuple[str, str, str]]:
    messages: List[Tuple[str, str, str]] =  wx.ChatWith(who, RollTimes=1)  # type: ignore # 打开`who`聊天窗口
    return messages # 获取所有消息
    pass 


def get_robot_name() -> str:
    print("update_robot_name")
    send_name = "文件传输助手"
    send_message(who = send_name,  message="测试")
    
    chat_message  = get_chat_messages(who=send_name)
    last_message =  chat_message[-1]
    print(f"last_message={last_message}")
    robot_name: str = last_message[0]
    print(f"robot_name={robot_name}")
    return robot_name
    pass

def chat_by_keywords(who:str, keywords:dict[str,Callable[[Tuple[str, str, str]], str]]) -> None:
    wx.GetSessionList() # type: ignore  # 获取会话列表
    wx.ChatWith(who) # type: ignore  # 打开`who`聊天窗口 
    try:
        friend_name, receive_msg = wx.GetAllMessage[-1][0], wx.GetAllMessage[-1][1]  # 获取朋友的名字、发送的信息
        # 优化这个代码
        for key in keywords:
            if key in receive_msg :
                send_message(who=who, message=keywords[key](receive_msg))
                break

    except:
        pass
    pass