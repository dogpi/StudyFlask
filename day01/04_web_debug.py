from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    a = 10
    b = 20
    c = 20/0
    return "20 / 0 = %s" %c

if __name__ == "__main__":
    app.run(debug=True)

"""
    当在页面出现错误时，也可以进行debug，但是要输入PIN码。
    在页面打开一个python交互界面
"""