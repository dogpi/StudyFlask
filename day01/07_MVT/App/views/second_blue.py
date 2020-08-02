from flask import Blueprint

second_blue = Blueprint("second_blue", __name__)

@second_blue.route("/second/")
def index():
    return "Second BluePrint"
@second_blue.route("/second_hello/")
def hello():
    return "Hello "
