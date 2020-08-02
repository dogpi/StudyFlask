from flask import Flask
from flask_script import Manager
from App import create_app

"""
    1、调用create_app创建app对象
            create_app：
                ① 创建app
                ② 加载views中的路由函数
"""
app = create_app()
manager = Manager(app=app)

if __name__ == "__main__":
    manager.run()