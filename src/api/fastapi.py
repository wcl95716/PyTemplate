from fastapi import FastAPI


from api.chat_record.api import CharRecordAPI

from api.support_ticket.api import TicketAPI


fast_api = FastAPI()
fast_api.include_router(
    TicketAPI().router, prefix="/ticket", tags=["Ticket Operations"]
)
fast_api.include_router(
    CharRecordAPI().router, prefix="/chat_record", tags=["Chat Record Operations"]
)


@fast_api.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello, World!"}



# @api_bp.route('/msg_cb', methods=['POST'])
# def message_callback():
#     if request.method == 'POST':
#         # 解析JSON数据
#         data = request.get_json()
#         # print("data ",data)

#         # 获取消息内容
#         message_content = data.get('content', '')

#         # 处理消息，这里简单打印消息内容
#         print("Received message:", message_content)
        
#         sendMsg(message_content,"Panda")

#         # 返回成功响应
#         return jsonify({"status": "success"})
