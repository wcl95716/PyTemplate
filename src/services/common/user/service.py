

# src/models/user/type.py 根据这个类型
# 仿照 src/services/common/chat_record/service.py 内部的写法
# 实现user 的增删改查 


from typing import Optional
from models.common.company_info.type import CompanyInfoFilterEnum
from models.tables.user.type import User, UserFilterParams
from utils.database_pymysql_util import DatabaseManager
from utils.database_sqlmodel_util import DatabaseCRUD


# 添加
def  add_user(user: User) -> bool:
    
    find_user = get_users_by_filter( UserFilterParams(phone=user.phone) )
    print("find_user: ",len(find_user))
    if len(find_user) > 0:
        return False
    
    return DatabaseCRUD.create(user)


def update(user: User) -> bool:
    return DatabaseCRUD.update(user)
    
# 获取用户 
# 添加过滤条件
# 手机号 , 邮箱 , 用户名 , 用户类型 , 用户状态 , 创建时间 , 更新时间
def get_users_by_filter(
        user_filter:UserFilterParams
    ) -> list[User]:
    sql = "SELECT * FROM user WHERE 1=1"
    args = []
    print("user_filter: ",user_filter)
    # name 为模糊搜索
    if user_filter.name:
        sql += " AND name LIKE %s"
        args.append(f"%{user_filter.name}%")
        
    # phone 为模糊搜索
    if user_filter.phone:
        sql += " AND phone LIKE %s"
        args.append(f"%{user_filter.phone}%")
        
    # email 为模糊搜索
    if user_filter.email:
        sql += " AND email LIKE %s"
        args.append(f"%{user_filter.email}%")
    
    # company_id 精确搜索
    if user_filter.company_id != CompanyInfoFilterEnum.NONE \
        and user_filter.company_id != CompanyInfoFilterEnum.NoneValue:
        sql += " AND company_id = %s"  # Convert to string
        args.append(str(user_filter.company_id.value))  # Convert to string
        
    # company_name 模糊搜索
    if user_filter.company_name:
        sql += " AND company_name LIKE %s"
        args.append(f"%{user_filter.company_name}%")
        
    # id 精确搜索
    if user_filter.id:
        sql += " AND id = %s"  # Convert to string
        args.append(str(user_filter.id))  # Convert to string
        
    # 执行查询
    res =  DatabaseManager.query_to_dict(sql, args)

    users:list[User] = []
    for row in res:
        # print(row)
        user = User(**row)
        users.append(user)
    
    return users
    pass