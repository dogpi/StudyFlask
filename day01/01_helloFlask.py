from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello Flask"


if __name__ == "__main__":
    app.run()

"""
    简单的启动Flask服务，在页面上显示一句话“Hello Flask”。
    
     * Serving Flask app "01_helloFlask" (lazy loading)
     * Environment: production
       WARNING: This is a development server. Do not use it in a production deployment.
       Use a production WSGI server instead.
     * Debug mode: off
     * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

"""