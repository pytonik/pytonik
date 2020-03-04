# Author : BetaCodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by BetaCodings on 05/11/2019.
import os
from pytonik.Router import Router
from pytonik.util.Variable import Variable
from pytonik import Version


class url(Variable):
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

        ront = Router()

        dev_path = ""

        seturl = str("localhost:") + str(os.environ.get("SERVER_PORT", ''))
        http = os.environ.get("HTTPS", "")

        if self.out("SERVER_SOFTWARE", "") == Version.AUTHOR:
            if http == 'on':
                url = str("https://") + seturl + str(
                    dev_path) + "/" + ront.alllanguages.get(ront.getLanguages(),
                                                            ront.getLanguages()) if lang is True else str(
                    "https://") + seturl + str(dev_path)
            else:
                url = str("http://") + seturl + str(dev_path) + "/" + ront.alllanguages.get(ront.getLanguages(),
                                                            ront.getLanguages()) if lang is True else str("http://") + seturl + str(dev_path)

        else:
            if http == 'on':
                url = str("https://") + os.environ.get("HTTP_HOST", seturl) + str(
                    dev_path) + "/" + ront.alllanguages.get(ront.getLanguages(),
                                                            ront.getLanguages()) if lang is True else str(
                    "https://") + os.environ.get("HTTP_HOST", seturl) + str(dev_path)
            else:
                url = str("http://") + os.environ.get("HTTP_HOST", seturl) + str(
                    dev_path) + "/" + ront.alllanguages.get(ront.getLanguages(),
                                                            ront.getLanguages()) if lang is True else str(
                    "http://") + os.environ.get("HTTP_HOST", seturl) + str(dev_path)

        DS, p = "", ""

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
