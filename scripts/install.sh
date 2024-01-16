#!/bin/bash
curl -fsSL https://get.docker.com -o get-docker.sh && sh get-docker.sh

# 检测当前操作系统
if [[ "$OSTYPE" == "linux-gnu" ]]; then
    # Linux操作系统
    echo "当前操作系统是Linux"
    curl -O https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh | bash

    # 在这里执行适用于Linux的命令
elif [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS操作系统
    echo "当前操作系统是macOS"
    # 在这里执行适用于macOS的命令
elif [[ "$OSTYPE" == "cygwin" || "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    # Windows操作系统
    echo "当前操作系统是Windows"
    # 在这里执行适用于Windows的命令
else
    # 未知操作系统
    echo "未知操作系统"
fi
