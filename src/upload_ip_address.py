
import sys
from api.common.server_ip_map.client_api import ServerIPMapClient
from models.tables.server_ip_map.type import ServerIPMapBase
sys.path.append("./src")

from utils.network_utilities import NetworkUtils


if __name__ == "__main__":
    # 获取ipv6地址
    ipv6 = NetworkUtils.get_ipv6_address()
    ipv4  = NetworkUtils.get_ipv4_address()
    mac_address = NetworkUtils.get_mac_address()
    hostname = NetworkUtils.get_hostname()
    
    server_ip_map : ServerIPMapBase = ServerIPMapBase(
        server_name = hostname,
        server_ipv4 = ipv4,
        server_ipv6 = ipv6,
        server_mac_address = mac_address
    )
    
    # print(server_ip_map)
    server_ip_map_client = ServerIPMapClient("http://192.168.0.100:25432")
    res = server_ip_map_client.update_record(server_ip_map)
    # print(res)
    
    
    
    