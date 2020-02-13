# Author : BetaCodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by BetaCodings on 05/11/2019.
import os

from pytonik.Functions.url import url
class path(url):

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




    def exit(self, newpath, defaultpath = ""):

        if os.path.isfile(newpath) == True:
            return newpath

        elif os.path.isfile(self.public(newpath)) == True:
            return self.public(newpath)

        elif os.path.isdir(newpath) == True:
            return newpath

        elif os.path.isdir(self.public(newpath)) == True:
            return self.public(newpath)

        else:
            if defaultpath is not "":

                if os.path.isfile(defaultpath) == True:
                    return defaultpath
                elif os.path.isfile(self.public(defaultpath)) == True:
                    return self.public(defaultpath)
                elif os.path.isdir(defaultpath) == True:
                    return defaultpath
                elif os.path.isdir(self.public(defaultpath)) == True:
                    return self.public(defaultpath)
            else:
                return False

    def public(self, path):

        if os.path.isdir(os.getcwd() + '/public'):
            host = str(os.getcwd()) + '/public'  # os.path.dirname(os.getcwd())

        else:
            host = str(os.path.dirname(os.getcwd())) + '/public'
        DS = str('/')

        if path[:1] == DS or path[:1] == DS:
            DS = ""
        else:
            DS = "/"

        return str(host) + DS + str(path)


