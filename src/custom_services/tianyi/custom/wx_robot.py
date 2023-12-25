import sys
sys.path.append("./src")

# 读取群聊列表
# 从excel中读取群聊列表

import time
from typing import Any
import pandas as pd

from custom_services.tianyi.utils.functions import work_order_create
from services.wx_robot.service import chat_by_keywords, get_chat_group_list, get_robot_name

from utils import local_logger


def get_group_list_from_excel() -> list[str]:
    try:
        df = pd.read_excel("data/微信服务群.xlsx", engine='openpyxl')
        print(df)
        result = []
        for index, row in df.iterrows():
            # 微信服务群名称
            group_name = row['微信服务群名称']
            result.append(group_name)

        # 使用set去除重复数据，然后再转回列表
        unique_group_list = list(set(result))
        return unique_group_list
    except Exception as e:
        local_logger.logger.info(f"读取群聊列表时发生错误：{str(e)}")
        return []


def process_one_group_tasks(process_group:str,group_list:list[str],robot_keywords_config:Any ) -> None:
    for group in group_list:
        if process_group.startswith(group) == False:
            continue
        chat_by_keywords(who=group, keywords=robot_keywords_config)
        pass
    pass

def chec_groups(group_list: list[str],robot_keywords_config:Any) -> None:
    chat_groups = get_chat_group_list()[:3]
    for group in chat_groups:
        process_one_group_tasks(group,group_list,robot_keywords_config)
    pass     

def groups_check() -> None:
    robot_name = get_robot_name()

    robot_keywords_config = {
        f"@{robot_name}": work_order_create,
    }
    group_list = []
    group_list = get_group_list_from_excel()
    group_list.append("测试3群")
    
    while True:
        chec_groups(group_list,robot_keywords_config)
        time.sleep(1)
    
    
    pass


if __name__ == "__main__":
    groups_check()
    pass