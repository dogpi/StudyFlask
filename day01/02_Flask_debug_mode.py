from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hellld Flask Debug"



if __name__ == "__main__":
    app.run(debug=True)

"""
    Flask debug模式，修改文件后，服务器会重新启动，加载代码。
    减去了开发人员手动启动的繁琐。
    
     * Serving Flask app "02_Flask_debug_mode" (lazy loading)
     * Environment: production                  --> 可通过FLASK_ENV环境变量进行修改。
       WARNING: This is a development server. Do not use it in a production deployment.
       Use a production WSGI server instead.
     * Debug mode: on
     * Restarting with stat
     * Debugger is active!
     * Debugger PIN: 655-456-661                -->在网页进行调试时需要输入PIN码
     * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

"""