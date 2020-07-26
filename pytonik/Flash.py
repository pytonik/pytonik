###
# Author : Betacodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by Betacodings on 2029.
###
from pytonik.Session import Session
from pytonik.util.Variable import Variable
from pytonik.Controllers import Controllers
FSession = Session()
FVariable = Variable()
FControllers = Controllers()

class Flash:

    def __getattr__(self, item):
        return item

    def __init__(self):
        return 
        
    @staticmethod
    def message(message, showin="", key='flash'):
        option = {'msg': message, 'controller' : showin if showin != "" else "/".join(str(FVariable.out('HTTP_REFERER')).split('/')[3:])}  
        if FSession.has(key) == True:
            FSession.destroy(key)
            return FSession.set(key, option)
        else:
            return FSession.set(key, option)

    @staticmethod
    def display(key='flash'):
        if FSession.has(key) == True:
            option = dict(FSession.get(key))
            if option.get('controller') == "/".join(FControllers._getUri()):
                return option.get('msg')
            else:
                return ""
        else:
            return ""
    
    