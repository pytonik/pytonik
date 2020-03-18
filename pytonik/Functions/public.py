# Author : BetaCodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by BetaCodings on 09/11/2019.


from pytonik.Editor import HTMLeditor
from pytonik.Log import Log
from pytonik.App import App
import os
log_msg = Log()
Ap = App()

class public():

    def __getattr__(self, item):
        return item
    
    def __init__(self, *args, **kwargs):
        if len(args) > 0 or len(kwargs) > 0:
            if all(args) != False:
                self.pt = self.path(*args, **kwargs)
            else:
                self.pt = self.path(**kwargs)

        return None

    def __str__(self):

        return self.pt


    def path(self, path = ""):
        DS = str('/');

        if path == "/":
            DS = ""
        else:
            DS = "/"

        return DS + 'public' + DS + path

