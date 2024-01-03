from models.tables.chat_record.type import ChatRecord, ChatRecordBase
from utils.database import DatabaseManager

from models.tables.ticket.type import Ticket

# 增加一条记录
def add_chat_record(chat_record: ChatRecordBase) -> bool:
    columns, placeholders, args = DatabaseManager.build_insert_sql_components(chat_record)
    # sql = "INSERT INTO chatrecord (type, content, title, creator_id, assigned_to_id) VALUES (%s, %s, %s, %s, %s)"
    sql = f"INSERT INTO chatrecord ({columns}) VALUES ({placeholders})"
    if DatabaseManager.execute(sql, args):
        return True
    return False
    pass


def get_chat_records_by_creator_id(creator_id: str) -> list[ChatRecordBase]:
    sql = "SELECT * FROM chatrecord WHERE creator_id=%s"
    args = creator_id
    result = DatabaseManager.query_to_dict(sql, args)
    # print("adsasdasd ",result)
    records = []
    if result is None:
        return []
    for row in result:
        # print(row)
        record = ChatRecordBase(**row)
        records.append(record)
        pass
    return records
    pass
