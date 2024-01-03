

# src/models/user/type.py 根据这个类型
# 仿照 src/services/common/chat_record/service.py 内部的写法
# 实现user 的增删改查 


from models.tables.user.type import User
from utils.database import DatabaseManager


# 添加
def  add_user(user: User) -> bool:
    columns, placeholders, args = DatabaseManager.build_insert_sql_components(user)
    # sql = "INSERT INTO chat_record (type, content, title, creator_id, assigned_to_id) VALUES (%s, %s, %s, %s, %s)"
    sql = f"INSERT INTO user ({columns}) VALUES ({placeholders})"
    if DatabaseManager.execute(sql, args):
        return True
    return False
    pass
    
# 获取用户 
# 添加过滤条件

def get_users_by_filter(
    
    ) -> None:
    
    
    pass