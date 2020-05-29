###
# Author : Betacodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by Betacodings on 2019.
###

import sys
import os
from pytonik import Version, Log
from pytonik.Config import Config
from pytonik.Core.env import env
from pytonik.Session import Session
from pytonik.util.Variable import Variable
from .Core import Helpers

h = Helpers

if os.path.isdir(os.getcwd() + '/public'):
    host = str(os.getcwd()).replace('\\', '/')  # os.path.dirname(os.getcwd())

else:
    host = str(os.path.dirname(os.getcwd())).replace('\\', '/')

DS="/"
class Controllers(env, Config):
    def __getattr__(self, item):
        return item

    def __init__(self):
        
        self.uri = self.url()
        
        self.add(self._e())

        self.controllers = self.get('default_controllers')
        self.actions = self.get('default_actions')
        self.default_controllers = self.get('default_controllers')
        self.default_actions = self.get('default_actions')

        self.languages = self.get('default_languages')
        self.all_languages = self.get('languages', '')
        self.routes = self.get('default_routes', "")
        self.methodprefix = ""
        self.parameter = ""

        path_parts = self.uri

        # Get parameter from Query String
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
                    pathparts_paramarray[name] = [
                        pathparts_paramarray[name], value]

                pathparts_paramarrayOut.setdefault(name, value)

        else:
            pathparts_paramarrayOut = ""

        if len(path_parts):

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

            if list(set(path_parts).intersection(self.all_languages.keys())):

                for s in path_parts:
                    if s in self.all_languages:
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

            # Get Path from URI / convert it to parameter
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

                                self.parameter = Helpers.covert_list_dict(
                                    list_params)

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

    def url(self):
        osv = Variable()
        url = osv.out('REQUEST_URI', "")
        http_s = osv.out("HTTP_HOST")
        uri = ""
        if osv.out("SERVER_SOFTWARE", "") == Version.AUTHOR:

            uri = url.split('/')[2:]

        else:

            if http_s == "127.0.0.1" or http_s == "localhost":
                uri = url.split('/')[2:]
            else:
                uri = url.split('/')[1:]
        return uri

    def _getUri(self):
        return self.uri

    def _getControllers(self):
        return self.controllers

    def _getActions(self):
        return self.actions

    def _getLanguages(self):
        return self.languages

    def _getParams(self):
        
        return self.get_routes_param(params=self.parameter)

    def _getMethodPrefix(self):

        return self.methodprefix

    def _getRoutes(self):
        return self.routes
    
    def get_routes_param(self, params):
            list_params = []
            if os.path.isfile(host + "/" + "routes.py") == True:
                sys.path.append(host)
                import routes as route

                
                for i, route_c in enumerate(route.route.getRouter()):
                        
                        uri = self.uri
                        while ("" in uri):
                            try:
                                uri.clear("")
                            except Exception as err:
                                uri.remove("")
                        
                        if self.languages in uri:
                            uri.pop(0)
                        
                        sltp = str(route_c).split("/")
                        luri = ""
                        if len(uri) > 0:

                            luri = "/".join(uri[0:len(sltp)])

                        else:

                            luri = str(uri)
                        
                        if self.controllers in route.route.getRouter():
                            
                            return self._getR_params(route.route.getParams())
                        else:
                            return self._getR_params(route.route.getParams())#route.route.getParams()[i]
                
                       
            else:
                return params

    def _getR_params(self, params):
        list_params = []
        parameter = {}
                
        
        new_uri = self._getUri()[1:]
        
        for i, para in enumerate(params):
            
            try:
                v_para = new_uri[i]
            except Exception as err:
                v_para = ""
            list_params.append(para)
            list_params.append(v_para)
            
            
        parameter = Helpers.covert_list_dict(list_params)
        return parameter
            