
# 停止先前的程序
stop:
	-lsof -t -i :25432 | xargs kill -9

# 启动新程序
start:
	nohup uvicorn src.main:fast_api --host 0.0.0.0 --port 25432 --reload &

# 启动数据库
start_mysql:
	bash  scripts/setup-database.sh 

# 刷新数据库
refresh_database:
	python src/models/creat_talbes.py

install:
	python -m pip install --upgrade pip
	pip install --ignore-installed -r requirements.txt

env:
	conda env remove --name myenv
	conda create --name myenv python=3.11.5
	conda activate myenv

init_mysql:
	scripts/setup-database.sh

clean_db:
	python db/mysql/clean_tables.py

push:
	git add .
	git commit -m "update"
	git push origin main

# 默认目标，停止先前的程序，然后启动新程序
run: start_mysql refresh_database stop start