# Author : BetaCodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by BetaCodings on 08/11/2019.
#############################################
#############################################
# SQLITE Support Database Connection
# Using Raw query from sqlite3 module
# Each method represent extensions from SQLITE 3


from pytonik import Log
import os, sys
log_msg = Log.Log()
host = os.path.dirname(os.getcwd())
D = "/"
try:
    import sqlite3

except Exception as err:
    log_msg.critical(err)



class SQLite:

    def __init__(self, setting):
        self.path = setting.get('path', '')
        self.name = setting.get('name', '')
        self.bdfile = str(host) + D + str(self.path)+ D +str(self.name)
        self.prefix = setting.get('prefix', '')
        self.Exception = ""
        self.success = ""
        self.conn = None
        self.con = None
        self.result = None
        self.connectDB()
        

    def connectDB(self):

        try:
            self.conn = sqlite3.connect(self.bdfile)
         
        except Exception as err:
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
        result = self.con.fetchall()
        row = []
        for r in result:
            rowf = {}
            for idx, col in enumerate(self.con.description):
                rowf[col[0]] = r[idx]
            row.append(rowf)
        return row if len(row) > 0 else ""

    def queryone(self, sql="", value = ""):
        self.con = self.conn.cursor()
        if sql !="" and value != "":
            
            self.con.execute(str(sql), value)
        else:
            self.con.execute(str(sql))

        return self.con

    def all(self):
        self.result = self.fetch()
        return self.result

    def one(self):
        result = self.con.fetchone()
        row = {}
        for idx, col in enumerate(self.con.description):
            
            row[col[0]] = result[idx]
        return row

    def count(self):
        return self.con.rowcount

    def countall(self):
        self.all()
        return self.con.rowcount if self.con.rowcount > 0 else 0
     
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
                except Exception as err:
                
                    log_msg.info("Database table '{}' already exists.".format(table_name))
                    self.Exception =  "Database table '{}' already exists.".format(table_name)
            
            return self
        
        else:
            self.Exception =  "Empty Table"
            return self

