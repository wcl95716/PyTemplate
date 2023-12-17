#!/bin/bash

# 设置MySQL根用户密码和数据库名称
MYSQL_ROOT_PASSWORD="12345678"
DATABASE_NAME="panda_code_database"
PORT=3308
# 检查是否提供了 PORT 参数，否则使用默认端口 3306
# if [ -z "$PORT" ]; then
#   PORT=3308
# fi

# 拉取MySQL镜像
docker pull mysql:latest

# 创建MySQL容器并设置根用户密码和数据库名称
docker run -d --name mysql-container -e MYSQL_ROOT_PASSWORD="$MYSQL_ROOT_PASSWORD" -e MYSQL_DATABASE="$DATABASE_NAME" -p "$PORT":3306 mysql:latest

# 等待MySQL容器启动
echo "Waiting for MySQL container to start..."
# sleep 10

# 连接到MySQL容器并创建其他MySQL用户（可选）
# 替换 <username> 和 <password> 为所需的用户名和密码
# docker exec -it mysql-container mysql -uroot -p"$MYSQL_ROOT_PASSWORD" -e "CREATE USER '<username>'@'%' IDENTIFIED BY '<password>'; GRANT ALL PRIVILEGES ON $DATABASE_NAME.* TO '<username>'@'%'; FLUSH PRIVILEGES;"

echo "MySQL database environment is ready!"
