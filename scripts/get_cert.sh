#!/bin/bash

# 安装 acme.sh
install_acme() {
    echo "安装 acme.sh..."
    curl https://get.acme.sh | sh
    source ~/.bashrc
}

# 使用 acme.sh 获取证书
issue_certificate() {
    local DOMAIN="$1"
    local DNS_API="$2"

    echo "申请 SSL 证书：$DOMAIN 通过 $DNS_API"

    # 申请证书 (这里以 DNS API 验证为例)
    ~/.acme.sh/acme.sh --issue --dns $DNS_API -d $DOMAIN --keylength ec-256

    # 安装证书到指定位置（根据需要修改）
    ~/.acme.sh/acme.sh --install-cert -d $DOMAIN \
        --key-file /path/to/keyfile.key \
        --fullchain-file /path/to/fullchain.cer \
        --reloadcmd "sudo nginx -s reload"
}

# 设置自动续期
setup_auto_renew() {
    ~/.acme.sh/acme.sh --install-cronjob
    echo "设置证书自动续期"
}

# 主流程
main() {
    # 替换为您的域名和 DNS API
    local DOMAIN="panda-code.top"
    local DNS_API="dns_namecheap"

    install_acme
    issue_certificate $DOMAIN $DNS_API
    setup_auto_renew
}

# 执行主流程
main
