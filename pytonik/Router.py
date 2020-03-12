###
# Author : Betacodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by Betacodings on 2019.
###



import sys, os, re
from pytonik import Version, Log
from pytonik.Config import Config
from pytonik.Core.env import env
from pytonik.Core import Helpers
from pytonik.Controllers import Controllers
from pytonik.util.Variable import Variable

log_msg = Log.Log()


class Router(env):
    def args(self, to="", params=[]):
        return to, params

    def __getattr__(self, item):
        return item

    def __init__(self):

        self.control = Controllers()
        self._route = []
        self._params = {}
        self._getcontrol = []
        self._getaction = []
        self._geturi = []
        self._redirect = []
        self._method = []
        self.route_to = []
        self._despatch = []
        self._code = []
        return None

    def get(self, uri, call=""):
        self._route_(route=uri, call=call, method="GET")
        return self

    def post(self, uri, call=""):
        self._route_(route=uri, call=call, method="POST")
        return self

    def put(self, uri, call=""):
        self._route_(route=uri, call=call, method="POST")
        return self

    def any(self, uri, call=""):
        self._route_(route=uri, call=call)
        return self

    def redirect(self, uri, to="", code=302):
        if to == "/":
            replace = self.control.default_controllers
        else:
            replace = to
        self._despatch.append(uri), self._redirect.append(replace), self._code.append(code)
        return self

    def permanentRedirect(self, uri, to="", code=301):
        if to == "/":
            replace = self.control.default_controllers
        else:
            replace = to

        self._despatch.append(uri), self._redirect.append(replace), self._code.append(code)
        return self


    def where(self, *args):

        if len(params) > 0:

            if isinstance(args[0], dict):
                if Version.PYVERSION_MA >= 3:

                    params = args[0].items()
                else:
                    params = args[0].iteritems()

                for k, v in params:
                    regex = re.compile(v)
                    if regex.match(self._params.get(k, "")):
                        return True
                    else:
                        return False

            elif isinstance(args, list):

                regex = re.compile(args[1])
                if regex.match(self._params.get(args[0], "")):
                    return True
                else:
                    return False

        else:
            return False


    def _route_(self, route="", call="", method=""):

        route = route.split('/')
        new_para = route

        parameter = {}
        replace = ""
        new_uri = []
        list_params = []
        params = ""

        new_paraf = []
        if self.control._getLanguages() in new_para:
            new_paraf = self.control._getUri()[1:]
            new_paraf.pop(-1)
        else:
            new_paraf = self.control._getUri()[2:]

        if self.control._getControllers() in new_paraf:
            new_paraf = self.control._getUri()
            new_paraf.pop(-1)

        if len(call) > 0:
            replace = call[0]
            params = call[1]

        if replace in route:

            new_uri = new_paraf

            for i, para in enumerate(params):

                if (len(new_uri) - i) > 0:
                    v_para = new_uri[i]
                else:
                    v_para = ""
                list_params.append(para)
                list_params.append(v_para)

            parameter = Helpers.covert_list_dict(list_params)
            self._params.update(parameter)

        if len(route) == 1:
            ctl = route[0] if route[0] != "" else self.control.default_controllers
            self._getcontrol.append(ctl)

            self._getaction.append(self.control.default_actions)
        elif len(route) > 1:
            self._getcontrol.append(route[0] if route[0] != "" else self.control.default_controllers)
            self._getaction.append(route[1] if route[1] != "" else self.control.default_actions)

        self._route.append(replace)
        self._method.append(method)

    def getParams(self):
        return self._params

    def getController(self):
        return self._getcontrol

    def getAction(self):
        return self._getaction

    def getRouter(self):
        return self._route

    def getMethod(self):
        return self._method

    def getRediret(self):
        return self._redirect

    def getDespatch(self):
        return self._despatch

    def getCode(self):
        return self._code
