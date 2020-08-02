from .first_blue import first_blue
from .second_blue import second_blue
from .index_blue import index_blue

def init_views(app):
    app.register_blueprint(first_blue)
    app.register_blueprint(second_blue)
    app.register_blueprint(index_blue)