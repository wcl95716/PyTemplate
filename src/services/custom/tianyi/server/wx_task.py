
import datetime
import sys
sys.path.append("./src")

from models.priority.type import PriorityEnum

from models.company.type import CompanyEnum


from typing import Any, Optional

import requests
from models.record.type import RecordEnum
from models.status.type import StatusEnum
from models.notification_task.type import NotificationEnum, NotificationTask

from services.common.notification_task.service import insert_notification


from utils import table_image


import pandas as pd

from utils.download_file import download_excel_and_read


# 生成任务
def get_notification_task(car_group_name:str, wx_group_name:str ,car_status_content:str  ) -> NotificationTask:
    car_status_task = NotificationTask(
        notification_type=NotificationEnum.WECHAT,
        destination={"group_name": wx_group_name},
        title=car_group_name,
        content=car_status_content,
        priority=PriorityEnum.NORMAL,
        status=StatusEnum.NEW,
        type=RecordEnum.TEXT,
        creator_id="",
        assigned_to_id=wx_group_name,
        create_time=datetime.datetime.now(),
        update_time=datetime.datetime.now(),
        company_id = CompanyEnum.TIAN_YI,
    ) 
    return car_status_task
    pass 

# 从url中获取文件
def get_file_from_url(excel_url:str) -> pd.DataFrame:
    # 读取Excel文件
    df:pd.DataFrame = download_excel_and_read(excel_url)
    
    # 遍历所有列，填充空值并转换为字符串
    for column in df.columns:
        df[column] = df[column].fillna('').astype(str)
    return df


# 从规则表中获取车辆组织对应的行
def get_wxgroup_name(group_name:str, rule_df: pd.DataFrame ) ->  Optional[pd.Series] : # type: ignore 
    # 获取符合条件的DataFrame
    matching_rows = rule_df[rule_df['车辆组织'] == group_name]
    # 检查结果是否为空
    if not matching_rows.empty:
        first_matching_row = matching_rows.iloc[0]
        return first_matching_row
        # 进行后续操作...
    else:
        print(f"没有找到匹配车辆组织为 '{group_name}' 的行")
        # 或进行其他适当的处理...
    return None
    pass 

# 上传文件
def upload_file(file_path:str) -> Optional[str]:
    url = 'http://47.116.201.99:8001/test/upload_file'
    files = {'file': open(file_path, 'rb')}
    response = requests.post(url, files=files)
    
    # 检查响应状态码是否为 200，表示请求成功
    if response.status_code == 200:
        # 使用 response.json() 方法解析返回的 JSON 数据
        json_data = response.json()
        
        # 获取 file_url 字段的值
        file_url:Optional[str] = json_data.get('file_url', None)
        
        if file_url:
            return file_url
        else:
            print("File URL not found in the JSON response.")
            return None
    else:
        print(f"Request failed with status code: {response.status_code}")
        return None
    

# 生成车辆组织的任务
def get_group_task(car_group_name:str, rule_df: pd.DataFrame, group: pd.DataFrame ) -> list[NotificationTask]:
    
    rule_line = get_wxgroup_name(str(car_group_name),rule_df)
    if rule_line is None:
        return []
    
    result_task:list[NotificationTask] = []
    wx_group_name:str = str(rule_line["微信服务群名称"])
    
    car_status = []
    camera_status = []
    for index, row in group.iterrows():
        if row["车辆状态（离线/定位）"] != "":
            car_status.append(row["车牌号码"])
        if row["摄像头状态"] != "":
            camera_status.append(row["车牌号码"])
        
    # 1 生成车辆状态的任务
    car_status_content = "车辆组织: " + car_group_name + '{ctrl}{ENTER}'  + "车牌号码: " + ",".join(car_status)+'{ctrl}{ENTER}' + rule_line["车辆状态（离线/定位）"]
    car_status_task = get_notification_task(car_group_name, wx_group_name, car_status_content)
    if len(car_status) > 0:
        result_task.append(car_status_task)
    
    # 2 生成摄像头状态的任务
    camera_status_content = "车辆组织: " + car_group_name + '{ctrl}{ENTER}'  + "车牌号码: " + ",".join(camera_status)+ '{ctrl}{ENTER}' + rule_line["摄像头状态"]
    camera_status_task = get_notification_task(car_group_name, wx_group_name, camera_status_content)
    
    if len(camera_status) > 0:
        result_task.append(camera_status_task)
        
    
    # 3 生成表格任务
    # file_path = table_image.create_table_image(group, title=str(car_group_name),file_name=car_group_name+".png")
    # file_url = upload_file(file_path)
    # # file_task
    # if file_url:
    #     file_task = get_notification_task(car_group_name, wx_group_name, file_url)
    #     result_task.append(file_task)
    return result_task
    pass 


# 生成任务
def task_creat(vehicle_url: str, rule_url: str) -> None:
    vehicle_df = get_file_from_url(vehicle_url)
    rule_df = get_file_from_url(rule_url)
    
    group_vehicle_df = vehicle_df.groupby("车辆组织")
    
    tasks:list[NotificationTask] = []
    # 遍历每个分组                  
    for car_group_name, group in group_vehicle_df:
        tasks.extend(get_group_task(str(car_group_name), rule_df, group) )
        
    for task in tasks:
        print(task)
        insert_notification(task)
    pass

    

if __name__=='__main__':
    vehicle_url= "http://47.116.201.99:8001/test/uploads/d1ce1148370e4ab28c8dc14594d935a1_c4cca99f1c2743bcb016ea80e3f61e87_12.66.xlsx"
    excel_file_path= "http://47.116.201.99:8001/test/uploads/80fcd33050464a439d65e71bdaa54a64_-12-11.xlsx"
    # get_vehicles_from_url(vehicle_url)
    task_creat(vehicle_url,excel_file_path)
    pass