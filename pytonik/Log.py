###
# Author : Betacodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by Betacodings on 2019.
###


import logging, os, datetime

class Log():
    def __init__(self):
        if os.path.isdir(os.getcwd() + '/public'):
            host = os.getcwd()  # os.path.dirname(os.getcwd())

        else:
            host = os.path.dirname(os.getcwd())

        self.locate = host
        self.logs = logging
        self.__file()
        dt = datetime

    def debug(self, string=""):
        return self.logs.debug(string)

    def info(self, string=""):

        return self.logs.info(string)

    def warning(self, string=""):

        return self.logs.warning(string)

    def error(self, string=""):

        return self.logs.error(string)

    def critical(self, string=""):

        return self.logs.critical(string)

    def __file(self):
        error_log = self.locate + "/" + 'app.log'
        if os.path.isfile(error_log) == False:
            try:
                f = open(error_log, 'a+')
                f.write("")
                f.close()
            except Exception as err:
                print(err)

        else:
            return self.logs.basicConfig(filename=error_log, level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  datefmt='%m/%d/%Y %I:%M:%S %p')
