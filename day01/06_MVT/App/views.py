# 存放路由函数
# 懒加载
def init_router(app):
    @app.route("/")
    def index():
        return "Hello Flask"