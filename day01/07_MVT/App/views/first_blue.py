"""
    使用蓝图
    pip install falsk-blueprint
"""
from flask import Blueprint

first_blue = Blueprint("first_blue", __name__)

@first_blue.route("/first/")
def index():
    return "First BluePrint"
@first_blue.route("/first_hello/")
def hello():
    return "Hello "
