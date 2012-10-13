'''
Created on 2012-9-27

@author: yyang21
'''
import MySQLdb
from settings import DATABASES


DEFAULTDB = DATABASES["default"]
class DBConnector:
    __conn = None
    __cursor = None
    def __init__(self):
        self.__conn = MySQLdb.Connect(host=DEFAULTDB['HOST'], user=DEFAULTDB['USER'], passwd=DEFAULTDB['PASSWORD'], db=DEFAULTDB['NAME'], port=int(DEFAULTDB['PORT']), charset='utf8')
        self.__conn.begin()
        self.__cursor = self.__conn.cursor()

    def getDefaultConn(self):
        pass


    def closeConn(self):
        self.__cursor.close()
        self.__conn.close()

    def qureySql(self, sql):
        count = self.__cursor.execute(sql)
        resultTuple = (count, self.__cursor.fetchall())
        self.closeConn()
        return resultTuple

if __name__ == '__main__':
    con = DBConnector()
    con1 = DBConnector()
    resultTuple = con.qureySql('select id,name,comments from test')
    resultTuple1 = con1.qureySql('select id,name,comments from test')
    print resultTuple[1]
    print resultTuple1[1]


#    cur = getDefaultConn()
#    count=cur.execute('select id,name,comments from test')
#    result = cur.fetchall()
#    print result
 #   closeConn(cur)
    #print 'there has %s rows record' % count
