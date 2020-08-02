from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "修改监听的主机范围，修改监听的端口号：默认为5000"

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=5005)

"""
    修改服务器监听的客户IP，0.0.0.0 表示监听所有IP，修改监听端口为5005，默认为5000
"""