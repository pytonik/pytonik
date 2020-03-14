###
# Author : Betacodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by Betacodings on 2019.
#############################################
#############################################
# MYSQL Support Database Connection
# Using Raw query from mysql-connector module
# Each method represent extensions from mysql version 2.2.9


from pytonik import Log
log_msg = Log.Log()

try:
    import mysql.connector
except Exception as err:
    log_msg.critical(err)


class MYSQL:

    def __init__(self, setting):
        self.settings = setting
        self.host = setting.get('host', '') #  get 'host' name 
        self.username = setting.get('username', '') #  get host 'username' 
        self.password = setting.get('password', '') #  get host 'password' 
        self.port = setting.get('port', '') #  get host 'port' 
        self.database = setting.get('database', '') #  get 'database' name 
        self.prefix = setting.get('prefix', '') #  get database 'prefix' 
        self.Exception = "" # Exception String handler
        self.conn =  None # Connection Return handler
        self.con = None # Connection Return cursor handler
        self.result = None # Return Query Results
        self.connectDB() # Initiating Connection Method 


    # This method 'connectDB' represent MYSQL configuration and Connection using 
    # 'host', 'database' 'username',  'password',  'prefix' 
    def connectDB(self):

        try:

            self.conn = mysql.connector.connect(
                    host=self.host,
                    user=self.username,
                    passwd=self.password,
                    database=self.database,
                    port = self.port
            )
        except mysql.connector.Error as err:
            log_msg.error(err)
            self.Exception = err

    # This method 'query' execute MYSQL query and returns cursor handler for 
    # select, update, delete, insert, tasks 
    def query(self, sql="", value = ""):
        try:
            self.con = self.conn.cursor(dictionary=True)
            if sql !="" and value != "":
                self.con.execute(str(sql), value)
            else:
                self.con.execute(str(sql))
        except Exception as err:
            log_msg.error(err)
            self.Exception = err
            
        return self

    # This method 'querymultiple' handles many execution of MYSQL queries and returns cursor handler for 
    # multiple insert tasks 
    def querymultiple(self, sql="", value = ""):
        try:
            self.con = self.conn.cursor(dictionary=True)
            
            if sql !="" and value != "":
                self.con.executemany(str(sql), value)
            else:
                self.con.executemany(str(sql))
        except Exception as err:
            log_msg.error(err)
            self.Exception = err
            
        return self

    # This method 'lastId' gets the last inserted or generated increment number in a row
    def lastId(self):
        return self.con.lastrowid

    # This method 'fetch' returns table results dictionary
    def fetch(self):
            return self.con.fetchall()

    # This method 'queryone' execute MYSQL query and returns cursor handler for 
    # select, update, delete, insert, tasks 
    def queryone(self, sql="", value = ""):
        self.con = self.conn.cursor(buffered=True)
        if sql !="" and value != "":
            self.con.execute(str(sql), value)
        else:
            self.con.execute(str(sql))
            
        return self.con

    # This method 'all' returns table results dictionary
    # Helps in calling both result and count
    def all(self):
        self.result = self.fetch()
        return self.result

    # This method 'one' returns table results list
    def one(self):
        return self.con.fetchone()

    # This method 'count' returns total number of rows count of a table
    def count(self):
        return self.con.rowcount
    
    # This method 'countall' returns table results dictionary
    # Helps in calling both result and count
    def countall(self):
        self.all()
        return self.con.rowcount

    # This method 'save' Execute table query: 
    # insert, update and return bool -> True or Exception
    def save(self):
        try:
            self.conn.commit()
            return True
        except Exception as err:
            self.Exception = err
            log_msg.error(err)
            return self

    # This method 'close' end query and also 
    # close connection at the end of a query 
    def close(self):
        return self.con.close()

    # This method 'create' handles query creation of tables
    def create(self, TABLES = ''):
        self.con = self.conn.cursor()
        if TABLES:
            for table_name in TABLES:
                table_description = TABLES[table_name]
                try:
                    self.con.execute(table_description)
                    
                except mysql.connector.Error as err:
                        log_msg.info("Database table '{}' already exists.".format(table_name))
                        self.Exception =  "Database table '{}' already exists.".format(table_name)
            return self          
        else:
            self.Exception =  "Empty Table"
            return self
