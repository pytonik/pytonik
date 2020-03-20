###
# Author : Betacodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by Betacodings on 2019.
###

from pytonik.App import App
from pytonik import Log
from pytonik.Driver.Schema import Schema
import sys
import os
import glob
import importlib
log_msg = Log.Log()


class Model(Schema):

    def __init__(self):
        ap = App()
        self.db = ap.DB() #this is database configuration from module App.py, but it is ignored by Schema.py

    # This Mothod 'load'  load module from model folder
    def load(self, m):

        if os.path.isdir(os.getcwd() + '/public'):
            host = os.getcwd()  # os.path.dirname(os.getcwd())

        else:
            host = os.path.dirname(os.getcwd())

        DS = str("/")

        paths = host + DS + 'model'
        model = paths + DS + m + ".py"
        sys.path.append(paths)
        importlib._RELOADING
        if os.path.isfile(model) == True:

            try:

                md = importlib.import_module(m)
                ob = getattr(md, m)
                if hasattr(ob(), '__call__'):
                    return ob()
                else:
                    log_msg.error("'%s' is not a callable" % m)

            except Exception as err:
                log_msg.error(err)
                self.App.header(0)

        else:

            log_msg.error("Model {e} does not exist ".format(m))



# This function 'auto' Auto load module from model folder
def auto():

    if os.path.isdir(os.getcwd() + '/public'):
        host = os.getcwd()  # os.path.dirname(os.getcwd())

    else:
        host = os.path.dirname(os.getcwd())

    DS = str("/")
    paths = host + DS + 'model'
    status = False
    for file in glob.glob(paths + "/*.py"):

        if os.path.isfile(file) == True:
            name = os.path.splitext(os.path.basename(file))[0]
            # Ignore __ files
            if name.startswith("__init__"):
                continue
            if name != "__init__":
                status = True

    if status == True:
        sys.path.append(paths)
