###
# Author : Betacodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by Betacodings on 2019.
###



import sys, os, cgitb
from pytonik import Version, Log
from pytonik.Config import Config
from pytonik.Core.env import env
from pytonik.Session import Session
from pytonik.util.Variable import Variable

cgitb.enable()
log_msg = Log.Log()


class Router(env, Config):
    def __getattr__(self, item):
        return item

    def __init__(self):
        osv = Variable()
        url = osv.out('REQUEST_URI', "")
        http_s = osv.out("HTTP_HOST")

        if osv.out("SERVER_SOFTWARE", "") == Version.AUTHOR:

            self.uri = url.split('/')[2:]

        else:
            if http_s == "127.0.0.1" or http_s == "localhost":
                self.uri = url.split('/')[2:]
            else:
                self.uri = url.split('/')[1:]

        self.add(self._e())

        self.controllers = self.get('default_controllers')
        self.actions = self.get('default_actions')
        self.languages = self.get('default_languages')
        self.alllanguages = self.get('languages', '')
        self.routes = self.get('default_routes')
        self.methodprefix = ""
        self.parameter = ""

        # if "?" in self.uri:

        # uri_paths = urlstr.split("?")
        # path_array = uri_paths[0]
        # else:
        # uri_paths = urlstr.split('/')
        # path_array = uri_paths[0]

        uri_paths = self.uri  # .split('/')

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

            # print(routes.keys())

            if Version.PYVERSION_MA < 3:
                path_parts = filter(None, path_parts)
            else:
                path_parts = list(filter(None, path_parts))

            routes = self.get('route', '')

            if list(set(path_parts).intersection(routes.keys())):

                for s in path_parts:

                    if s in routes:
                        self.routes = s

                        if self.routes in routes:
                            self.methodprefix = routes[self.routes]
                        else:
                            self.methodprefix = ""

                            # path_parts.append(path_parts.pop(-1))

            languages = self.get('languages', '')

            if list(set(path_parts).intersection(languages.keys())):

                for s in path_parts:
                    if s in languages:
                        self.languages = s
                        path_parts.append(path_parts.pop(-1))

            controllers = self.get('default_controllers', '')
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

            action = self.get('default_actions', '')
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

            if pathparts_paramarray == None or pathparts_paramarray == "":
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

                                        if (len(new_para) - i) > 0:
                                            v_para = new_para[i]
                                        else:
                                            v_para = ""

                                        list_params.append(param_n)
                                        list_params.append(v_para)

                                self.parameter = Helpers.covert_list_dict(list_params)


                else:
                    for s in path_parts:

                        if s is not self.controllers and s is not self.actions and s is not self.languages:
                            list_params.append(s)

                            path_parts.append(path_parts.pop(-1))

                    self.parameter = Helpers.covert_list_dict(list_params)

            else:

                self.parameter = pathparts_paramarrayOut

                path_parts.append(path_parts.pop(-1))

        return None

    def getUri(self):
        return self.uri

    def getControllers(self):

        return self.controllers

    def getAction(self):
        return self.actions

    def getParams(self):

        return self.parameter

    def getRoutes(self):

        return self.routes

    def getMethodPrefix(self):
        return self.methodprefix

    def getLanguages(self):
        return self.languages