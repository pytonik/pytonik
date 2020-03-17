###
# Author : Betacodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by Betacodings on 2019.
###
import ast

class Config:


    def __init__(self, key=None, value=None):

        self.__key = key
        self.__value = value
        self.settings = {key : value}


    def add(self, key=None, value=None):

        try:
            if value is None:
                self.settings = key
            else:
                self.set(key, value)
        except Exception as err:
            print(err)

    def set(self, key=None, value=None):
        self.settings = {key : value}

    def get(self, key=None, empty=''):

        try:
            l = ast.literal_eval(self.settings)

            if str(key) in l:
                return l.get(key, empty)
            else:
                return ""
        except Exception as err:
            print(err)

