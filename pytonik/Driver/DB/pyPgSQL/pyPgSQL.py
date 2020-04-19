# Author : BetaCodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by BetaCodings on 17/12/2019.
#############################################
#############################################
# POSTGRES Support Database Connection
# Using Raw query from psycopg2 module
# Each method represent extensions from POSTGRES version 2.2.9

from pytonik import Log

log_msg = Log.Log()

try:
    import psycopg2
    import psycopg2.extras
except Exception as err:
    log_msg.critical(err)


class pyPgSQL:
   
    def __init__(self, setting):
        self.settings = setting
        self.database = setting.get('database', '') # 
        self.username = setting.get('username', '') # 
        self.password = setting.get('password', '') # 
        self.port = setting.get('port', '') # 
        self.host = setting.get('host', '') # 
        self.prefix = setting.get('prefix', '') # 
        self.Exception = ""
        self.conn =  None
        self.con = None
        self.result = None
        self.connectDB()

    def connectDB(self):

        try:
       
            self.conn = psycopg2.connect(database=self.database, host = self.host,  port = self.port, user=self.username, password=self.password)
       
        except (Exception, psycopg2.Error) as err:
            self.Exception = err
            log_msg.error("Something went wrong : {err}".format(err=err))
            


    def query(self, sql="", value = ""):
        try:
            
            if sql !="" and value != "":
                self.con = self.conn.cursor()
                self.con.execute(str(sql), value)
            else:
                self.con = self.conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
                self.con.execute(str(sql))
                
        except (Exception, psycopg2.Error) as err:
            self.Exception = err
            log_msg.error(err)
        return self
        
        
            

    def querymultiple(self, sql="", value = ""):
        try:
            self.con = self.conn.cursor()
            if sql !="" and value != "":
                self.con.executemany(str(sql), value)
            else:
                self.con.executemany(str(sql))
        except (Exception, psycopg2.Error) as err:
            self.Exception = err
            log_msg.error(err)
            
    
        return self


 
    def lastId(self):

        try:
            self.save()
            getrowid = self.con.fetchone()[0]
        except Exception as err:
            getrowid = err

        return getrowid

    def fetch(self):
        result = self.con.fetchall()
        row = []
        for r in result:
            row.append(dict(r))
        return row
       
    def queryone(self, sql="", value = ""):
        self.con = self.conn.cursor()
        if sql !="" and value != "":
            self.con.execute(str(sql), value)
        else:
            self.con.execute(str(sql))

        return self

    def all(self):
        self.result = self.fetch()
        return self.result
    
    def one(self):
        result = self.con.fetchone()
        return dict(result)

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
                except (Exception, psycopg2.DatabaseError) as err :
                    self.Exception = "Database table '{}' already exists.".format(table_name)
                    log_msg.error("Database table '{}' already exists.".format(table_name))
                
            return self
        
        else:
            self.Exception = "Empty Table"
            return self

