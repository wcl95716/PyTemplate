import sys
sys.path.append("./src")


from external.PyOfficeRobot.PyOfficeRobot.core.WeChatType import WeChat
from external.PyOfficeRobot.PyOfficeRobot.api import chat

from utils import local_logger
from utils.download_file import download_file_to_folder
from typing import Any, Callable, List, Tuple


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
    # 获取会话列表
    wx.GetSessionList() # type: ignore 
    wx.ChatWith(who , RollTimes = 1) # type: ignore  # 打开`who`聊天窗口
    # for i in range(10):
    wx.SendMsg(message, who) # type: ignore   # 向`who`发送消息：你好~
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
    wx.ChatWith(who, RollTimes=1)  # type: ignore # 打开`who`聊天窗口
    messages: List[Tuple[str, str, str]] =   wx.GetAllMessage() # type: ignore  # 获取所有消息
    return messages # 获取所有消息
    pass 


def get_robot_name() -> str:
    print("update_robot_name")
    send_name = "文件传输助手"
    
    send_message(who = send_name,  message="测试")
    # PyOfficeRobot.chat.send_message(who=send_name, message="测试")
    
    chat_message  = get_chat_messages(who=send_name)
    print("chat_message "  ,chat_message)
    
    last_message =  chat_message[-1]
    print(f"last_message={last_message}")
    robot_name: str = last_message[0]
    print(f"robot_name={robot_name}")
    return robot_name
    pass

def chat_by_keywords(who:str, keywords:dict[str, Any]) -> None:
    wx.GetSessionList() # type: ignore  # 获取会话列表
    # wx.ChatWith(who) # type: ignore  # 打开`who`聊天窗口 
    wx.Search(who) # type: ignore  # 打开`who`聊天窗口 
    try:
        friend_name, receive_msg = wx.GetAllMessage[-1][0], wx.GetAllMessage[-1][1]  # 获取朋友的名字、发送的信息
        print("receive_msg ",receive_msg)
        # 优化这个代码
        for key in keywords:
            if key in receive_msg:
                tem = keywords[key](who, wx.GetAllMessage[-1],wx.GetAllMessage)
                print("tem",tem)
                if tem is not None:
                    chat.send_message(who=who, message=tem[2])  # type: ignore
                    break

    except:
        pass
    pass