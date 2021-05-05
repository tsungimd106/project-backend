from flask import Blueprint, request, Response
from model import articleModel
import json
from coder import MyEncoder
from .util import ret, checkParm

articleAPI = Blueprint("article", __name__, url_prefix="/article")


@articleAPI.route("/", methods=["GET"])
def article():
    return ret(articleModel.getArticle())
