from model.db import DB
from datetime import datetime as dt


class proposal:
    @staticmethod
    def create(data):
        sqlstr = "select id from status where status = \"%s\"" % data["billStatus"]
        statusiidd = DB.execution(DB.select, sqlstr)
        sqlstr = ("insert into proposal(`id`,`term`,`session_Period`,`title`,`status_id`,`pdfUrl`,`docUrl`,`updateTime`) values('%s','%s','%s','%s','%s','%s','%s','%s')" % (
            data["billNo"], data["term"], data["session_Period"], data["title"], statusiidd["data"][0]["id"], data["pdfUrl"], data["docUrl"], data["updateTime"]))
        print(sqlstr)
        DB.execution(DB.create, sqlstr)


class web:
    @staticmethod
    def createpo(data):
        # 搜尋進度狀態

        for i in data:
            # sqlstr = "select id from status where status = \"%s\"" % data["billStatus"]
            statusiidd = {
                "退回程序": 1,
                "審查完畢": 2,
                "交付審查": 3,
                "排入院會": 4,
                "三讀": 5,
                "逕付二讀": 6,
                "撤案": 7,
                  "逕付二讀(委員會抽出)": 8,
                   "排入程序": 9,


            }.get(i["billStatus"], "error")
            # DB.execution(DB.select, sqlstr)
            updateT = dt.now()
            sqlstrs = []
            sqlstr = ("insert into proposal(`id`,`term`,`session_Period`,`session_Time`,`title`,`status_id`,`pdfUrl`,`docUrl`,`updateTime`) values('%s','%s','%s','%s','%s','%s','%s','%s','%s')"
                      % (i["billNo"], i["term"], i["sessionPeriod"],i["sessionTimes"], i["billName"],
                         statusiidd, i["pdfUrl"], i["docUrl"], updateT))
            sqlstrs.append({"sql": sqlstr, "name": i["billNo"]})
            print(sqlstr+";")
        DB.execution(DB.create, sqlstrs)

