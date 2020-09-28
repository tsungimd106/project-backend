from db import DB

class polician:
    @staticmethod
    def create(data):

        sqlstr=("insert into politician(term,name,sex,experience,tel,degree,address) values('%s','%s','%s','%s','%s','%s','%s')" %(
        data["term"],data["name"],data["sex"],data["experience"],data["tel"],data["degree"],data["addr"]))
        print(sqlstr)
        DB.execution(DB.create,sqlstr)
           
class area:
    @staticmethod
    def findArea():
        sqlstr=("select * from area")
        data =DB.execution(DB.select,sqlstr) 
        result=[]
        for i in data:
            temp=[]
            for k in i:
                temp.append(k.decode("utf8"))
            result.append(temp)
        return result
    
