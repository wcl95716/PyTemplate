# 导入 FastAPI 实例
from api.fastapi import fast_api

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:fast_api", host="0.0.0.0", port=25432, reload=True)
