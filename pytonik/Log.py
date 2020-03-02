###
# Author : Betacodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by Betacodings on 2019.
###


import logging, os, datetime, sys


class Log:
    def __init__(self, base_path=__name__):
        if os.path.isdir(os.getcwd() + "/public"):
            host = os.getcwd()  # os.path.dirname(os.getcwd())

        else:
            host = os.path.dirname(os.getcwd())

        self.format = "%(asctime)s, %(msecs)d %(name)s - [%(funcName)s %(levelname)s]  -    %(message)s"  # [%(filename)s:%(lineno)d]
        self.datefmt = "%m/%d/%Y %I:%M:%S %p"
        self.locate = host
        # base_path = str(self.locate.split('/')[-1:][0])
        # print(base_path)
        self.logs = logging.getLogger(base_path)  # base_path
        dt = datetime
        self.indata = ""

    def debug(self, string=""):
        self.indata = string
        self.__file()
        if int(self.__check()) == 1:
            self.__open_tem()
            self.logs.debug(self.indata)
            exit()
        else:
            self.logs.debug(self.indata)

    def info(self, string=""):
        self.indata = string
        self.__file()
        if int(self.__check()) == 1:
            self.__open_tem()
            self.logs.info(self.indata)
            exit()
        else:
            self.logs.info(self.indata)

    def warning(self, string=""):
        self.indata = string
        self.__file()
        if int(self.__check()) == 1:
            self.__open_tem()
            self.logs.warning(self.indata)
            exit()
        else:
            self.logs.warning(self.indata)

    def error(self, string=""):
        self.indata = string
        self.__file()

        if int(self.__check()) == 1:
            self.__open_tem()
            self.logs.error(self.indata)
            exit()
        else:
            self.logs.error(self.indata)

    def critical(self, string=""):
        self.indata = string
        self.__file()
        if int(self.__check()) == 1:
            self.__open_tem()
            self.logs.critical(self.indata)
            exit()
        else:
            self.logs.critical(self.indata)

    def __file(self):

        error_log = self.locate + "/" + "app.log"
        if os.path.isfile(error_log) == False:
            try:
                f = open(error_log, "a+")
                f.write("")
                f.close()
            except Exception as err:
                if conf.get("exception", "") == 1:
                    Exception(err)

        else:

            if int(self.__check()) == 1:
                logging.basicConfig(
                    stream=sys.stdout, format=self.format, datefmt=self.datefmt
                )

            else:
                logging.basicConfig(
                    filename=error_log, format=self.format, datefmt=self.datefmt
                )

    def __check(self):

        from pytonik.Core.env import env
        from pytonik.Config import Config
        from pytonik.Exception import Exception

        getenv = env()
        conf = Config()
        conf.add(getenv._e())
        return 0 if conf.get("exception", 0) is "" else conf.get("exception", 0)

    def __open_tem(self):
        from pytonik.App import App

        App.header()
