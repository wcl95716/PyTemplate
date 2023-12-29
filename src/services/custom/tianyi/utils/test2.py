import requests
import json
from datetime import datetime

# 接口的URL
url = "http://127.0.0.1:25432/ticket"  # 替换为实际的URL

# 构造请求体的数据
data = {
    "priority": 2,
    "status": 0,
    "create_time": datetime.now().isoformat(),  # 使用当前时间，格式化为ISO格式
    "update_time": datetime.now().isoformat(),  # 使用当前时间，格式化为ISO格式
    "id": 0,
    "uu_id": "some-uuid-string",  # 替换为有效的UUID
    "type": 1,
    "content": "这是工单内容",
    "title": "工单标题",
    "creator_id": "creator-id",
    "assigned_to_id": "assigned-to-id"
}

# 发送POST请求
response = requests.post(url, json=data)

# 检查响应
if response.status_code == 200:
    print("工单创建成功")
    print(response.json())  # 打印响应的JSON数据
else:
    print("工单创建失败", response.status_code, response.text)
