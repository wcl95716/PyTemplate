# 导入 FastAPI 实例
import json
import sys

from utils.database_crud import DatabaseCRUD
sys.path.append("./src")

from models.tables.notification_task.type import NotificationTaskBase, NotificationTaskFilterParams
from utils.database import DatabaseManager

table_name = "notificationtask"

# 增加一条记录
def insert_notification(task: NotificationTaskBase) -> bool:
    return DatabaseCRUD.create(task)
    pass

# 根据NotificationTaskFilterParams 过滤条件查询
# like get_users_by_filter
def query_notification_task_by_filter_params(filter_params: NotificationTaskFilterParams) -> list[NotificationTaskBase]:
    
    sql1, args1 = filter_params.build_sql_query()
    sql = f"SELECT * FROM {table_name} WHERE 1=1"
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


# # 根据NotificationTaskFilterParams 过滤条件查询
# # like get_users_by_filter
# def query_notification_task_by_filter_params(filter_params: NotificationTaskFilterParams) -> list[NotificationTaskBase]:
#     sql = f"SELECT * FROM {table_name} WHERE 1=1"
#     args = []
#     if filter_params.assigned_to_id is not None:
#         sql += " AND assigned_to_id = %s"
#         args.append(filter_params.assigned_to_id)
    
#     if filter_params.creator_id is not None:
#         sql += " AND creator_id = %s"
#         args.append(filter_params.creator_id)
    
    
#     if filter_params.id is not None:
#         sql += " AND id = %s"
#         args.append(str(filter_params.id))
    
#     if filter_params.notification_type is not None and filter_params.notification_type.value is not None:
#         sql += " AND notification_type = %s"
#         args.append(str(filter_params.notification_type.value))
        
#     if filter_params.priority is not None:
#         sql += " AND priority = %s"
#         args.append(str(filter_params.priority.value))

#     if filter_params.status is not None:
#         sql += " AND status = %s"
#         args.append(str(filter_params.status.value))
        
    
#     # 模糊搜索
#     if filter_params.title is not None:
#         sql += " AND title LIKE %s"
#         args.append(filter_params.title)
    
#     if filter_params.record_type is not None:
#         sql += " AND type = %s"
#         args.append(str(filter_params.record_type.value))
        
#     if filter_params.content is not None:
#         sql += " AND content LIKE %s"
#         args.append(filter_params.content)
    
#     if filter_params.start_date and filter_params.end_date:
#         sql += " AND create_time BETWEEN %s AND %s"
#         args.append(str(filter_params.start_date))
#         args.append(str(filter_params.end_date))
        
    
#     res = DatabaseManager.query_to_dict(sql, args)
    
#     tasks:list[NotificationTaskBase] = []
#     for row in res:
#         print("row ",row)
#         task = NotificationTaskBase(**row)
#         tasks.append(task)
#         pass
#     return tasks
#     pass
