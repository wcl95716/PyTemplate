import socket
import logging
import uuid
import requests
from typing import Dict, Optional

class NetworkUtils:
    _instance: Optional['NetworkUtils'] = None
    logger: logging.Logger
    ipv6:Optional[str] = None
    ipv4:Optional[str] = None
    connected = False

    def __new__(cls) -> 'NetworkUtils':
        if cls._instance is None:
            cls._instance = super(NetworkUtils, cls).__new__(cls)
            # 初始化日志记录器
            cls._instance.logger = logging.getLogger(cls.__name__)
        return cls._instance


    @classmethod
    def _get_address(cls, family: int, remote_server: str = "ipv4.google.com") -> str:
        """
        获取指定类型(family)的IP地址。

        :param family: IP地址类型（IPv4/IPv6）
        :param remote_server: 用于确定公网IP的远程服务器地址，默认为"ipv4.google.com"
        :return: IP地址字符串，如果无法获取则返回空字符串
        """
        try:
            with socket.socket(family, socket.SOCK_DGRAM) as s:
                s.connect((remote_server, 80))
                return s.getsockname()[0]  # type: ignore
        except Exception as e:
            if cls._instance is not None:
                cls._instance.logger.error(f"无法获取地址: {e}")
            return ""

    @classmethod
    def get_ipv6_address(cls) -> str:
        """
        获取公网IPv6地址。

        :return: IPv6地址字符串，如果无法获取则返回空字符串
        """
        if cls.ipv6:
            return cls.ipv6
        cls.ipv6 = cls._get_address(socket.AF_INET6, "ipv6.google.com")
        return cls.ipv6
    @classmethod
    def get_ipv4_address(cls) -> str:
        """
        获取公网IPv4地址。

        :return: IPv4地址字符串，如果无法获取则返回空字符串
        """
        if cls.ipv4:
            return cls.ipv4
        cls.ipv4 = cls._get_address(socket.AF_INET, "ipv4.google.com")
        return cls.ipv4

    @classmethod
    def is_connected_to_internet(cls) -> bool:
        """
        检测是否连接到互联网。

        :return: 布尔值，表示是否连接到互联网
        """
        test_sites = ["http://www.baidu.com", "http://www.cloudflare.com", "http://www.amazon.com"
                      ,"http://www.aliyun.com", "http://www.jd.com", "http://www.github.com"]
        for site in test_sites:
            try:
                requests.get(site, timeout=5)
                return True
            except requests.ConnectionError:
                continue
        return False
    
    #获取本机mac地址
    @classmethod
    def get_mac_address(cls) -> str:
        mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
        mac_address = ":".join([mac[e:e+2] for e in range(0, 12, 2)])
        return mac_address
    
    @classmethod
    def get_interface_details(cls) -> Dict[str, int]:
        """
        获取所有网络接口的详细信息。

        :return: 包含网络接口名称和索引的字典
        """
        return {interface[1]: socket.if_nametoindex(interface[1]) for interface in socket.if_nameindex()}
    
NetworkUtils.__new__(NetworkUtils)



# 示例代码
if __name__ == "__main__":
    # 获取IPv6地址
    ipv6_address = NetworkUtils.get_ipv6_address()
    print(f"IPv6地址: {ipv6_address}" if ipv6_address else "未找到IPv6地址。")

    # 获取IPv4地址
    ipv4_address = NetworkUtils.get_ipv4_address()
    print(f"IPv4地址: {ipv4_address}" if ipv4_address else "未找到IPv4地址。")

    # 检测网络连接
    print("已连接到互联网。" if NetworkUtils.is_connected_to_internet() else "未连接到互联网。")

    # 获取所有网络接口详情
    print("网络接口详情:", NetworkUtils.get_interface_details())
    
    #获取mac地址
    print("mac地址:",NetworkUtils.get_mac_address())
