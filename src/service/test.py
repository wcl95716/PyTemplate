from flask import Flask
from flask_cors import CORS
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)
CORS(app) # 解决跨域问题

# 定义一个资源
@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        # 处理 GET 请求
        return {'hello': 'world'}
    def post(self):
        # 处理 POST 请求
        return {'hello': 'world'}
    def delete(self):
        # 处理 DELETE 请求
        return {'hello': 'world'}
    def put(self):
        # 处理 PUT 请求
        return {'hello': 'world'}


# 可以定义多个资源并分配给不同的路由
@api.route('/goodbye')
class GoodbyeWorld(Resource):
    def get(self):
        # 另一个 GET 请求处理
        return {'goodbye': 'world'}

if __name__ == '__main__':
    app.run(debug=True)
