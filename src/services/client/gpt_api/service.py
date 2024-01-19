import openai
from typing import Dict, List

# 配置 OpenAI 和 Azure 参数
openai.api_type = "azure"
openai.api_base = "https://chenglongwen.openai.azure.com/"
openai.api_version = "2023-07-01-preview"
openai.api_key = "62f432e462164233993b473d45854844"

# 用户历史记录字典
user_histories: Dict[str, List[Dict[str, str]]] = {}

def update_histories(user_id:str , ai_message:str) -> None:
    user_histories[user_id].append({"role": "assistant", "content": ai_message})
    if len(user_histories[user_id]) > 5:
        user_histories[user_id].pop(0)
    pass

def get_ai_response(user_id: str, user_message: str) -> str:
    # 确保用户历史存在
    if user_id not in user_histories:
        user_histories[user_id] = []

    # 更新用户历史
    user_histories[user_id].append({"role": "user", "content": user_message})

    # 调用 OpenAI API
    response = openai.ChatCompletion.create(  # type: ignore
        engine="test1",
        messages=user_histories[user_id],  # 使用用户历史
        temperature=0.7,
        max_tokens=800,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )

    # 更新历史记录，添加 AI 响应
    ai_message:str = response.choices[0].message['content']

    update_histories(user_id, ai_message)
    return ai_message

# 测试函数
print(get_ai_response("user1", "给我一首李白的诗 中文回复"))
print(get_ai_response("user2", "你好，我是另一个用户。"))
