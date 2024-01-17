
# 停止先前的程序
stop:
	-lsof -t -i :443 | xargs kill -9
	-lsof -t -i :25432 | xargs kill -9

# 启动新程序
start_ssl:
	nohup uvicorn src.main:fast_api --host 0.0.0.0 --port 443 --ssl-keyfile /root/.acme.sh/panda-code.top_ecc/panda-code.top.key --ssl-certfile /root/.acme.sh/panda-code.top_ecc/panda-code.top.cer --reload &

start:
	nohup uvicorn src.main:fast_api --host 0.0.0.0 --port 25432 --reload &
	
# 启动数据库
start_mysql:
	bash  scripts/setup-database.sh 

# 刷新数据库
refresh_database:
	python src/models/creat_talbes.py


# 安装依赖
install_requirements:
	python -m pip install --upgrade pip
	pip install --ignore-installed -r requirements.txt

# 创建虚拟环境
env:
	conda env remove --name myenv
	conda create --name myenv python=3.11.5
	conda activate myenv

clean_db:
	python db/mysql/clean_tables.py

push:
	git add .
	git commit -m "update"
	git push origin main

# 默认目标，停止先前的程序，然后启动新程序
run: start_mysql refresh_database stop start