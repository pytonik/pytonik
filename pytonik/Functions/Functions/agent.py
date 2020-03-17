# Author : BetaCodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by BetaCodings on 17/11/2019.
import os as opy, re
from pytonik.util.Variable import Variable

class os(Variable):

    def __getattr__(self, item):
        return item

    def __call__(self, *args, **kwargs):
        return None

    def __init__(self):
        if self.out('HTTP_USER_AGENT') != "":
            self.agent = self.out('HTTP_USER_AGENT')
        else:
            self.agent = None

        self.info = []
        self.name()
        self.name = self.info['OS']
        self.device = self.info['Device']

    def name(self):
         NAME = {
                "Windows": "PC",
				"Linux" : "PC",
				"Unix" : "PC",
				"Mac": "PC",
				"Android" : "Mobile",
				"Ubuntu" : "PC",
				"Chromium" : "PC",
				"iOS" : "PC",
				"DOS" : "PC",
				"JavaOS" : "PC",
				"Zorin" : "PC",
				"Elementary" : "PC",
				"NetWare" : "PC",
				"Papyros" : "PC",
				"Solaris" : "PC",
				"Symbian" : "Mobile",
				"Bharat" : "PC",
				"CentOS" : "PC",
				"ReactOS" : "PC",
                "iPhone" : "Mobile",
                "iPod" : "Mobile",
                "iPad" : "Mobile",
                "BlackBerry" : "Mobile",
                "Funtouch" : "Mobile",
                "LineageOS" : "Mobile",
                "BADA" : "Mobile",
                "Palm" : "Mobile",
                "Open" : "Mobile",
                "Maemo" : "Mobile",
                "Verdict" : "Mobile",

            }
         agent = str(self.agent)
         slipt1 = agent.split(")")
         slipt1 = str(slipt1).split("(")
         slipt1 = str(slipt1).split(";")
         slipt1 = str(slipt1).replace('"', " ").split('"')
         splits = str(slipt1).replace("'", " ").split(' ')

         for key in splits:
            if len(key) > 0:
                if NAME.get(key, None) is not None:
                    self.info = {'OS': key}
                    info = {'Device': NAME.get(key, "UNKNOWN")}
                    break
                else:
                    self.info = {'OS': "UNKNOWN"}
                    info = {'Device': "UNKNOWN"}


            else:
                self.info = {'OS': "UNKNOWN"}
                info = {'Device': "UNKNOWN"}

         self.info.update(info)





class browser(Variable):

    def __getattr__(self, item):
        return item

    def __call__(self, *args, **kwargs):

        return None

    def __init__(self):
        if self.out('HTTP_USER_AGENT') !="":
            self.agent = self.out('HTTP_USER_AGENT')
        else:
            self.agent = None

        self.info = []
        self.name()
        self.name = self.info['Browser']
        self.version = self.info['Version']

    def name(self):
         NAME = {
                "Navigator": "Navigator",
                "Firefox": "Firefox",
                "Internet Explorer": "MSIE",
                "Chrome": "chrome",
                "Maxthon": "Maxthon",
                "Opera": "Opera",
                "OPR": "Opera",
                "Safari": "Safari",
                "Camino": "Camino",
                "SeaMonkey": "SeaMonkey",
                "K-Meleon": "K-Meleon",
                "Flock": "Flock",
                "Lunascape": "Lunascape",
                "Torch": "Torch",
                "Xtravo": "Xtravo",
                "Stainless": "Stainless",
                "Deepnet Explorer": "Deepnet",
                "QtWeb": "QtWeb",
                "CometBird": "CometBird",
                "xombrero": "xombrero",
                "Ultrabrowser": "Ultrabrowser",
                "Chromium": "Chromium",
                "Dooble": "Dooble"

            }
         agent = str(self.agent)
         slipt = agent.split(" ")
         for key in reversed(slipt):
             splits = key.split("/")

             if len(splits[0]) > 0 or len(splits[1]) > 0 :
                 if NAME.get(splits[0], None) is not None:
                     self.info = {'Browser': splits[0]}
                     info = {'Version': splits[1]}
                     break
                 else:
                     self.info = {'Browser': "UNKNOWN"}
                     info = {'Version': "UNKNOWN"}

             else:
                self.info = {'Browser': "UNKNOWN"}
                info = {'Version': "UNKNOWN"}


         self.info.update(info)