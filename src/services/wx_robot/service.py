import datetime
import os

import poai
import porobot as porobot
import schedule
import hashlib
from external.PyOfficeRobot.PR.Dumogu.WeChatType import WeChat


from utils import local_logger
from utils.download_file import download_file_to_folder
from external.PyOfficeRobot.PR.Dumogu.WeChatType import WeChat


wx: WeChat = WeChat()


def get_group_list () -> list[str]:
    RollTimes = 1
    def roll_to(RollTimes:int = 0 ) -> int:
        for i in range(RollTimes):
            wx.SessionList.WheelUp(wheelTimes=3, waitTime=0.1 * i)
        return 0

    rollresult = roll_to(RollTimes)
    group_list: list[str] = wx.GetSessionList()  # 获取会话列表
    local_logger.logger.info(f" group_list {group_list}")
    return group_list
    pass

def send_message(who:str, message: str) -> None:
    # local_logger.logger.info(who , message)
    wx.GetSessionList()
    wx.ChatWith(who,RollTimes=1)  # 打开`who`聊天窗口
    # for i in range(10):
    wx.SendMsg(message, who)  # 向`who`发送消息：你好~
    pass 

def send_file_from_url(who:str , file_url:str) -> None:
    file_path = download_file_to_folder(file_url)
    """
    发送任意类型的文件
    :param who:
    :param file: 文件路径
    :return:
    """
    wx.ChatWith(who,RollTimes=1)  # 打开聊天窗口
    # wx.SendFiles(file)
    wx.test_SendFiles(filepath=file_path, who=who)  # 添加who参数：雷杰
    pass 


def get_chat_messages(who:str) -> list:
    wx.ChatWith(who,RollTimes=1)  # 打开`who`聊天窗口
    return wx.GetAllMessage # 获取所有消息
    pass 


def update_robot_name() -> str:
    print("update_robot_name")
    send_name = "文件传输助手"
    send_message(who = send_name,  message="测试")
    
    chat_message  = get_chat_messages(who=send_name)
    last_message =  chat_message[-1]
    print(f"last_message={last_message}")
    robot_name = last_message[0]
    print(f"robot_name={robot_name}")
    return robot_name
    pass