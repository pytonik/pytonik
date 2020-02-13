###
# Author : Betacodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by Betacodings on 2019.
###


import os, datetime, sys, ast
from pytonik import Version

if Version.PYVERSION_MA <= 3 and  Version.PYVERSION_MI < 7:
    import Cookie
else:
    from http import cookies


class Session:
    def __init__(self):
            self.result = ""


    def has(self, key=None):

        if key in self.settings:
            return True
        else:
            return False

    def set(self, key="", value="", duration = 3600, url=os.environ.get("HTTP_HOST"), path="/"):
        expires = datetime.datetime.utcnow() + datetime.timedelta(minutes=duration)  # minutes in 30 days

        if Version.PYVERSION_MA >= 3:
            cooKeys = cookies.SimpleCookie(os.environ.get('HTTP_COOKIE'))
        else:
            cooKeys = Cookie.SimpleCookie(os.environ.get('HTTP_COOKIE'))

        cooKeys[str(key)] = value
        cooKeys[str(key)]['domain'] = url
        cooKeys[str(key)]['path'] = '/'
        cooKeys[str(key)]['expires'] = expires.strftime('%a, %d %b %Y %H:%M:%S')
        print(cooKeys)

    def get(self, key=""):
        if Version.PYVERSION_MA >= 3:
            cooKeys = cookies.SimpleCookie()

        else:
            cooKeys = Cookie.SimpleCookie()

        OsEnviron = os.environ.get("HTTP_COOKIE")
        if OsEnviron is not None:
            cooKeys.load(OsEnviron)
            if key in cooKeys:
                if cooKeys[key].value is not None:
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
        if Version.PYVERSION_MA >= 3:
            cooKeys = cookies.SimpleCookie(os.environ.get('HTTP_COOKIE'))
            cook = cooKeys.items()
        else:

            cooKeys = Cookie.SimpleCookie(os.environ.get('HTTP_COOKIE'))
            cook = cooKeys.iteritems()

        if "HTTP_COOKIE" in os.environ:
            if args:

                for key in args:

                    if self.get(key) is not "":
                        return self.set(key, "", 60)
            else:
                for key, v in cook:

                    if self.get(key) is not "":
                        return self.set(key, "", 60)

        else:
            return False
