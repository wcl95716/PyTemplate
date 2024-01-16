#!/bin/bash

# 请求用户输入域名
read -p "请输入你的域名: " DOMAIN

# 检查是否输入了域名
if [ -z "$DOMAIN" ]; then
    echo "错误：没有输入域名。"
    exit 1
fi

# 定义邮箱地址
EMAIL="your-email@example.com"

# 安装 Certbot
echo "正在安装 Certbot..."
sudo apt-get update
sudo apt-get install software-properties-common
sudo add-apt-repository universe
sudo add-apt-repository ppa:certbot/certbot
sudo apt-get update
sudo apt-get install certbot python3-certbot-nginx

# 获取证书
echo "正在获取 Let's Encrypt 证书..."
sudo certbot --nginx -d $DOMAIN -m $EMAIL --agree-tos --non-interactive

# 设置自动续期
echo "设置证书自动续期..."
(crontab -l 2>/dev/null; echo "0 12 * * * /usr/bin/certbot renew --quiet") | crontab -
