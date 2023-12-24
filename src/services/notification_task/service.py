# 导入 FastAPI 实例
import json
import sys
sys.path.append("./src")

from models.notification_task.type import NotificationTask
from utils.database import DatabaseManager

table_name = "notification_task"

# 增加一条记录
def insert_notification(task: NotificationTask) -> bool:
    # 获取对象的所有属性及其值
    attrs = vars(task)
    
    # 特别处理 'destination' 字段，将其转换为 JSON 字符串
    if isinstance(attrs.get('destination'), dict):
        attrs['destination'] = json.dumps(attrs['destination'])

    # 构建列名和占位符
    columns = ', '.join(attrs.keys())
    placeholders = ', '.join(['%s'] * len(attrs))

    # 构建SQL语句
    sql = f"INSERT INTO {table_name}  ({columns}) VALUES ({placeholders})"
    # 构建参数元组
    args = tuple(attrs.values())
    
    if DatabaseManager.execute(sql, args):
        return True
    return False
    pass


# def get_tasks(id:str ) -> list[NotificationTask]:
#     sql = "SELECT * FROM {table_name}  WHERE creator_id=%s"
#     args = creator_id
#     result = DatabaseManager.query_to_dict(sql, args)
#     # print("adsasdasd ",result)
#     records = []
#     if result is None:
#         return []
#     for row in result:
#         # print(row)
#         record = ChatRecord(**row)
#         records.append(record)
#         pass
#     return records
#     pass
