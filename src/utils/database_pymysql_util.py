import json
import subprocess
from pydantic import BaseModel
import pymysql
from dbutils.pooled_db import PooledDB
from typing import Optional, Any, ClassVar


class DatabaseManager:
    _instance: ClassVar[Optional["DatabaseManager"]] = None

    def __new__(cls, *args: Any, **kwargs: Any) -> "DatabaseManager":
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
            charset="utf8mb4",
            init_command="SET time_zone='Asia/Shanghai'",
        )

    @classmethod
    def init(cls, host: str, port: int, user: str, password: str, db: str) -> None:
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            cls.__init__(cls._instance, host, port, user, password, db)
            cls._get_instance().create_database_if_not_exists(db)

    @classmethod
    def _get_instance(cls) -> "DatabaseManager":
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
    def query_to_dict(
        cls, sql: str, args: Optional[Any] = None
    ) -> list[dict[str, Any]]:
        instance = cls._get_instance()
        conn = instance.pool.connection()
        # 使用 DictCursor 以便结果以字典形式返回
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        try:
            cursor.execute(sql, args or ())
            result: list[dict[str, Any]] = cursor.fetchall()
            return result
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def execute(cls, sql: str, args: Optional[Any] = None) -> bool:
        instance = cls._get_instance()
        conn = instance.pool.connection()
        cursor = conn.cursor()
        try:
            cursor.execute(sql, args or ())
            conn.commit()
            print(f"Successfully executed SQL: {sql}")
            return True
        except pymysql.Error as e:
            # 处理数据库错误
            print(f"Database error: {e}")
            conn.rollback()  # 回滚事务
            return False
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
    def execute_sql_file(cls, file_path: str) -> None:
        instance = cls._get_instance()
        docker_str = "docker exec -i mysql-container"
        command = f"{docker_str} mysql -u {instance.pool._kwargs['user']} -p{instance.pool._kwargs['password']} -h {instance.pool._kwargs['host']} --default-character-set=utf8mb4  {instance.pool._kwargs['database']} < {file_path}"

        try:
            subprocess.run(command, shell=True, check=True, stderr=subprocess.PIPE)
            print(f"Successfully executed SQL file: {file_path}")
        except subprocess.CalledProcessError as e:
            # 捕获并打印错误信息
            print(f"Error executing SQL file: {e}")
            print(e.stderr.decode("utf-8"))
    
    @classmethod 
    def build_insert_sql_components(cls, obj:BaseModel,) -> tuple[str, str, tuple[Any, ...]]:
        attrs = vars(obj)
        #  去掉 _sa_instance_state 属性
        if attrs.get("_sa_instance_state"):
            attrs.pop("_sa_instance_state")
        # 特殊处理，比如将字典转换为 JSON 字符串
        for key, value in attrs.items():
            if isinstance(value, dict):
                attrs[key] = json.dumps(value)

        # 构建列名和占位符
        columns = ', '.join(attrs.keys())
        placeholders = ', '.join(['%s'] * len(attrs))

        # 构建 SQL 语句
        # sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        
        # 构建参数元组
        args = tuple(attrs.values())

        return columns, placeholders, args


# 初始化单例
DatabaseManager.init("localhost", 3308, "root", "12345678", "panda_code_database")

# # 示例使用
# try:
#     DatabaseManager.init('localhost', 3306, 'root', '12345678', 'global_data')
#     # ... 进行数据库操作 ...
# except Exception as e:
#     logging.error(f"Database error: {e}")

# 查询
# result = DatabaseManager.query("SELECT * FROM some_table")

# 其他数据库操作...
