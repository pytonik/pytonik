###
# Author : Betacodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by Betacodings on 2019.
###
from pytonik import Log
log_msg = Log.Log()

try:
    import cx_Oracle
except Exception as err:
    log_msg.critical(err)


class Oracle:

    def __init__(self, setting):
        self.settings = setting
        self.host = setting.get('host', '') # 
        self.database = setting.get('database', '') # 
        self.username = setting.get('username', '') # 
        self.password = setting.get('password', '') # 
        self.prefix = setting.get('prefix', '') # 
        self.port = setting.get('port', '') # 
        self.Exception = ""
        self.conn =  None
        self.con = None
        self.result = None
        self.connectDB()

    def connectDB(self):

        try:
            dsn = cx_Oracle.makedsn(self.host, self.port, service_name=self.database)
            self.conn = cx_Oracle.connect(self.username, 
                                          self.password, 
                                          dsn,
                                          encoding="UTF-8")
          
        except cx_Oracle.IntegrityError as err:
            log_msg.error(err)
            self.Exception = err

    def query(self, sql="", value = ""):
        try:
            self.con = self.conn.cursor()
            if sql !="" and value != "":
                self.con.execute(str(sql), value)
            else:
                self.con.execute(str(sql))
        except Exception as err:
            log_msg.error(err)
            self.Exception = err
            
        return self

    def querymultiple(self, sql="", value = ""):
        try:
            self.con = self.conn.cursor()
            if sql !="" and value != "":
                self.con.executemany(str(sql), value)
            else:
                self.con.executemany(str(sql))
        except Exception as err:
            log_msg.error(err)
            self.Exception = err
        return self


    def lastId(self):
        return self.con.lastrowid

    def fetch(self):
        column = [d[0] for d in self.con.description]
        def row(*args):
            return dict(zip(column, args))
        return row

    def queryone(self, sql="", value = ""):
        self.con = self.conn.cursor()
        if sql !="" and value != "":
            self.con.execute(str(sql), value)
        else:
            self.con.execute(str(sql))

        return self.con

    def all(self):
        self.result = self.fetch()
        return self.fetch()

    def one(self):
        return self.con.fetchone()

    def count(self):
        return self.con.rowcount

    def countall(self):
        self.all()
        return self.con.rowcount

    def save(self):
        try:
            self.conn.commit()
            return True
        except Exception as err:
            self.Exception = err
            log_msg.error(err)
            return self

    def close(self):
        return self.con.close()

    def create(self, TABLES = ''):
        self.con = self.conn.cursor()
        if TABLES:
            for table_name in TABLES:
                table_description = TABLES[table_name]
                try:
                    self.con.execute(table_description)
                    self.Exception = "Database table '{}' created successfully.".format(table_name)
                except cx_Oracle.IntegrityError as err:
                        log_msg.info("Database table '{}' already exists.".format(table_name))
                        self.Exception =  "Database table '{}' already exists.".format(table_name)         
            return self
        else:
            self.Exception =  "Empty Table"
            return self

