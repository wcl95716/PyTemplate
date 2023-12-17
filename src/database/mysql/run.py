import pymysql
import os
import subprocess

from typing import Any

from pymysql.connections import Connection

import sys
sys.path.append("./src")

from utils.database import DatabaseManager

def main() -> None:
    sql_folder = 'src/database/tables'
    database_name = "global_data"

    # 创建数据库（如果不存在）
    DatabaseManager.create_database_if_not_exists(database_name)

    # 执行 SQL 文件
    for filename in os.listdir(sql_folder):
        if filename.endswith('.sql'):
            filepath = os.path.join(sql_folder, filename)
            DatabaseManager.execute_sql_file(database_name, filepath)

            
if __name__ == '__main__':
    main()
