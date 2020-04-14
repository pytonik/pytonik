# Author : BetaCodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by BetaCodings on 08/11/2019.

from pytonik.App import App



class Schema(App):

    def __getattr__(self, item):
        return item


    def __init__(self):
        return None
    
    def table(self, table):
        self.DB()
        drive = self.Driver
        if drive == "MYSQL":
            from pytonik.Driver.DB.MYSQL.Table import  Table
            return Table(table)
        
        if drive == "Oracle":
            from pytonik.Driver.DB.Oracle.Table import  Table
            return Table(table)
        
        if drive == "pyPgSQL":
            from pytonik.Driver.DB.pyPgSQL.Table import  Table
            return Table(table)
    
          
        if drive == "SQLite":
            from pytonik.Driver.DB.SQLite.Table import  Table
            return Table(table)

    def raw(self, string):
        return string

    def query(self, raw):
        return self.DB().query(raw)

