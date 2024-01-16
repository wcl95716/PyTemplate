#!/bin/bash

function install_letsencrypt_tls() {
    # 定义 acme.sh 的安装路径
    ACME_SH="$HOME/.acme.sh/acme.sh"

    # 安装 acme.sh
    if [ ! -f "$ACME_SH" ]; then
        echo "正在安装 acme.sh..."
        curl https://get.acme.sh | sh
        # 重新加载 shell 配置
        source "$HOME/.bashrc"
        # 或者重新加载 acme.sh 的配置文件
        # source "$HOME/.acme.sh/acme.sh.env"
    fi

    # 输入域名
    read -p "请输入你要为其获取证书的域名: " domain
    if [[ -z "$domain" ]]; then
        echo "域名不能为空。"
        return 1
    fi

    # 结束占用 80 端口的进程
    echo "正在检查并结束占用 80 端口的进程..."
    sudo fuser -k 80/tcp

    # 使用 acme.sh 的完整路径生成证书
    echo "正在从 Let's Encrypt 获取证书..."
    "$ACME_SH" --issue --standalone -d "$domain" --keylength ec-256 --server letsencrypt


    # 检查证书是否生成成功
    if [[ -f "$HOME/.acme.sh/$domain_ecc/fullchain.cer" ]] && [[ -f "$HOME/.acme.sh/$domain_ecc/$domain.key" ]]; then
        echo "证书成功生成。"
        echo "证书路径: $HOME/.acme.sh/$domain_ecc/fullchain.cer"
        echo "私钥路径: $HOME/.acme.sh/$domain_ecc/$domain.key"
    else
        echo "证书生成失败。"
        return 1
    fi
}

# 调用函数
install_letsencrypt_tls
