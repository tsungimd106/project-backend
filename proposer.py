from model.db import DB
from spider.opendata import proposal
from spider.opendata import web

def findProposal():
    sqlstr = ("select id from proposal" % id)
    print(sqlstr)
    data = DB.execution(DB.select, sqlstr)
    return data

#提案人傳回
def returnProposer(data):
    #如果爬蟲提案的id=資料庫proposal表的id，就將爬蟲的提案人與政治人物編號比對 將id傳回提案人資料表
    if web.createpo(data["id"]) = proposal(data["id"]):
        return  web.createpo(data["billProposer"])

        sqlstr = ("insert into proposer(proposal_id, politician_id ) values('%s','%s')" %(
            data["proposal_id"],data["politician_id"]))
        print(sqlstr)
        DB.execution(DB.create, sqlstr)