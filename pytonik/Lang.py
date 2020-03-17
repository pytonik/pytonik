###
# Author : Betacodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by Betacodings on 2019.
###

import os
from pytonik import Log
from pytonik import Version
from pytonik.Controllers import Controllers
from pytonik import Router
import ast

log_msg = Log.Log()


class Lang:

    def __init__(self, lg):
        self.data = ""
        self.lg = lg
        

    def loadLang(self):
        if os.path.isdir(os.getcwd() + '/public'):
            host = os.getcwd()  # os.path.dirname(os.getcwd())

        else:
            host = os.path.dirname(os.getcwd())

        DS = str("/")
        ront = Controllers()
        getl = ront.all_languages
        
        langpath = host + DS + 'lang'+DS + \
            getl.get(self.lg.lower(), self.lg.lower()) + ".py"
        
        try:
            if os.path.isfile(langpath) == True:

                with open(langpath, 'rb') as rb:
                    self.data = rb.read().decode('utf-8')
                
                return self.data

        except Exception as e:
            log_msg.error("Lang file not found {}".format(e))
            return "Lang file not found {}".format(e)

    def get(self, key, defindValue=''):

        data = ast.literal_eval(self.data)

        return data.get(key.lower(), defindValue)
