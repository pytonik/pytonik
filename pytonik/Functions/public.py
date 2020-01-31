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

        return  None

    def path(self, public = ""):
        DS = str('/');

        if public == "/":
            DS = ""
        else:
            DS = "/"
        return DS + 'public' + DS + value

