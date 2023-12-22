import sys
sys.path.append("./src")
from models.chat_record.type import ChatRecord
from utils.database import DatabaseManager

from models.ticket.type import Ticket

# src/db/tables/chat_record.sql
# 根据这个表创建增删改查的接口
# CREATE TABLE IF NOT EXISTS chat_records (
#     id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
#     type INT NOT NULL,
#     content TEXT NOT NULL,
#     title VARCHAR(255),
#     creator_id VARCHAR(255) NOT NULL,
#     assigned_to_id VARCHAR(255),
#     create_time TIMESTAMP NOT NULL,
#     update_time TIMESTAMP,
#     INDEX idx_creator_id (creator_id),
#     INDEX idx_assigned_to_id (assigned_to_id),
#     INDEX idx_create_time (create_time),
#     INDEX idx_type (type)
# ) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

# 增加一条记录
def insert_chat_record(chat_record:ChatRecord) -> bool:
    sql = "INSERT INTO chat_record (type, content, title, creator_id, assigned_to_id, create_time) VALUES (%s, %s, %s, %s, %s, %s)"
    args = (chat_record.type, chat_record.content, chat_record.title, chat_record.creator_id, chat_record.assigned_to_id, chat_record.create_time)
    if DatabaseManager.execute(sql, args):
        return True
    return False
    pass

def get_chat_records_by_creator_id(creator_id:str) -> list[ChatRecord]:
    sql = "SELECT * FROM chat_records WHERE creator_id=%s"
    args = (creator_id)
    result = DatabaseManager.query_to_dict(sql, args)
    # print("adsasdasd ",result)
    records = []
    if result is None:
        return []
    for row in result:
        # print(row)
        record = ChatRecord(**row)
        records.append(record)
        pass
    return records
    pass


