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




class Session(Variable):

    def __getattr__(self, item):
        return item

    def __call__(self, *args, **kwargs):
        return None

    def __init__(self):
        self.result = ""
        self.s_string = "HTTP_COOKIE"
        self.session_list = []
        return None
        
    def has(self, key=""):

        session_dict = self.x_get()
        if len(session_dict) > 0:
            if session_dict.get(key, "") != "":
                return True
            elif session_dict.get(' {key}'.format(key=key), "") != "":
                return True
            else:
                return False
        else:
            return False

    def set(self, key="", value="", duration=3600, url="", path="/"):
        url_v = self.out("HTTP_HOST")+str(":")+str(self.out("SERVER_PORT", '')) if self.out("HTTP_HOST") == "localhost" or self.out("HTTP_HOST") == "127.0.0.1" else self.out("HTTP_HOST")
        url = url if url  != "" else url_v
        expires = datetime.datetime.utcnow() + datetime.timedelta(minutes=duration)  # minutes in 30 days

        if self.out("SERVER_SOFTWARE") == Version.AUTHOR:
            session_string = str(key)+"="+str(value)
            self.set_x(session_string) 
        else:

            cooKeys = cook.SimpleCookie(self.out(self.s_string))

            cooKeys[str(key)] = value
            cooKeys[str(key)]['domain'] = url
            cooKeys[str(key)]['path'] = '/'
            cooKeys[str(key)]['expires'] = expires.strftime('%a, %d %b %Y %H:%M:%S')

            print(cooKeys)



        
    def get(self, key=""):
        if self.out("SERVER_SOFTWARE") == Version.AUTHOR:
            session_dict = self.x_get()
            if len(session_dict) > 0:
                if session_dict.get(key, "") != None or session_dict.get(key, "") != "":
                    try:
                        return ast.literal_eval(session_dict.get(key, ""))
                    except Exception as err:
                        return session_dict.get(key, "")
                elif session_dict.get(' {key}'.format(key=key), "") != None or session_dict.get(' {key}'.format(key=key), "") != "":
                    try:
                        return ast.literal_eval(session_dict.get(' {key}'.format(key=key), ""))
                    except Exception as err:
                        return session_dict.get(' {key}'.format(key=key), "")
                else:
                    return ""
            else:
                return ""       
        else:
            cooKeys = cook.SimpleCookie()
            OsEnviron = self.out(self.s_string)
            
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

            session_result = self._delete(args)
            if session_result[0] == True:
                return self._reset(session_result[1])
            else:
                return False
            
        else:
            cooKeys = cook.SimpleCookie(self.out(self.s_string))
            if Version.PYVERSION_MA >= 3:

                cookv = cooKeys.items()
            else:
                cookv = cooKeys.iteritems()

            OsEnviron = self.out(self.s_string)

            if self.s_string in self.see():
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
    
    def set_x(self, session_string=""):
        if session_string  != "":
            if self.s_string not in self.see():
                self.default(self.s_string, session_string)
                
            else:
                self.session_list.append(session_string)
                self._update(self.unqiue(self.session_list))
        else:
            return False
                
                
    def _update(self, session_string):
        dict_session = dict({"HTTP_COOKIE": session_string})
        try:
            self.update(dict_session)
            return True
        except Exception as e:
            return False
        

    def unqiue(self, session_list=[]):
       
        session_relist = []
        for l_session in session_list:
            session_string = str(l_session)+";"+str(self.out("HTTP_COOKIE", ""))
            session_relist.append(session_string)
        initial_session = str(session_relist).replace("[' ", "").replace("]", "").replace(',', ";").replace("'", "").replace("[", "")
        return self._unquie(initial_session)

    def _unquie(self, initial_session=""):
        try:
            unique_session = initial_session.split(";")
            re_unique = []
            [ress.append(x) for x in unique_session if x not in re_unique]
            return ";".join(re_unique)
        except Exception as err:
            return initial_session    
        
    def _delete(self, session_key=tuple()):
        get_session = self.x_get()
        response = None
        if len(get_session) > 0: 
            if len(session_key) > 0:
                
                try:
                    for k in session_key:  
                        get_session.pop(k, None)
                    self._update(get_session)
                    response = True

                except Exception as err:
                    response = False 
            else:   
                try:
                    for k in dict(get_session):
                        get_session.pop(k, None)
                    response = True 
                except Exception as err:
                    response = False 
        else:
            response = False 
        return response, get_session

    def _reset(self, session_dict = dict()):

        session_list =  []
        if Version.PYVERSION_MA >= 3:
            session_dict_l = session_dict.items()
        else:
            session_dict_l = cooKsession_dicteys.iteritems()

        for k, v in session_dict_l:
            session_list.append("{k}={v}".format(k=k,v=v))
            
        return self._update(";".join(session_list))

    def x_get(self):

        session_dict = {}
        session_string = ""
        try:
            session_string = self.out(self.s_string)
        except Exception as err:

            session_dict = {}
        try:
            for c_g in session_string.split(";"):
                k, v = c_g.split("=")
                session_dict.update({str(k):str(v)})
        except Exception as err:
            try:
                k, v = session_string.split("=")
                session_dict.update({str(k):str(v)})
            except Exception as err:
                 session_dict = {}
        return session_dict