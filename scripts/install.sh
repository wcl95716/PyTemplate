#!/bin/bash
curl -fsSL https://get.docker.com -o get-docker.sh && sh get-docker.sh


function install_python(){
    # 安装python依赖
    python -m pip install --upgrade pip
	pip install --ignore-installed -r requirements.txt
    echo "python依赖安装完成"
}

function install_linux_conda() {
    curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && bash Miniconda3-latest-Linux-x86_64.sh
    echo "conda 安装完成"
}

# 检测当前操作系统
if [[ "$OSTYPE" == "linux-gnu" ]]; then
    # Linux操作系统
    echo "当前操作系统是Linux"
    # 安装make git 等
    sudo apt update
    sudo apt install make
    sudo apt install git
    
    # 安装conda , python 环境
    install_conda
    install_python

    # 在这里执行适用于Linux的命令
elif [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS操作系统
    echo "当前操作系统是macOS"
    # Anaconda3-2023.09-0-MacOSX-x86_64.sh
    curl -O https://repo.anaconda.com/archive/Anaconda3-2023.09-0-MacOSX-x86_64.sh && bash Anaconda3-2023.09-0-MacOSX-x86_64.sh

    install_python

elif [[ "$OSTYPE" == "cygwin" || "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    # Windows操作系统
    echo "当前操作系统是Windows"
    # 在这里执行适用于Windows的命令
else
    # 未知操作系统
    echo "未知操作系统"
fi
