
import datetime
import sys
sys.path.append("./src")

from utils.table_image import create_table_image


import pandas as pd

from utils.download_file import download_excel_and_read


def get_vehicles_from_url(excel_url:str) -> None:
    # 读取Excel文件
    
    df:pd.DataFrame = download_excel_and_read(excel_url)
    
    df['车牌号码'] = df['车牌号码'].fillna('').astype(str)
    df['车辆组织'] = df['车辆组织'].fillna('').astype(str)
    # 类型为时间
    df['车辆状态（离线/定位）'] = df['车辆状态（离线/定位）'].fillna('').astype(str)
    df['摄像头状态'] = df['摄像头状态'].fillna('').astype(str)
    # 根据某一列的值进行分组
    # 假设我们根据名为"Column_Name"的列来分组
    grouped_data = df.groupby("车辆组织")

    # 遍历每个分组                  
    for name, group in grouped_data:
        print(f"Group: {name}")
        print(group)
        create_table_image(group, title=str(name))
        # for row in group.itertuples():
        #     print(row)
        print("\n")
        

    

if __name__=='__main__':
    vehicle_url= "http://47.116.201.99:8001/test/uploads/d1ce1148370e4ab28c8dc14594d935a1_c4cca99f1c2743bcb016ea80e3f61e87_12.66.xlsx"
    excel_file_path= "http://47.116.201.99:8001/test/uploads/80fcd33050464a439d65e71bdaa54a64_-12-11.xlsx"
    get_vehicles_from_url(vehicle_url)
    pass