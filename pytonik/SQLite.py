# Author : BetaCodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by BetaCodings on 08/11/2019.

from . import Log
import os, sys
log_msg = Log.Log()
host = os.path.dirname(os.getcwd())

try:
    import sqlite3

except Exception as err:
    log_msg.critical(err)


class SQLite:
    global connect, con
    def __init__(self, setting):
        self.path = setting['path']
        self.name = setting['name']
        self.conn = str(host) + str(self.path)+"/"+str(name)
        self.con = None
        self.result = None
        self.connectDB()

    def connectDB(self):

        try:
            self.con = self.conn.cursor(dictionary=True)
        except Exception as err:
            log_msg.error(err)
            return ("Something went wrong : {err}".format(err=err))


    def query(self, sql="", value = ""):

        if sql !="" and value != "":
            self.con.execute(str(sql), value)
        else:
            self.con.execute(str(sql))
            #self.result = self.con.fetchall()
            #self.fetch()
        return self.con


    def insert_id(self):
        return self.con.lastrowid

    def lastId(self):
        return self.con.lastrowid

    def fetch(self):
        import json

        if self.result != "" and self.result is not None:
            return self.result
        else:
            return False

    global dictv
    dictv = dict()
    def addDict(self, k, v):

        for i in dictv:
            if i == k:
                print(i)
                print('error')
                return
        #dictv[k] = v

    def all(self):
        self.result = self.con.fetchall()
        return  self.fetch()

    def one(self):
        return self.con.fetchone()

    def countrow(self):
        return self.con.rowcount

    def countall(self):
        self.all()
        return self.con.rowcount

    def save(self):
        try:
            self.conn.commit()
            return True
        except Exception as err:
            return err

    def close(self):
        return self.con.close()

