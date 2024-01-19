#Note: The openai-python library support for Azure OpenAI is in preview.
      #Note: This code sample requires OpenAI Python library version 0.28.1 or lower.
import os
import openai

openai.api_type = "azure"
openai.api_base = "https://chenglongwen.openai.azure.com/"
openai.api_version = "2023-07-01-preview"
openai.api_key = "62f432e462164233993b473d45854844"

message_text = [
    {"role":"user","content":"给我一首李白的诗 中文回复"},
]

response = openai.ChatCompletion.create(
  engine="test1",
  messages = message_text,
  temperature=0.7,
  max_tokens=800,
  top_p=0.95,
  frequency_penalty=0,
  presence_penalty=0,
  stop=None
)
print(response)
print(response['choices'][0]['message']['content'])