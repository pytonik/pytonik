# Author : BetaCodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by BetaCodings on 05/11/2019.
import os


class url:

    def __getattr__(self, item):
        return item

    def __call__(self, *args, **kwargs):

        return None

    def __init__(self, *args, **kwargs):
        self.ul = self.url(*args, **kwargs)
        return None

    def __str__(self):

        return self.ul


    def url(self, path = ""):

        http = os.environ.get("HTTPS")
        if http == 'on':
            url = str("https://") + os.environ.get("HTTP_HOST")
        else:
            url = str("http://") + os.environ.get("HTTP_HOST")

        DS = ""
        p = ""

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
