import pymysql

# 连接到 MySQL 服务器，而不是特定的数据库
connection = pymysql.connect(host='localhost',
                             port=3306,
                             user='root',
                             password='12345678',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


database_name = "global_data"
try:
    with connection.cursor() as cursor:
        # 使用字符串格式化来创建新数据库
        sql = f"CREATE DATABASE IF NOT EXISTS `{database_name}`"
        cursor.execute(sql)
    connection.commit()
finally:
    connection.close()


if __name__ == '__main__':
    
    pass