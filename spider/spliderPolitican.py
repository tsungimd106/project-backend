from ..model.db import DB


class polician:
    @staticmethod
    def create(data):
        sqlstr = ("insert into politician(term,name,sex,experience,tel,degree,address) values('%s','%s','%s','%s','%s','%s','%s')" % (
            data["term"], data["name"], data["sex"], data["experience"], data["tel"], data["degree"], data["addr"]))
        print(sqlstr)
        DB.execution(DB.create, sqlstr)

class area:
    @staticmethod
    def findArea():
        sqlstr = ("select * from area")
        data = DB.execution(DB.select, sqlstr)
        return data

class web:
    @staticmethod
    def createlygov(data):

        areaName = data["areaName"]
        if(any(chr.isdigit() for chr in areaName)):
            num = ''.join([x for x in areaName if x.isdigit()])
            print(num)
        # 搜尋選區
        sqlstr = "select id from area where name = \"%s\" " % areaName
        print(sqlstr)
        areaName = DB.execution(DB.select, sqlstr)[0][0]
        print(areaName)
        
        # 搜尋委員會
        sqlstr = "select id from committee where name = \"%s\" " % data["committee"]
        print(sqlstr)
        committee = DB.execution(DB.select, sqlstr)[0][0]
        print(committee)
        
        # 搜尋黨籍
        sqlstr = "select id from party where name = \"%s\" " % data["party"]
        print(sqlstr)
        party = DB.execution(DB.select, sqlstr)[0][0]
        print(party)
        sqlstr = ("insert into politician(term,name,sex,experience,tel,degree,address,partyid,photo,area,committee) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
                % (data["term"], data["name"], data["sex"],
                    data["experience"], data["tel"], data["degree"],
                    data["addr"], party, data["picUrl"],
                    areaName, committee))
        print(sqlstr)
        DB.execution(DB.create, sqlstr)

    @staticmethod
    def createpo(data):
        # 搜尋進度狀態
        sqlstr = "select id from proposalstatus where status = \"%s\" " % data["billStatus"]
        statusID = DB.execution(DB.select, sqlstr)
        sqlstr = ("insert into proposal(term,sessionPeriod,billNo,billName,billOrg,statusid,billProposer,billCosignatory,pdfUrl,docUrl) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
                % (data["term"], data["sessionPeriod"], data["billNo"],
                    data["billName"], data["billOrg"], statusID,
                    data["billProposer"], data["billCosignatory"],
                    data["pdfUrl"], data["docUrl"]))
        print(sqlstr)
        DB.execution(DB.create, sqlstr)
