import MySQLdb
from settings import MYSQL_SERVER, MYSQL_USER, MYSQL_PWD, MYSQL_DB


class MySQLHelper:
    def __init__(self):
        self.host = MYSQL_SERVER
        self.user = MYSQL_USER
        self.pwd = MYSQL_PWD
        self.db = MYSQL_DB
        self.port = 3306
        self.encoding = 'utf8'

    def connect(self):
        self.conn = MySQLdb.connect(MYSQL_SERVER, MYSQL_USER, MYSQL_PWD, MYSQL_DB, charset='utf8', use_unicode=False)
        return self.conn.cursor()

    def insert(self, sql):
        cur = self.connect()
        cur.execute(sql)
        cur.close()
        self.conn.commit()
        self.conn.close()

    def find_all(self, sql):
        cur = self.connect()
        cur.execute(sql)
        result = cur.fetchall()
        cur.close()
        self.conn.close()
        return result