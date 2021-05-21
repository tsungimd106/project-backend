from ..model.db import DB
import cn2an
from datetime import datetime as dt

class proposal:
    @staticmethod
    def create(data):
        sqlstr = ("insert into proposal(id,term,session_Period,title,status_id,pdfUrl,docUrl,updateTime) values('%s','%s','%s','%s','%s','%s','%s','%s')" % (
            data["id"], data["term"], data["session_Period"], data["title"], data["status_id"], data["pdfUrl"], data["docUrl"],data["updateTime"]))
        print(sqlstr)
        DB.execution(DB.create, sqlstr)


class web:
    @staticmethod
    def createpo(data):
        # 搜尋進度狀態
        sqlstr = "select id from proposalstatus where status = \"%s\" " % data["billStatus"]
        statusID = DB.execution(DB.select, sqlstr)
        updateT = dt.now()
        sqlstr = ("insert into proposal(id,term,session_Period,title,status_id,pdfUrl,docUrl,updateTime) values('%s','%s','%s','%s','%s','%s','%s','%s')"
                  % (data["billNo"],data["term"], data["sessionPeriod"], data["billName"],
                      statusID,data["pdfUrl"], data["docUrl"],updateT))
        print(sqlstr)
        DB.execution(DB.create, sqlstr)
