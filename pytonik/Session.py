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

try:
    from http import cookies as cook
except Exception as err:
    import Cookie as cook

var_q = "HTTP_COOKIE"


class Session(Variable):

    def __init__(self):
        self.result = ""
        self.list_Str = []
        
    def has(self, key=None):

        if key in self.settings:
            return True
        else:
            return False

    def set(self, key="", value="", duration=3600, url="", path="/"):
        url_v = self.out("HTTP_HOST")+str(":")+str(self.out("SERVER_PORT", '')) if self.out("HTTP_HOST") == "localhost" or self.out("HTTP_HOST") == "127.0.0.1" else self.out("HTTP_HOST")
        url = url if url  != "" else url_v
        expires = datetime.datetime.utcnow(
        ) + datetime.timedelta(minutes=duration)  # minutes in 30 days
        if self.out("SERVER_SOFTWARE") == Version.AUTHOR:
            #cooKeys = cook.SimpleCookie(self.out(var_q))

            ##self.prheader("Set-cookie", cooKeys.output(header="", sep=""))
            ck = str(key)+"="+str(value)
            self.list(ck) 
            
            

        else:

            cooKeys = cook.SimpleCookie(self.out(var_q))

            cooKeys[str(key)] = value
            cooKeys[str(key)]['domain'] = url
            cooKeys[str(key)]['path'] = '/'
            cooKeys[str(key)]['expires'] = expires.strftime(
                '%a, %d %b %Y %H:%M:%S')
            #print(cooKeys)
            ck = str(key)+"="+str(value)
            self.list(ck) 

    def get(self, key=""):

        if self.out("SERVER_SOFTWARE") == Version.AUTHOR:

            #cooKeys = #cook.SimpleCookie()
            OsEnviron = self.out(var_q)
            if OsEnviron != "" or OsEnviron !=None:
                
                cooKeys = {}
                try:
                    for c_g in OsEnviron.split(";"):
                        k, v = c_g.split("=")
                        cooKeys.update({str(k):str(v)})
                except Exception as err:
                    try:
                        k, v = OsEnviron.split("=")
                        cooKeys.update({str(k):str(v)})
                    except Exception as err:
                         ""
                if cooKeys.get(key, "") != None or cooKeys.get(key, "") != "":
                    try:
                        return ast.literal_eval(cooKeys.get(key, ""))
                    except Exception as err:
                        return cooKeys.get(key, "")
                else:
                    
                    return ""
        else:
            cooKeys = cook.SimpleCookie()
            OsEnviron = self.out(var_q)

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

        if self.out("SERVER_SOFTWARE") == Version.AUTHOR:

            cooKeys = cook.SimpleCookie(self.out(var_q))
            if Version.PYVERSION_MA >= 3:
                cookv = cooKeys.iteritems()
            else:
                cookv = cooKeys.items()

            OsEnviron = self.out(var_q)
        else:
            cooKeys = cook.SimpleCookie(self.out(var_q))
            if Version.PYVERSION_MA >= 3:

                cookv = cooKeys.items()
            else:
                cookv = cooKeys.iteritems()

            OsEnviron = self.out(var_q)

        if var_q in self.see():
            if args:

                for key in args:
                    if self.get(key) != "":
                        return self.set(key, "", 60)
            else:
                for key, v in cookv:

                    if self.get(key) != "":
                        return self.set(key, "", 60)

        else:
            return False
    
    def list(self, list_s=""):
        if list_s  != "":
            list_v_c = []
           
            
            if "HTTP_COOKIE" not in self.see():
               
                try:
                
                    self.default("HTTP_COOKIE", list_s)
                except Exception as err:
                    return err
            else:
                
                
                self.list_Str.append(list_s)
                
                dl = dict({"HTTP_COOKIE": self.unqiue(self.list_Str)})
                
                self.update(dl)
                
        
    def unqiue(self, list_s):
       
        repl_cook = []
        for lcook in list_s:
            s_c = str(lcook)+";"+str(self.out("HTTP_COOKIE", ""))
            repl_cook.append(s_c)
       
        intial_cook = str(repl_cook).replace("[' ", "").replace("]", "").replace(',', ";").replace("'", "").replace("[", "")
        try:
            unique_l = intial_cook.split(";")
            ress = []
            [ress.append(x) for x in unique_l if x not in ress]
            return ";".join(ress)
        except Exception as err:
            return intial_cook
         
        