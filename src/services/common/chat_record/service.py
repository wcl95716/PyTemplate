from models.tables.chat_record.type import ChatRecord, ChatRecordBase
from utils.database_pymysql_util import DatabaseManager

from models.tables.work_order.type import WorkOrder
from utils.database_sqlmodel_util import DatabaseCRUD

# 增加一条记录
def add_chat_record(chat_record: ChatRecord) -> bool:

    return DatabaseCRUD.create(chat_record)
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
