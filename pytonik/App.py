###
# Author : Betacodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by Betacodings on 2019.
###


from pytonik.Request import Request
from pytonik.Session import Session
from pytonik.Editor import HTMLeditor
from pytonik.Config import Config
from pytonik.Log import Log
from pytonik import Lang
from pytonik import Version
from pytonik.Core.env import env
from pytonik.util.Variable import Variable
from pytonik.Functions import url
from pytonik.Controllers import Controllers
import os
import sys
import cgi
import cgitb
import importlib
import glob
import  json
import inspect

cgitb.enable()

global host, u

if os.path.isdir(os.getcwd() + '/public'):
    host = os.getcwd()  # os.path.dirname(os.getcwd())

else:
    host = os.path.dirname(os.getcwd())

DS = str("/")
u = url

controllerpath = host + DS + 'controller'
error_page_class = controllerpath + DS + "ErrorController" + ".py"
header_response_page = {
    '301': 'error/page404',  # Bad Request
    '302': 'error/page404',  # Bad Request
    '307': 'error/page404',  # Bad Request
    '400': 'error/page400',  # Bad Request
    '404': 'error/page404',  # Not Found
    '405': 'error/page405',  # Method Not Allowed
    '500': 'error/',  # Internal Server Error

}


class App(env, Config, Variable):
    def __getattr__(self, item):
        return item

    def __init__(self, routers="", routes="", getpath="", getrouters=""):

        self.routers = routers
        self.routes = routes
        self.getpath = getpath
        self.codereponse = 200
        self.getrouters = getrouters
        self.getDB = ""
        self.Request = Request
        self.Session = Session
        self.methodprefix = ""
        self.actions = ""
        self.controllers = ""
        self.controller = ""
        self.dbDriver = None
        self.Config = None
        self.url = ""
        self.params = ""
        self.key = ""
        self.vpathf = ""
        self.languages = ""
        self.Driver = ""
        self.formData = None

    def getRouters(self):

        return self.routers

    def getPath(self):
        return self.getpath

    def runs(self, formData=None):

        self.formData = formData
        return self.initial()

    def initial(self):
        self.default("Framework", Version.AUTHOR)
        self.default("X-Version", Version.VERSION_TEXT)
        self.getrouters = self.envrin('route')
        self.controllers = Controllers()
        self.methodprefix = self.controllers._getMethodPrefix()
        self.actions = self.controllers._getActions()
        self.uri = self.controllers._getUri()
        self.controller = self.controllers._getControllers()
        self.routers = self.controllers._getRoutes()
        self.languages = self.controllers._getLanguages()
        self.params = self.controllers._getParams()

        langs = Lang.Lang(self.languages)
        langs.loadLang()

        controlUri = []


        if Version.PYVERSION_MA >= 3:
            lrounters = self.getrouters.items()
        else:
            lrounters = self.getrouters.iteritems()

        for k, getRouter in lrounters:

            if self.controller == k:
                controlUri = getRouter.split('@')

        self.routerend()

        if len(controlUri) != 0:

            if 'controller' in controlUri[0].lower():

                controllersClass = str(controlUri[0].lower()).replace(
                    'controller', '').capitalize() + 'Controller'
            else:
                controllersClass = str(
                    controlUri[0]).capitalize() + 'Controller'

            if ':' not in controlUri[1]:
                controllersMethods = str(controlUri[1])

            else:
                getMapPara = controlUri[1].split(':')

                controllersMethods = str(getMapPara[0])

        else:


            if str(self.controller[0]) == '?':

                controllersClass = 'IndexController'
            else:

                controllersClass = str(self.controller[0]).capitalize(
                ) + str(self.controller[1:]) + 'Controller'

            controllersMethods = str(self.actions)
        
        if controllersMethods != "":
            self.actions = controllersMethods

        controllers = controllerpath + DS + controllersClass + ".py"

        if os.path.isfile(controllers) == True:

            if __name__ == '__main__':
                spac = ""
            if os.path.isfile(controllers) == True:

                if sys.version_info.major <= 2:

                    return self.strClass(controllerpath, controllersClass)
                else:

                    return self.strClass3(controllerpath, controllersClass)

        else:
            Log(controllerpath).error(
                'Controller does not exist ' + str(controllersClass))
            return self.errorP('405')

    def errorP(self, code, replace=""):
        getErrorP = self.envrin('error')

        if os.path.isfile(host + DS + "routes.py") == True:
            sys.path.append(host)
            import routes as route

            if len(route.route.getError()) > 0:

                for i, redirect in enumerate(route.route.getError()):

                    if len(route.route.getError()) > 0:
                        toeroor = route.route.getError()[i]
                    if len(route.route.getErrorControl()) > 0:
                        fromroute = route.route.getErrorControl()[i]

                    if len(route.route.getCode()) > 0:
                        code = route.route.getCode()[i]

                    if len(route.route.getLink()) > 0:
                        link = route.route.getLink()[i]

                    if fromroute == self.controller:
                        return self.redirect(location=toeroor, link=bool(link), code=code)

        pageCode = "page{code}".format(code=code)
        if os.path.isdir(os.getcwd() + '/public'):
            if self.out("SERVER_SOFTWARE") == Version.AUTHOR:
                re_url = ""
                errorP = {}
                if getErrorP != '':
                    errorP = getErrorP

                if errorP.get(code, '') != '':

                    controllerP = ""
                    if '/' in errorP.get(code, ''):
                        splitP = errorP.get(code, '').split('/')
                        controllerP = controllerpath + DS + \
                            str(splitP[0]).capitalize() + 'Controller' + ".py"
                    else:
                        controllerP = controllerpath + DS + str(
                            errorP.get(code, '')).capitalize() + 'Controller' + ".py"

                    if code == "500":

                        if os.path.isfile(controllerP) == True:
                            re_url = u.url().url('/' + str(errorP.get(code, '')))
                        else:
                            re_url = u.url().url("/error")
                    else:
                        if os.path.isfile(controllerP) == True:
                            re_url = u.url().url('/' + str(errorP.get(code, '')))
                        else:

                            if os.path.isfile(self.error_page_html(code)) == True:
                                re_url = u.url().url(
                                    "/error/{code}".format(code=pageCode))

                else:
                    if code == "500":
                        re_url = u.url().url("/error")
                    else:

                        if os.path.isfile(self.error_page_html(code)) == True:
                            re_url = u.url().url(
                                "/error/{code}".format(code=pageCode))

                self.put(status=code)

                return code, re_url

        if getErrorP != '':

            errorP = getErrorP

            if errorP.get(code, '') != '':
                self.put(status=code)
                if '/' in errorP.get(code, ''):
                    splitP = errorP.get(code, '').split('/')
                    controllerP = controllerpath + DS + \
                        str(splitP[0]).capitalize() + 'Controller' + ".py"
                else:
                    controllerP = controllerpath + DS + str(
                        errorP.get(code, '')).capitalize() + 'Controller' + ".py"

                if os.path.isfile(controllerP) == True:
                    return self.redirect(u.url().url('/' + str(errorP.get(code, ''))))
                else:
                    if os.path.isfile(self.error_page_html(code)) == True:
                        return self.redirect(u.url().url("/error/{code}".format(code=pageCode)))

            else:

                if os.path.isfile(self.error_page_html(code)) == True:
                    return self.redirect(u.url().url("/error/{code}".format(code=pageCode)))
            self.default("REDIRECT_STATUS", 301)
            self.default("REDIRECT_REDIRECT_STATUS", 301)
        else:
            if os.path.isfile(error_page_class) == True:
                self.default("REDIRECT_STATUS", 301)
                self.default("REDIRECT_REDIRECT_STATUS", 301)
                return self.redirect(u.url().url("/error/{code}".format(code=pageCode)))

    def envrin(self, key):
        env = self._e()
        self.add(env)
        return self.get(key, '')

    def DB(self):

        self.dbDriver = self.envrin('dbConnect')
        if self.dbDriver.get("driver", '') == "MYSQL":
            from pytonik.Driver.DB.MYSQL.MYSQL import MYSQL
            self.getDB = MYSQL(self.dbDriver)
            self.Driver = "MYSQL"
            return self.getDB

        if self.dbDriver.get("driver", '') == "SQLite":
            from pytonik.Driver.DB.SQLite.SQLite import SQLite
            self.getDB = SQLite(self.dbDriver)
            self.Driver = "SQLite"
            return self.getDB

        if self.dbDriver.get("driver", '') == "Oracle":
            from pytonik.Driver.DB.Oracle.Oracle import Oracle
            self.getDB = Oracle(self.dbDriver)
            self.Driver = "Oracle"
            return self.getDB

        if self.dbDriver.get("driver", '') == "pyPgSQL":
            from pytonik.Driver.DB.pyPgSQL.pyPgSQL import pyPgSQL
            self.getDB = pyPgSQL(self.dbDriver)
            self.Driver = "pyPgSQL"
            return self.getDB

    def strClass(self, p=None, c=None):

        try:
            sys.path.append(p)
            ms = str(self.actions)
            md = importlib.import_module(c)
            self.default("REDIRECT_REDIRECT_STATUS", 200)
            self.default("REDIRECT_STATUS", 200)
            return self.strMethod(p, md, ms)

        except Exception as err:
            Log(p + DS + c + '.py').critical(err)

            return self.errorP('400')

    def strMethod(self, p, c=None, mv=None):
        Request = self.Request(prform=self.formData)
        Session = self.Session()
        try:
            m = mv.split("?")[0]
        except Exception as err:
            m = mv
        try:
            return getattr(c, m)(Request, Session)
        except Exception as err:
            try:
                return getattr(c, m)(Session, Request)
            except Exception as err:
                try:
                    return getattr(c, m)(Request)
                except Exception as err:
                    try:
                        return getattr(c, m)(Session)
                    except Exception as err:
                        try:
                            return getattr(c, m)()
                        except Exception as err:
                            Log(p + DS + c + '.py').critical(err)
                            return self.errorP('400')

    def strClass3(self, p=None, c=None):

        try:
            sys.path.append(p)
            ms = str(self.actions)
            importlib._RELOADING
            md = importlib.import_module(c, ms)
            self.default("REDIRECT_REDIRECT_STATUS", 200)
            self.default("REDIRECT_STATUS", 200)
            return self.strMethod(p, md, ms)

        except Exception as err:


            Log(p + DS + c + '.py').critical(err)
            return self.errorP('400')

    def redirect(self, location='/', link=False, code="307"):

        if self.out("SERVER_SOFTWARE") == Version.AUTHOR:

            if link == True:
                location_d = u.url().url(location)
            else:
                location_d = location
            self.put(status=code)
            self.put(redirect_url=location_d)
            return code, location_d
        else:

            if link == True:
                location_d = u.url().url(location)
            else:
                location_d = location

            self.default("REDIRECT_STATUS", code)
            self.default("REDIRECT_REDIRECT_STATUS", code)
            print("Location: {location}".format(location=location_d))
            print()

    def referer(self, location='/', link=False, code="307"):
        if self.out("SERVER_SOFTWARE") == Version.AUTHOR:
            if link == True:
                location_d = u.url().url(location)
            else:
                location_d = location
            self.put(status=code)
            self.put(referral=self.out('HTTP_REFERER', location_d))
            return code, self.out('HTTP_REFERER', location_d)
        else:
            if link == True:
                location_d = u.url().url(location)
            else:
                location_d = location
            self.default("REDIRECT_STATUS", code)
            self.default("REDIRECT_REDIRECT_STATUS", code)
            print("Location: {location}".format(
                location=self.out('HTTP_REFERER', location_d)))
            print()

    @staticmethod
    def header(p=0, type="text/html"):

        try:
            import imp
            imp.reload()
        except Exception:
            import importlib
            importlib.reload(sys)

        if os.path.isdir(os.getcwd() + '/public') == False:
            print("Content-type: {type}\r\n".format(type=type))  # \r\n\r\n
            if p > 0:
                for x in range(p):
                    print("")
        else:
            return

    def Jdumps(self, strings):

        try:
            return json.dumps(strings)
        except Exception as err:
            return strings

    def Jloads(self, strings):

        try:
            return json.loads(strings)
        except Exception as err:
            return strings


    def XHreponse(self, dataString, type=""):
        if self.out("SERVER_SOFTWARE") == Version.AUTHOR:
            return dataString
        else:
            self.header(type=type)
            print(dataString)

    def views(self, pathf="", datag={}, datal={}):

        if pathf == "":
            pathf = self.getDefaultViewPath()

        pathfhtml = host + DS + 'views' + DS + pathf + ".html"
        html = ""
        if os.path.isfile(pathfhtml) == False:
            Log(host + DS + 'views').critical('Cannot find file {}'.format(pathf + ".html"))

            return self.errorP('404')

        else:
            if os.path.isdir(os.getcwd() + '/public'):
                # print(os.environ)
                return self.read_html(host + DS + 'views' + DS, pathf, datag)

            else:
                self.header()
                
                print(self.read_html(host + DS + 'views' + DS, pathf, datag))

    def read_html(self, template_dir, engine, context=[]):

        html_file_path = os.path.join(template_dir, "%s.html" % engine)

        try:
            with open(html_file_path, encoding='utf-8') as html_file:
                html = html_file.read()
            
            return str('<!-- Pytonik -->')+HTMLeditor.Template(html).render(**context) + str(
                '\n<!-- Pytonik {} -->'.format(Version.VERSION_TEXT))

        except Exception as err:

            Log(template_dir + DS + engine + str('.html')).error(err)
            return

    def getDefaultViewPath(self):

        router = self.Router.getRoutes()  # Routers.getRoutes()

        if router == "":
            rout = ""
        controllerDirectory = self.Router.getControllers()

        templateName = str(self.Router.getMethodPrefix()) + \
            str(self.Router.getAction()) + '.html'

        return templateName

    def error_page_html(self, code):
        return host + DS + 'views' + DS + str(code) + ".html"

    def loadmodule(self):

        path = [os.path.dirname(__file__) + str("/") +
                str("Functions"), str(host) + str("/") + "model"]
        listpath = [path[0], path[1]]

        i = 0
        lclass = {}

        for pl in listpath:

            current_dir = os.path.join(pl)

            current_module_name = os.path.splitext(
                os.path.basename(current_dir))[0]

            for file in glob.glob(os.path.join(current_dir + "/*.py")):
                name = os.path.splitext(os.path.basename(file))[0]

                i = i + 1
                # Ignore __ files
                ++i
                if name.startswith("__init__"):
                    continue
                if name != "__init__":
                    lclass0 = {name: name}
                    lclass.update(lclass0)

        if Version.PYVERSION_MA <= 2:
            item = lclass.iteritems()
        else:
            item = lclass.items()
        result = {}
        for key, value in item:
            if value not in result.values():
                result[key] = value

        return result

    def routerend(self):
        if os.path.isfile(host + DS + "routes.py") == True:
            sys.path.append(host)
            import routes as route
            toroute, fromroute = "", ""
            
            if len(route.route.getRouter()) > 0:

                for i, redirect in enumerate(route.route.getCode()):
                    if len(route.route.getRediret()) > 0:
                        toroute = route.route.getRediret()[i]
                    if len(route.route.getDespatch()) > 0:
                        fromroute = route.route.getDespatch()[i]
                    if fromroute == self.controller:
                        
                        self.redirect(location=toroute,
                                      link=True, code=redirect)
                
                for i, route_c in enumerate(route.route.getRouter()):
                    
                    
                    
                    uri = self.uri
                    while("" in uri):
                        try:
                            uri.clear("")
                        except Exception as err:
                            uri.remove("")


                    if self.languages in uri:
                        uri.pop(0)

                    sltp  = str(route_c).split("/")
                    luri = ""
                    if len(uri) > 0:

                        luri = "/".join(uri[0:len(sltp)])

                    else:
                        luri = str(uri)
                    
                    if luri == route_c:
                        routes_l = route_c
                
                    
                        if len(route.route.getController()) > 0:
                            self.controller = route.route.getController()[i]

                        if len(route.route.getAction()) > 0:
                            self.actions = route.route.getAction()[i]

                        if len(route.route.getRouter()) > 0:
                            self.routers = route.route.getRouter()[i]
                        if len(route.route.getMethod()) > 0:
                            self.method = route.route.getMethod()[i]

                            if self.method != "":
                                if self.method != self.out("REQUEST_METHOD", ""):
                                    Log().error(str(str(self.controller).capitalize()) + "Controller/" + str(
                                        self.actions) + " Requires " + self.method)

                                    return self.errorP('400')
                        
