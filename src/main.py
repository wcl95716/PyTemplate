# 导入 FastAPI 实例
import sys
sys.path.append("./src")
from utils.network_utilities import NetworkUtils

from api.fastapi import fast_api

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:fast_api", host=NetworkUtils.get_ipv6_address(), port=25432, reload=True)
