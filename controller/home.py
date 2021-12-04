from flask import Blueprint, request, Response
from model import homeModel
import json
from coder import MyEncoder
from .util import ret, checkParm

homeAPI = Blueprint("home", __name__, url_prefix="/home")


@homeAPI.route("/", methods=["GET"])
def home():
    return ret(homeModel.home())

