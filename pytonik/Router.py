###
# Author : Betacodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by Betacodings on 2019.
###


import sys
import os
import re
from pytonik import Version, Log
from pytonik.Config import Config
from pytonik.Core.env import env
from pytonik.Core import Helpers
from pytonik.Controllers import Controllers
from pytonik.util.Variable import Variable

log_msg = Log.Log()


class Router(env):
    def args(self, to="", params=[], link=False, code=200):
        return to, params, link, code

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
        self._getmethod = []
        self._despatch = []
        self._code = []
        self._error = []
        self._geterrocontrol = []
        self._link = []
        return None

    def get(self, uri, call=""):

        if call != "":
            if isinstance(call, tuple):
                self._route_(route=uri, call=call, method="GET")
            else:
                lcall = []
                method_v, control_v = "", ""

                if len(call.split('@')) > 0:
                    control = call.split('@')
                    if len(control) == 2:
                        control_v = str(control[0]).lower().replace(
                            'Controller', '').replace('controller', '')
                        if len(str(control[1]).split(":")) > 0:
                            method_v = control[1].split(":")[0]
                            param = control[1].split(":")[1:]
                            lcall.append(uri)
                            lcall.append(param)
                        else:
                            method_v = control[1]
                    else:

                        if control[0] == "/":
                            control_v = self.control.default_controllers
                        else:
                            control_v = str(control[0]).lower().replace(
                                'Controller', '').replace('controller', '')

                        method_v = self.control.default_actions
                    lroute = str(control_v)+"/"+str(method_v)

                    self._route_(route=lroute, call=lcall, method="GET")

        return self

    def post(self, uri, call=""):
        if call != "":
            if isinstance(call, tuple):
                self._route_(route=uri, call=call, method="POST")
            else:
                lcall = []
                method_v, control_v = "", ""
                if len(call.split('@')) > 0:
                    control = call.split('@')
                    if len(control) == 2:
                        control_v = str(control[0]).lower().replace(
                            'Controller', '').replace('controller', '')
                        if len(str(control[1]).split(":")) > 0:
                            method_v = control[1].split(":")[0]
                            param = control[1].split(":")[1:]
                            lcall.append(uri)
                            lcall.append(param)
                        else:
                            method_v = control[1]
                    else:
                        if control[0] == "/":
                            control_v = self.control.default_controllers
                        else:
                            control_v = str(control[0]).lower().replace(
                                'Controller', '').replace('controller', '')

                        method_v = self.control.default_actions
                    lroute = str(control_v)+"/"+str(method_v)

                    self._route_(route=lroute, call=lcall, method="POST")
        return self

    def put(self, uri, call=""):
        if call != "":
            if isinstance(call, tuple):
                self._route_(route=uri, call=call, method="POST")
            else:
                lcall = []
                method_v, control_v = "", ""
                if len(call.split('@')) > 0:
                    control = call.split('@')
                    if len(control) == 2:
                        control_v = str(control[0]).lower().replace(
                            'Controller', '').replace('controller', '')
                        if len(str(control[1]).split(":")) > 0:
                            method_v = control[1].split(":")[0]
                            param = control[1].split(":")[1:]
                            lcall.append(uri)
                            lcall.append(param)
                        else:
                            method_v = control[1]
                    else:
                        if control[0] == "/":
                            control_v = self.control.default_controllers
                        else:
                            control_v = str(control[0]).lower().replace(
                                'Controller', '').replace('controller', '')

                        method_v = self.control.default_actions
                    lroute = str(control_v)+"/"+str(method_v)

                    self._route_(route=lroute, call=lcall, method="POST")
        return self

    def any(self, uri, call=""):
        if call != "":
            if isinstance(call, tuple):
                self._route_(route=uri, call=call)
            else:
                lcall = []
                method_v, control_v = "", ""
                if len(call.split('@')) > 0:
                    control = call.split('@')
                    if len(control) == 2:
                        control_v = str(control[0]).lower().replace(
                            'Controller', '').replace('controller', '')
                        if len(str(control[1]).split(":")) > 0:
                            method_v = control[1].split(":")[0]
                            param = control[1].split(":")[1:]
                            lcall.append(uri)
                            lcall.append(param)
                        else:
                            method_v = control[1]
                    else:
                        if control[0] == "/":
                            control_v = self.control.default_controllers
                        else:
                            control_v = str(control[0]).lower().replace(
                                'Controller', '').replace('controller', '')

                        method_v = self.control.default_actions
                    lroute = str(control_v)+"/"+str(method_v)

                    self._route_(route=lroute, call=lcall)
        return self

    def error(self, uri, call="", code=302):
        if isinstance(call, tuple):
            if call[0] == "/":
                replace = self.control.default_controllers
            else:
                replace = call[0]
            code = code if int(call[3]) == int(200) else call[3]
        else:
            if call[0] == "/":
                replace = self.control.default_controllers
            else:
                replace = call
            code = int(code)

        self._geterrocontrol.append(uri)
        self._link.append(call[2])
        self._error.append(replace)
        self._code.append(code)

        return self

    def redirect(self, uri, call="", code=302):

        if isinstance(call, tuple):
            if call[0] == "/":
                replace = self.control.default_controllers
            else:
                replace = call[0]
            code = code if int(call[3]) == int(200) else call[3]
        else:
            if call == "/":
                replace = self.control.default_controllers
            else:
                replace = call
            code = int(code)

        self._despatch.append(uri)
        self._redirect.append(replace)
        self._code.append(code)

        return self

    def permanentRedirect(self, uri, call="", code=301):
        if isinstance(call, tuple):
            if call[0] == "/":
                replace = self.control.default_controllers
            else:
                replace = call[0]
            code = code if int(call[3]) == int(200) else call[3]
        else:
            if call == "/":
                replace = self.control.default_controllers
            else:
                replace = call
            code = int(code)

        self._despatch.append(uri)
        self._redirect.append(replace)
        self._code.append(code)
        return self

    def where(self, *args):

        if len(args) > 0:

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
        if self.control.languages in self.control._getUri():

            new_paraf = self.control._getUri()[1:]
            new_paraf.pop(0)
        else:
            new_paraf = self.control._getUri()[1:]



        if self.control._getControllers() in new_paraf:
            new_paraf = self.control._getUri()
            new_paraf.pop(-1)


        if len(call) > 0:
            replace = call[0]
            params = call[1]


        uri = self.control._getUri()

        while ("" in uri):
            try:
                uri.clear("")
            except Exception as err:
                uri.remove("")

        if self.control.languages in uri:
            uri.pop(0)

        if len(replace) > 0:
            sltp = str(replace).split("/")
        elif len(uri) > 1:
             uri.pop(0)
             uri.pop(0)
             sltp = ""
        else:
            sltp = ""


        luri, para_v = "", ""

        if len(uri) > 0:
            para_v = "/".join(uri[len(sltp):])

        new_uri = para_v.split("/")


        if len(uri) > 0:
            luri = "/".join(uri[0:len(sltp):])

        parameter = {}
        for i, para in enumerate(params):

            if len(new_uri) > 0:

                if luri == replace :
                    if len(para) > 0:
                        list_params.append(para)

                        try:
                            v_para = new_uri[i]
                        except Exception as err:
                            v_para = ""

                        list_params.append(v_para)

                elif replace == "":

                    if len(para) > 0:
                        list_params.append(para)

                        try:
                            v_para = new_uri[i]
                        except Exception as err:
                            v_para = ""

                        list_params.append(v_para)


                parameter = Helpers.covert_list_dict(list_params)
        self._params.update(parameter)



        if len(route) == 1:
            ctl = route[0] if route[0] != "" else self.control.default_controllers
            self._getcontrol.append(ctl)
            act = self.control.default_actions
            self._getaction.append(act)
        elif len(route) > 1:
            ctl = route[0] if route[0] != "" else self.control.default_controllers
            self._getcontrol.append(ctl)

            act = route[1] if route[1] != "" else self.control.default_actions
            self._getaction.append(act)


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

    def getError(self):
        return self._error

    def getLink(self):
        return self._link

    def getErrorControl(self):
        return self._geterrocontrol
