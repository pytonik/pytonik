# Author : BetaCodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by BetaCodings on 05/11/2019.
import os

class path:

    def __getattr__(self, item):
        return item

    def __call__(self, *args, **kwargs):

        return None

    def __init__(self, *args,  **kwargs):
        if len(args) > 0 or len(kwargs) > 0:
            if all(args) is not False:
                self.pt = self.path(*args,  **kwargs)
            else:
                self.pt = self.path(**kwargs)

        return None

    def __str__(self):

        return self.pt

    def path(self, path = "", link = False):

        DS = str('/')
        u = ""
        if path[:1] == DS or path[:1] == DS:
            DS = ""
        else:
            DS = "/"


        if bool(link) is True:
            u = self.url()


        return u + DS + path



    def url(self):
        http = os.environ.get("HTTPS")
        if http == 'on':
            url = str("https://") + os.environ.get("HTTP_HOST")
        else:
            url = str("http://") + os.environ.get("HTTP_HOST")

        return url



