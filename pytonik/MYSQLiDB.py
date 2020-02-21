###
# Author : Betacodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by Betacodings on 2019.
###

from . import Log
log_msg = Log.Log()

try:
    import mysql.connector
except Exception as err:
    log_msg.critical(err)


class MYSQLiDB:
    global connect, con
    def __init__(self, setting):
        self.settings = setting
        self.host = setting['host']
        self.database = setting['database']
        self.username = setting['username']
        self.password = setting['password']
        self.conn =  None
        self.con = None
        self.result = None
        self.connectDB()

    def connectDB(self):

        try:

            self.conn = mysql.connector.connect(
                    host=self.host,
                    user=self.username,
                    passwd=self.password,
                    database=self.database
            )


        except mysql.connector.Error as err:
            log_msg.error(err)
            return ("Something went wrong : {err}".format(err=err))


    def query(self, sql="", value = ""):
        self.con = self.conn.cursor(dictionary=True)
        if sql !="" and value != "":
            self.con.execute(str(sql), value)
        else:
            self.con.execute(str(sql))
            #self.result = self.con.fetchall()
            #self.fetch()
        return self

    def querymultiple(self, sql="", value = ""):
        self.con = self.conn.cursor(dictionary=True)
        if sql !="" and value != "":
            self.con.executemany(str(sql), value)
        else:
            self.con.executemany(str(sql))
            #self.result = self.con.fetchall()
            #self.fetch()
        return self


    def insert_id(self):
        return self.con.lastrowid

    def lastId(self):
        return self.con.lastrowid

    def fetch(self):
        if self.result != "" and self.result is not None:
            return self.result
        else:
            return False

    def queryone(self, sql="", value = ""):
        self.con = self.conn.cursor(buffered=True)
        if sql !="" and value != "":
            self.con.execute(str(sql), value)
        else:
            self.con.execute(str(sql))

        return self.con

    def all(self):
        self.result = self.con.fetchall()
        return self.fetch()

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

    def create(self, TABLES = ''):
        if TABLES:
            for table_name in TABLES:
                table_description = TABLES[table_name]
                try:
                    self.con.execute(table_description)
                    return True
                except mysql.connector.Error as err:
                    if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                        log_msg.info("Database table '{}' already exists.".format(table_name))
                        return "Database table '{}' already exists.".format(table_name)

                    else:
                        log_msg.error(err)
                        return err
        else:
         return False

    def database(self):
        cnx = mysql.connector.connect(user=self.username)
        cursor = cnx.cursor()
        try:
            cursor.execute("USE {}".format(self.database))
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                cursor.execute(
                    "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(self.database))
                log_msg.info("Database {} created successfully.".format(self.database))
            else:
                log_msg.error(err)
                return err

        cursor.close()
        cnx.close()


