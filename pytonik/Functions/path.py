# Author : BetaCodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by BetaCodings on 05/11/2019.
import os

from pytonik.Functions.url import url
from pytonik.util.Variable import Variable
from pytonik import Version

if os.path.isdir(os.getcwd() + '/public'):
    host_public = str(os.getcwd()).replace('\\', '/') + '/public' # os.path.dirname(os.getcwd())
    host_app = str(os.path.dirname(os.getcwd())).replace("\\", "/") + '/app'
else:
    host_public = str(os.getcwd()).replace("\\", "/") 
    host_app = str(os.path.dirname(os.getcwd())).replace("\\", "/")




class path(url, Variable):
    def __getattr__(self, item):
        return item

    def __call__(self, *args, **kwargs):

        return None

    def __init__(self, *args, **kwargs):
        self.DS = "/"
        if len(args) > 0 or len(kwargs) > 0:
            if all(args) is not False:
                self.pt = self.path(*args, **kwargs)
            else:
                self.pt = self.path(**kwargs)

        return None

    def __str__(self):

        return self.pt

    def path(self, path="", link=False):
        
        u = ""

        dev_path = ""
        if path[:1] == self.DS or path[0] == self.DS:
            self.DS = ""
        else:
            self.DS = "/"
        
        if bool(link) == True:
            u = self.url()
        
        return str(u)+str(self.DS)+str(path)

    def exist(self, newpath, defaultpath="", link=False):
        path_res = ""
        if os.path.isfile(newpath) == True:
  
            path_res = self.path(path=newpath, link=link)

        elif os.path.isfile(host_app + self.DS + str(newpath)) == True:
   
            path_res = self.path(path=newpath, link=link)

        elif os.path.isfile(host_public + self.DS + str(newpath)) == True:

            path_res = self.path(path="/public/"+str(+newpath), link=link)

        elif os.path.isdir(newpath) == True:
            path_res =  newpath

        elif os.path.isdir(self.public(path=newpath)) == True:
            path_res =  self.public(path=newpath)

        else:
            
            if defaultpath != "":
                
                if os.path.isfile(defaultpath) == True:
                    path_res = self.path(path=defaultpath, link=link)

                elif os.path.isfile(host_app + self.DS + str(defaultpath)) == True:
                    
                    path_res = self.path(path=defaultpath, link=link)

                elif os.path.isfile(host_public + self.DS + str(defaultpath)) == True:
                    
                    path_res = self.path(path="/public/"+str(+defaultpath), link=link)

                elif os.path.isdir(defaultpath) == True:
                    path_res =  defaultpath

                elif os.path.isdir(self.public(defaultpath)) == True:
                    
                    path_res =  self.public(path=defaultpath)
        
        return path_res

    def public(self, path):
        if path[:1] == self.DS or path[:1] == self.DS:
            self.DS = ""
        else:
            self.DS = "/"

        return str(host_public) + self.DS + str(path)
