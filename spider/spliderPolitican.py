from ..model.db import DB
import cn2an


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
            print(cn2an.an2cn(num, "low"))
            areaName=areaName.replace( num, cn2an.an2cn(num, "low"))
            print("after replace",areaName)
            
        # 搜尋選區
        sqlstr = "select id from area where name = \"%s\" " % areaName
        print(sqlstr)
        areaName = DB.execution(DB.select, sqlstr)
        areaName = areaName.get("data")[0].get("id")
        print(areaName)

        # 搜尋黨籍
        sqlstr = "select id from party where name = \"%s\" " % data["party"]
        print(sqlstr)
        party = DB.execution(DB.select, sqlstr)
        party = party.get("data")[0].get("id")
        print(party)
        sqlstr = ("insert into politician(term,name,sex,experience,tel,degree,address,party_id,photo,area_id,position_id) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
                  % (data["term"], data["name"], data["sex"],
                     data["experience"], data["tel"], data["degree"],
                     data["addr"], party, data["picUrl"],
                     areaName, "1"))
        print(sqlstr)
        DB.execution(DB.create, sqlstr)
        # 搜尋政治人物id回傳
        # 搜尋委員會
        comms = data["committee"].split(";")
        sqlstr = ("select id from politician where name='%s' and term='%s'  and position_id='%s'" %
                  (data["name"], data["term"], 1))
        print(comms)
        print(sqlstr)
        politid = DB.execution(DB.select, sqlstr)

        politid = politid.get("data")[0].get("id")
        for i in comms:
            if(i != ""):
                session = i.split("：")[0]

                sqlstr = ("select id from committee where name= '%s'" %
                          i.split("：")[1])
                print(sqlstr)
                committee = DB.execution(DB.select, sqlstr)
                print(committee)
                committee = committee.get("data")[0].get("id")
                sqlstr = (
                    "insert into legislatorcol (politician_id,committee_id,sessions) values('%s','%s','%s')" % (politid, committee, session))
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
