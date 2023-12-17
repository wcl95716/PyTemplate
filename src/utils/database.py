import subprocess
import pymysql
from pymysql.connections import Connection
from dbutils.pooled_db import PooledDB
from typing import Optional, Any, ClassVar

class DatabaseManager:
    _instance: ClassVar[Optional['DatabaseManager']] = None

    def __new__(cls, *args: Any, **kwargs: Any) -> 'DatabaseManager':
        if cls._instance is None:
            cls._instance = super(DatabaseManager, cls).__new__(cls)
        return cls._instance
    
    def __init__(self, host: str, port: int, user: str, password: str, db: str) -> None:
        self.pool: PooledDB = PooledDB(
            creator=pymysql,
            maxconnections=8,
            host=host,
            port=port,
            user=user,
            password=password,
            database=db,
            charset='utf8mb4'
        )

    @classmethod
    def init(cls, host: str, port: int, user: str, password: str, db: str) -> None:
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            cls.__init__(cls._instance, host, port, user, password, db)
            
    @classmethod
    def _get_instance(cls) -> 'DatabaseManager':
        if cls._instance is None:
            raise Exception("DatabaseManager has not been initialized")
        return cls._instance

    @classmethod
    def query(cls, sql: str, args: Optional[Any] = None) -> Any:
        instance = cls._get_instance()
        conn = instance.pool.connection()
        cursor = conn.cursor()
        try:
            cursor.execute(sql, args or ())
            result = cursor.fetchall()
            conn.commit()
            return result
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def execute(cls, sql: str, args: Optional[Any] = None) -> None:
        instance = cls._get_instance()
        conn = instance.pool.connection()
        cursor = conn.cursor()
        try:
            cursor.execute(sql, args or ())
            conn.commit()
        finally:
            cursor.close()
            conn.close()
            
            
    @classmethod
    def create_database_if_not_exists(cls, database_name: str) -> None:
        instance = cls._get_instance()
        conn = instance.pool.connection()
        try:
            with conn.cursor() as cursor:
                sql_check_db = f"SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = '{database_name}'"
                cursor.execute(sql_check_db)
                if not cursor.fetchone():
                    sql_create_db = f"CREATE DATABASE `{database_name}`"
                    cursor.execute(sql_create_db)
                    conn.commit()
        finally:
            conn.close()  # 确保在结束时关闭连接


    @classmethod
    def execute_sql_file(cls, database_name: str, file_path: str) -> None:
        instance = cls._get_instance()
        command = f"mysql -u {instance.pool._kwargs['user']} -p{instance.pool._kwargs['password']} -h {instance.pool._kwargs['host']} {database_name} < {file_path}"
        subprocess.run(command, shell=True)


# 初始化单例
DatabaseManager.init('localhost', 3306, 'root', '12345678', 'global_data')

# # 示例使用
# try:
#     DatabaseManager.init('localhost', 3306, 'root', '12345678', 'global_data')
#     # ... 进行数据库操作 ...
# except Exception as e:
#     logging.error(f"Database error: {e}")

# 查询
#result = DatabaseManager.query("SELECT * FROM some_table")

# 其他数据库操作...
