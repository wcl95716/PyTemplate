
# 停止先前的程序
stop:
	-lsof -t -i :25432 | xargs kill -9

# 启动新程序
start:
	nohup uvicorn src.main:fast_api --host 0.0.0.0 --port 25432 --reload &


install:
	python -m pip install --upgrade pip
	pip install --ignore-installed -r requirements.txt

env:
	conda create --name myenv python=3.11.5
	conda activate myenv

init_mysql:
	scripts/setup-database.sh

init_db:
	python src/db/mysql/run.py

push:
	git add .
	git commit -m "update"
	git push origin main

# 默认目标，停止先前的程序，然后启动新程序
run: stop start