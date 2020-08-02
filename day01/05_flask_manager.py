"""
pip install flask-script

使用manager通过命令行修改Flask服务器的参数例如修改port，不需要修改代码
"""
from flask import Flask
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route("/")
def index():
    return "Hello Flask Manager"

if __name__ == "__main__":
    manager.run()

"""
    python 05_flask_manager.py  --> 将无法启动，要使用参数才能启动服务器
    
    usage: 05_flask_manager.py [-?] {shell,runserver} ...
    positional arguments:
      {shell,runserver}
        shell            Runs a Python shell inside Flask application context.
        runserver        Runs the Flask development server i.e. app.run()
    启动命令 python 05_flask_manager.py runserver
    
    参数介绍：python 05_flask_manager.py runserver --help
    usage: 05_flask_manager.py runserver [-?] [-h HOST] [-p PORT] [--threaded]
                                         [--processes PROCESSES]
                                         [--passthrough-errors] [-d] [-D] [-r]
                                         [-R] [--ssl-crt SSL_CRT]
                                         [--ssl-key SSL_KEY]
    
    Runs the Flask development server i.e. app.run()
    
    optional arguments:
      -?, --help            show this help message and exit
      -h HOST, --host HOST
      -p PORT, --port PORT
      --threaded
      --processes PROCESSES
      --passthrough-errors
      -d, --debug           enable the Werkzeug debugger (DO NOT use in production
                            code)
      -D, --no-debug        disable the Werkzeug debugger
      -r, --reload          monitor Python files for changes (not 100% safe for
                            production use)
      -R, --no-reload       do not monitor Python files for changes
      --ssl-crt SSL_CRT     Path to ssl certificate
      --ssl-key SSL_KEY     Path to ssl key

"""