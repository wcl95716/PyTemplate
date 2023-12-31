from models.chat_record.type import ChatRecord
from utils.database import DatabaseManager

from models.ticket.type import Ticket

# 增加一条记录
def add_chat_record(chat_record: ChatRecord) -> bool:
    columns, placeholders, args = DatabaseManager.build_insert_sql_components(chat_record)
    # sql = "INSERT INTO chat_record (type, content, title, creator_id, assigned_to_id) VALUES (%s, %s, %s, %s, %s)"
    sql = f"INSERT INTO chat_record ({columns}) VALUES ({placeholders})"
    if DatabaseManager.execute(sql, args):
        return True
    return False
    pass


def get_chat_records_by_creator_id(creator_id: str) -> list[ChatRecord]:
    sql = "SELECT * FROM chat_record WHERE creator_id=%s"
    args = creator_id
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
