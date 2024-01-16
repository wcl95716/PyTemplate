#!/bin/bash

# 设置MySQL根用户密码和数据库名称
MYSQL_ROOT_PASSWORD="12345678"
DATABASE_NAME="panda_code_database"
PORT=3308

# 检查是否已经存在名为mysql-container的容器
if ! docker ps -a | grep -q "mysql-container"; then
  # 如果容器不存在，拉取MySQL镜像并创建容器
  docker pull mysql:latest
  docker run -d --name mysql-container -e MYSQL_ROOT_PASSWORD="$MYSQL_ROOT_PASSWORD" -e MYSQL_DATABASE="$DATABASE_NAME" -p "$PORT":3306 mysql:latest
  echo "MySQL container created."
fi

# 检查MySQL容器的运行状态
if ! docker ps | grep -q "mysql-container"; then
  # 如果容器没有在运行，启动容器
  docker start mysql-container
  echo "MySQL container started."
fi

# 等待MySQL容器启动
echo "Waiting for MySQL container to start..."
# sleep 10

# 连接到MySQL容器并创建其他MySQL用户（可选）
# 替换 <username> 和 <password> 为所需的用户名和密码
# docker exec -it mysql-container mysql -uroot -p"$MYSQL_ROOT_PASSWORD" -e "CREATE USER '<username>'@'%' IDENTIFIED BY '<password>'; GRANT ALL PRIVILEGES ON $DATABASE_NAME.* TO '<username>'@'%'; FLUSH PRIVILEGES;"

echo "MySQL database environment is ready!"
