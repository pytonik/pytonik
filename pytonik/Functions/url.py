# Author : BetaCodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by BetaCodings on 05/11/2019.
import os
from pytonik.Router import Router
from pytonik import Version


class url(Router):
    def __getattr__(self, item):
        return item

    def __call__(self, *args, **kwargs):

        return None

    def __init__(self, *args, **kwargs):
        if len(args) > 0 or len(kwargs) > 0:
            if all(args) is not False:
                self.ul = self.url(*args, **kwargs)
            else:
                self.ul = self.url(**kwargs)
        else:
            self.ul = self.url('')
        return None

    def __str__(self):

        return self.ul

    def url(self, path="", lang=False):

        DS, p = "", ""
        seturl = self.out("HTTP_HOST")+str(":")+str(self.out("SERVER_PORT", '')) if self.out("HTTP_HOST") == "localhost" or self.out("HTTP_HOST") == "127.0.0.1" else self.out("HTTP_HOST")
        if self.out("HTTPS", "") == 'on':
            url = str("https://") + seturl + "/" + self.alllanguages.get(self.getLanguages(), self.getLanguages()) if lang == True else str(
                    "https://") + seturl 
        else:
            url = str("http://") + seturl+ "/" + self.alllanguages.get(self.getLanguages(), self.getLanguages()) if lang == True else str("http://") + seturl

        if path == "":
            DS = ""
        else:

            if path[:1] == "/":
                p = path[1:]
                DS = "/"
            else:
                p = path
                DS = "/"

        return url + DS + p
