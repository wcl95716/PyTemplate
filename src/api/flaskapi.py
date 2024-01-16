from typing import Any
from flask import Flask, send_file
import sys
sys.path.append("./src")


from flask_cors import CORS

app = Flask(__name__)
CORS(app) # 解决跨域问题

@app.route('/video')
def get_video() -> Any:
    file_path = "/Users/panda/Desktop/github/PyTemplate/data/upload_file/xvideos.com_2cb31335a21d9fa774f153b65829d590.mp4"
    return send_file(file_path, conditional=True)

if __name__ == '__main__':
    app.run(debug=True)
