import mysql.connector
from mysql.connector import Error


class DB():
    @property
    def select(self):
        return 0

    @property
    def create(self):
        return 1

    @property
    def update(self):
        return 2

    @property
    def delete(self):
        return 3
    @property
    def store_p(self):
        return 5

    __host = '140.131.114.148'
    __user = 'root'
    __dbname = 'db'
    __password = 'ntubimd106'
    __conn = None

    @staticmethod
    def execution(type, sqlstr):
        print(sqlstr)
        try:
            connection = mysql.connector.connect(
                host=DB.__host,
                database=DB.__dbname,
                user=DB.__user,
                password=DB.__password,
                charset="utf8",
                )
            if connection.is_connected():                
                cursor = connection.cursor(dictionary=True)
                if(isinstance(sqlstr, list)):
                    if(type == DB.create or type == DB.update):
                        for i in sqlstr:
                            cursor.execute(i["sql"])
                        connection.commit()
                        return{"success": True}
                    elif(type==DB.store_p):
                        cursor.callproc(sqlstr["name"], sqlstr["arg"])                     
                        resD=cursor.stored_results()
                        connection.commit()
                        return{"success": True,"data":resD}
                    else:
                        result = {}
                        for sqlstrItem in sqlstr:
                            cursor.execute(sqlstrItem["sql"])
                            rows = cursor.fetchall()
                            result[sqlstrItem["name"]] = rows
                        return {"success": True, "data": result}
                else:
                    if(type == DB.create or type == DB.update):
                        cursor.execute(sqlstr)
                        connection.commit()
                        return {"success": True}
                    elif(type==DB.store_p):
                        cursor.callproc(sqlstr["name"], sqlstr["arg"])                     
                        resD=cursor.stored_results()
                        connection.commit()
                        print(resD)
                        return{"success": True,"data":f"{resD}"}
                    else:
                        cursor.execute(sqlstr)
                        rows = cursor.fetchall()
                        return {"success": True, "data": rows}
                cursor.close()
                connection.close()
                print("enter close")

        except Error as e:
            print("資料庫連接失敗：", e)
            cursor.close()
            connection.close()
            return {"success": False, "data": e}
