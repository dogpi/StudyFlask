from flask import Blueprint

index_blue = Blueprint("index_blue", __name__)

@index_blue.route("/")
def index():
    return "BluePrint"

