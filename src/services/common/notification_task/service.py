# 导入 FastAPI 实例
import json
import sys

from utils.database_sqlmodel_util import DatabaseCRUD
sys.path.append("./src")

from models.tables.notification_task.type import NotificationTaskBase, NotificationTaskFilterParams
from utils.database_pymysql_util import DatabaseManager

table_name = "notificationtask"

# 增加一条记录
def insert_notification(task: NotificationTaskBase) -> bool:
    return DatabaseCRUD.create(task)
    pass

# 根据NotificationTaskFilterParams 过滤条件查询
# like get_users_by_filter
def query_notification_task_by_filter_params(filter_params: NotificationTaskFilterParams) -> list[NotificationTaskBase]:
    
    sql1, args1 = filter_params.build_sql_query()
    sql = f"SELECT * FROM {table_name} WHERE 1=1 "
    sql += sql1
    
    args = []
    args.extend(args1)
    
    print("sql ",sql)
    print("args ",args)
    
    res = DatabaseManager.query_to_dict(sql, args)
    
    tasks:list[NotificationTaskBase] = []
    for row in res:
        print("row ",row)
        task = NotificationTaskBase(**row)
        tasks.append(task)
        pass
    return tasks
    pass

