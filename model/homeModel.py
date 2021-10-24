from model.db import DB
from model.util import (group)
import json


def home():
    sqlstr = [{"sql": "select * from home_policy limit 5", "name": "policy"},
              {"sql": "select * from home_mes limit 5", "name": "mes"},
              {"sql": "select * from home_proposal limit 5", "name": "proposal"},
              {"sql": "select  cs.name,round(cs.score,2) as score,p.photo from count_score as cs join politician as p on cs.id=p.id order by score desc limit 3", "name": "rank"}]
    result = DB.execution(DB.select, sqlstr)
    # result["data"]["proposal"]=group(result["data"]["proposal"],["c_name","name"],"id")
    return result
