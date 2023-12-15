import threading
from flask import Blueprint, current_app, jsonify, request, send_file, render_template, url_for
from flask_cors import CORS
import os
import markdown2

from models import ticketing_system
from models.ticketing_system.types.ticket_record import TicketRecord
from models.ticketing_system.types.user_profile import UserProfile
from models.wechat_bot.types.chat_action_function import ChatActionFunctionFactory
from models.wechat_robot_online.api.main_api import get_log_processing, upload_img_file
from models.wechat_robot_online.types.log_processing_type import LogProcessingFilesUrl
from models.wechat_robot_online.types.robot_task_type import RobotTask, RobotTaskType
from utils import  local_logger

from service.api_folder.api_ticketing_system.sub_model1 import api_bp as api_bp_sub
api_bp = Blueprint('wechat_werobot', __name__ ,url_prefix='/wechat_werobot')

api_bp.register_blueprint(api_bp_sub)

CORS(api_bp) # 解决跨域问题

# 定义用于测试的 API 路由
@api_bp.route('/api_endpoint')
def api_endpoint():
    return "This is an API endpoint from api_module.py"


@api_bp.route('/msg_cb', methods=['POST'])
def message_callback():
    if request.method == 'POST':
        # 解析JSON数据
        data = request.get_json()
        print("data ",data)

        # 获取消息内容
        # message_content = data.get('content', '')

        # 处理消息，这里简单打印消息内容
        #print("Received message:", message_content)

        # 返回成功响应
        return jsonify({"status": "success"})
