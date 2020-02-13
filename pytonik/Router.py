###
# Author : Betacodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by Betacodings on 2019.
###



import sys, os, cgitb
from pytonik import Version, Config, Log
from pytonik.Session import Session
cgitb.enable()
url = os.environ.get('REQUEST_URI', os.environ.get('PATH_INFO'))
log_msg = Log.Log()


class Router:
    def __init__(self):
        urlstr = str(url)
        self.uri = urlstr.split('/')

        Conf = Config.Config()
        Conf.add(self.env())


        self.controllers = Conf.get('default_controllers')
        self.actions = Conf.get('default_actions')
        self.languages = Conf.get('default_languages')
        self.alllanguages = Conf.get('languages', '')
        self.routes = Conf.get('default_routes')
        self.methodprefix = ""
        self.params = ""



        #if "?" in self.uri:

            #uri_paths = urlstr.split("?")
            #path_array = uri_paths[0]
        #else:
            #uri_paths = urlstr.split('/')
            #path_array = uri_paths[0]

        uri_paths = urlstr.split('/')

        pathparts_array = uri_paths



        pathparts_paramarray = os.environ.get("QUERY_STRING", '')

        pathparts_paramarrayOut = dict()
        if pathparts_paramarray != '':
            pairs = pathparts_paramarray.split('&')

            pathparts_paramarray = pairs

            for i in pairs:

                name, value = i.split('=', 2)

                pathparts_paramarray = {name: value}

                if name in pathparts_paramarray:

                    pathparts_paramarray[name] = value

                else:
                    pathparts_paramarray[name] = [pathparts_paramarray[name], value]

                pathparts_paramarrayOut.setdefault(name, value)


        else:
            pathparts_paramarrayOut = ""

        path_parts = pathparts_array


        if len(path_parts):

            #print(routes.keys())

            if Version.PYVERSION_MA < 3:
                path_parts = filter(None, path_parts)
            else:
                path_parts = list(filter(None, path_parts))



            routes = Conf.get('route', '')

            if list(set(path_parts).intersection(routes.keys())):

                for s in path_parts:

                    if s in routes:
                        self.routes = s

                        if self.routes in routes:
                            self.methodprefix = routes[self.routes]
                        else:
                            self.methodprefix = ""

                        #path_parts.append(path_parts.pop(-1))


            languages = Conf.get('languages', '')


            if list(set(path_parts).intersection(languages.keys())):

                for s in path_parts:
                    if s in languages:
                        self.languages = s
                        path_parts.append(path_parts.pop(-1))


            controllers = Conf.get('default_controllers', '')
            if controllers:

                i = 0
                path_parts = list(filter(None, path_parts))

                for s in path_parts:

                    if s is not self.languages:
                        i += 1

                        if i == 1:
                            self.controllers = s
                            path_parts.append(path_parts.pop(-1))
                    ++i


            action = Conf.get('default_actions', '')
            if action:
                i = 0
                for s in path_parts:
                    if s is not self.controllers and s is not self.languages:
                        i += 1
                        if i == 1:
                            self.actions = s
                            path_parts.append(path_parts.pop(-1))
                        ++i


            from .Core import Helpers
            h = Helpers
            list_params = []

            if pathparts_paramarray == None or pathparts_paramarray == "" :
                if Version.PYVERSION_MA <= 2:
                    lroutes = routes.iteritems()
                else:
                    lroutes = routes.items()
                for k, getRouter in lroutes:

                    if self.controllers == k:

                        paraUri = getRouter.split('@')
                    else:
                        paraUri = []
                    if len(paraUri) > 0:
                        if ':' not in paraUri[1]:
                            getMapPara = []
                        else:
                            getMapPara = paraUri[1].split(':')


                        if self.controllers in routes:

                            if len(getMapPara[1:]) > 0:

                                new_para = path_parts[1:]

                                if len(new_para) > 0:
                                    param_m = []
                                    for i, para in enumerate(getMapPara[1:]):
                                        param_n = para
                                        v_para  = new_para[i]
                                        list_params.append(param_n)
                                        list_params.append(v_para)

                                self.params = Helpers.covert_list_dict(list_params)

                else:
                    for s in path_parts:

                        if s is not self.controllers and s is not self.actions and s is not self.languages:

                            list_params.append(s)

                            path_parts.append(path_parts.pop(-1))

                    self.params = Helpers.covert_list_dict(list_params)

            else:


                self.params = pathparts_paramarrayOut

                path_parts.append(path_parts.pop(-1))


        return None

    def getUri(self):
        return self.uri

    def getControllers(self):

        return self.controllers

    def getAction(self):
        return self.actions

    def getParams(self):

        return self.params

    def getRoutes(self):

        return self.routes

    def getMethodPrefix(self):
        return self.methodprefix

    def getLanguages(self):
        return self.languages


    def env(self):

        import os

        if os.path.isdir(os.getcwd() + '/public'):
            host = os.getcwd()  # os.path.dirname(os.getcwd())

        else:
            host = os.path.dirname(os.getcwd())

        DS = str("/")

        envpath = host + DS + ".env"

        if os.path.isfile(envpath) == True:

            try:
                f = open(envpath, "r")
                return f.read()
            except Exception as err:
                    log_msg.error(err)
        else:
            log_msg.critical(".env file not found")
            return ".env file not found"
