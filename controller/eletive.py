from flask import Blueprint, request, Response
# from model import articleModel
import json
from coder import MyEncoder
from .util import ret, checkParm

eletiveAPI = Blueprint("eletive", __name__, url_prefix="/eletive")


@eletiveAPI.route("/", methods=["GET"])
def article():
    return ret("ok")
