###
# Author : Betacodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by Betacodings on 2019.
###


import os
import datetime
import sys
import ast
from pytonik import Version
from pytonik.util.Variable import Variable

if Version.PYVERSION_MA >= 3:
    from http import cookies
else:
    import Cookie


class Session(Variable):
    def __init__(self):
        self.result = ""

    def has(self, key=None):

        if key in self.settings:
            return True
        else:
            return False

    def set(self, key="", value="", duration=3600, url="", path="/"):
        url = self.out("HTTP_HOST", "") if url == "" or url == None else url
        expires = datetime.datetime.utcnow(
        ) + datetime.timedelta(minutes=duration)  # minutes in 30 days

        if self.out("SERVER_SOFTWARE") == Version.AUTHOR:
            if Version.PYVERSION_MA >= 3:
                cooKeys = cookies.SimpleCookie(self.out('HTTP_SESSION'))
            else:
                cooKeys = Cookie.SimpleCookie(self.out('HTTP_SESSION'))
        else:
            if Version.PYVERSION_MA >= 3:
                cooKeys = cookies.SimpleCookie(self.out('HTTP_COOKIE'))
            else:
                cooKeys = Cookie.SimpleCookie(self.out('HTTP_COOKIE'))

        cooKeys[str(key)] = value
        cooKeys[str(key)]['domain'] = url
        cooKeys[str(key)]['path'] = '/'
        cooKeys[str(key)]['expires'] = expires.strftime(
            '%a, %d %b %Y %H:%M:%S')
        if self.out("SERVER_SOFTWARE", "") == Version.AUTHOR:
            self.put(session == cooKeys)
            return cooKeys
        else:
            print(cooKeys)

    def get(self, key=""):
        if Version.PYVERSION_MA >= 3:
            cooKeys = cookies.SimpleCookie()

        else:
            cooKeys = Cookie.SimpleCookie()

        if self.out("SERVER_SOFTWARE") == Version.AUTHOR:
            OsEnviron = self.out("HTTP_SESSION")
        else:
            OsEnviron = self.out("HTTP_COOKIE")

        if OsEnviron != None:
            cooKeys.load(OsEnviron)
            if key in cooKeys:
                if cooKeys[key].value != None:
                    try:
                        return ast.literal_eval(cooKeys[key].value)
                    except Exception as err:
                        return cooKeys[key].value

                else:
                    return ""
            else:
                return ""
        else:
            return ""

    def destroy(self, *args):
        var_q = ""
        if self.out("SERVER_SOFTWARE") == Version.AUTHOR:
            var_q = "HTTP_SESSION"
            if Version.PYVERSION_MA >= 3:
                cooKeys = cookies.SimpleCookie(self.out(var_q))
                cook = cooKeys.iteritems()
            else:
                cooKeys = Cookie.SimpleCookie(self.out(var_q))
                cook = cooKeys.items()

            OsEnviron = self.out(var_q)
        else:
            var_q = "HTTP_COOKIE"
            if Version.PYVERSION_MA >= 3:
                cooKeys = cookies.SimpleCookie(self.out(var_q))
                cook = cooKeys.items()
            else:

                cooKeys = Cookie.SimpleCookie(self.out(var_q))
                cook = cooKeys.iteritems()
            
            OsEnviron = self.out(var_q)
            
        if var_q in self.see():
            if args:

                for key in args:
                    if self.get(key) != "":
                        return self.set(key, "", 60)
            else:
                for key, v in cook:

                    if self.get(key) != "":
                        return self.set(key, "", 60)

        else:
            return False
