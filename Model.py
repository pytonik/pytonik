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
import sys, os, importlib
log_msg = Log.Log()



class Model(Schema):
    
    def __init__(self):
        ap = App()
        self.db = ap.DB()




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

    