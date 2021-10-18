from model.db import DB
from model.util import (group)
import json


def home():
    sqlstr = [{"sql": "select * from home_policy limit 5", "name": "policy"},
              {"sql": "select * from home_mes limit 5", "name": "mes"},
              {"sql": "select * from home_proposal ", "name": "proposal"}]
    result=DB.execution(DB.select, sqlstr)
    # result["data"]["proposal"]=group(result["data"]["proposal"],["c_name","name"],"id")
    return result
