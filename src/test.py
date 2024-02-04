from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

# 配置CORS，允许所有来源的请求
CORS(app)


@app.route('/')
def hello_world() -> str:
    return 'Hello, World!'

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=8000, debug=True)
    app.run(host='::', port=8000, debug=True)
