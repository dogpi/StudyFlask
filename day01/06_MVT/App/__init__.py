from flask import Flask
from .views import init_router

def create_app():
    # 创建app
    app = Flask(__name__)
    # 加载路由（路由出来函数）
    init_router(app)
    return app