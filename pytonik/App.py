###
# Author : Betacodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by Betacodings on 2019.
###


from pytonik.Request import Request
from pytonik.Router import Router
from pytonik.Editor import HTMLeditor
from pytonik.Config import Config
from pytonik.Log import Log
from pytonik import Lang
from pytonik import Version
from pytonik.Functions import url
import os, sys, cgi, cgitb, importlib, glob, inspect
from http import HTTPStatus

cgitb.enable()

log_msg = Log()

global host, u



if os.path.isdir(os.getcwd()+'/public'):
    host = os.getcwd() #os.path.dirname(os.getcwd())

else:
    host = os.path.dirname(os.getcwd())


DS = str("/")
u = url
controllerpath = host + DS + 'controller'
error_page_class= controllerpath + DS + "ErrorController" + ".py"
header_response_page = {
   '400': 'error/page400', #Bad Request
   '404': 'error/page404', #Not Found
   '405': 'error/page405', #Method Not Allowed

}


class App(Router):


    def __init__(self, routers="", routes="", getpath="", getrouters=""):

        self.routers = routers
        self.routes = routes
        self.getpath = getpath
        self.getrouters = getrouters
        self.getDB = ""
        self.Router = Router
        self.Request = Request
        self.methodprefix = ""
        self.actions = ""
        self.controllers = ""
        self.routersc = ""
        self.dbDriver = None
        self.Config = None
        self.url = ""
        self.params = ""
        self.key = ""
        self.vpathf = ""
        self.languages = ""
        self.Driver = ""

    def getRouters(self):

        return self.routers

    def getPath(self):
        return self.getpath


    def runs(self):

        self.getrouters = self.envrin('route')
        self.routersc = self.Router()
        self.methodprefix = self.routersc.getMethodPrefix()
        self.actions = self.routersc.getAction()
        self.controllers = self.routersc.getControllers()
        self.routers = self.routersc.getRoutes()
        self.languages = self.routersc.getLanguages()
        self.params = self.routersc.getParams()


        langs = Lang.Lang(self.languages)
        langs.loadLang()
        routesUri = []
        for k, getRouter in self.getrouters.items():

            if self.controllers == k:
                routesUri = getRouter.split('@')


        if len(routesUri) != 0:


            if 'controller' in routesUri[0].lower():

                controllersClass =  str(routesUri[0].lower()).replace('controller', '').capitalize()+ 'Controller'
            else:
                controllersClass = str(routesUri[0]).capitalize() + 'Controller'

            if ':' not in routesUri[1]:
                controllersMethods = str(routesUri[1])

            else:
                getMapPara = routesUri[1].split(':')

                controllersMethods = str(getMapPara[0])



        else:

            if '?' is str(self.controllers[0]):

                controllersClass =  'IndexController'
            else:
                controllersClass = str(self.controllers[0].capitalize()) + str(self.controllers[1:])  + 'Controller'

            controllersMethods = str(self.actions)


        if controllersMethods != "":
            self.actions = controllersMethods


        controllers = controllerpath + DS + controllersClass + ".py"



        if os.path.isfile(controllers) == True:
            if __name__ == '__main__':
                spac = ""
            if os.path.isfile(controllers) == True:

                if sys.version_info.major <= 2:
                    self.strClass(controllerpath, controllersClass)
                else:
                    self.strClass3(controllerpath, controllersClass)

        else:

            self.errorP('405')



    def errorP(self, code="", replace = ""):
        getErrorP = self.envrin('error')

        pageCode = "page{code}".format(code=code)

        if getErrorP is not '':
            errorP = getErrorP

            if errorP.get(code, '') is not '':
               if '/' in  errorP.get(code, ''):
                    splitP = errorP.get(code, '').split('/')
                    controllerP = controllerpath + DS + str(splitP[0]).capitalize() + 'Controller'  + ".py"
               else:
                    controllerP = controllerpath + DS + str(errorP.get(code, '')).capitalize() + 'Controller'  + ".py"


               if os.path.isfile(controllerP) == True:
                   self.redirect(u.url().url('/'+str(errorP.get(code, ''))))

               else:

                   if  os.path.isfile(self.error_page_html(code)) == True:

                       self.redirect(u.url().url("/error/{code}".format(code=pageCode)))

                   else:
                       self.create_error_page(error_page_class)
                       self.redirect(u.url().url("/error/page{code}".format(code=code)))

            else:

                if  os.path.isfile(self.error_page_html(code)) == True:
                    self.redirect(u.url().url("/error/{code}".format(code=pageCode)))

                else:
                    self.create_error_page(error_page_class)
                    self.redirect(u.url().url("/error/{code}".format(code=pageCode)))

        else:
            if os.path.isfile(error_page_class) == True:
                self.redirect(u.url().url("/error/{code}".format(code=pageCode)))

            else:
                self.create_error_page(error_page_class)
                self.redirect(u.url().url("/error/{code}".format(code=pageCode)))





    def envrin(self,  key):
        env = self.env()
        self.Config = Config()
        self.Config.add(env)
        return self.Config.get(key, '')


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
            self.strMethod(md, ms)

        except Exception as err:
            log_msg.error(err)
            self.errorP('400')





    def strMethod(self, c=None, m=None):
        Request = self.Request()
        try:
            return getattr(c, m)(Request)
        except Exception as err:
            return getattr(c, m)()

    def strClass3(self, p=None, c=None):

        try:
            sys.path.append(p)
            ms = str(self.actions)
            importlib._RELOADING
            md = importlib.import_module(c, ms)
            self.strMethod(md, ms)

        except Exception as err:
            log_msg.error(err)
            self.errorP('400')


    def redirect(self, location='/'):
        print("Location: {location}".format(location=location))
        print()

    def referer(self, location='/'):
        print("Location: {location}".format(location=os.environ.get('HTTP_REFERER', location)))
        print()

    @staticmethod
    def header(p=0, type="text/html"):

        if Version.PYVERSION_MA <= 2 and Version.PYVERSION_MI <= 7:
            reload(sys)
            sys.setdefaultencoding('utf-8')
        elif Version.PYVERSION_MA == 3 and Version.PYVERSION_MI <= 3:
            import imp
            imp.reload()

        elif Version.PYVERSION_MA >= 3 and Version.PYVERSION_MI >= 4:
            import importlib
            importlib.reload(sys)
        print("Content-type: {type}\r\n".format(type=type))#\r\n\r\n
        if p > 0:
            for x in range(p):
                print("")

    def views(self, pathf="", datag={}, datal={}):

        if pathf == "":
            pathf = self.getDefaultViewPath()

        pathfhtml = host + DS + 'views' + DS + pathf + ".html"

        if os.path.isfile(pathfhtml) == False:
            self.errorP('404')
        else:
            self.header()
            self.read_html(host + DS + 'views' + DS, pathf, datag)

        return False

    def read_html(self, template_dir, engine, context=[]):

        html_file_path = os.path.join(template_dir, "%s.html" % engine)


        try:
            with open(html_file_path) as html_file:
                html = html_file.read()

            print(str('<!-- Pytonik -->\n')+ HTMLeditor.Template(html).render(**context) + str('\n<!-- Pytonik {} -->'.format(Version.VERSION_TEXT)))

        except Exception as err:
            log_msg.error(err)

    def getDefaultViewPath(self):

        router = self.Router.getRoutes()  # Routers.getRoutes()

        if router == "":
            rout = ""
        controllerDirectory = self.Router.getControllers()

        templateName = str(self.Router.getMethodPrefix()) + str(self.Router.getAction()) + '.html'

        return templateName

    def error_page_html(self, code):
        return host+DS+'views'+DS+str(code)+".html"

    def create_error_page(self, error_page_class):


        try:
            python_writer_code = ""
            for code in header_response_page:
                if os.path.isfile(self.error_page_html(code)) == False:
                    f = open(self.error_page_html(code), 'a+')
                    f.write("<h1> {code}  Not Found</h1>".format(code=code))
                    f.close()
                    python_writer_code += """\ndef page{code} ():\n""".format(code=code)
                    python_writer_code += """\n    data = {'title': 'pytonik"""
                    python_writer_code += """ {code} """.format(code=code)
                    python_writer_code += """'}\n\n"""
                    python_writer_code += """    m.views('{code}', data)\n""".format(code=code)



            writer_code = """from pytonik import Web
                              \nm = Web.App()
                              \ndef index():
                              \n  m.header()
                              \n  print("do work here") \n
                            """
            code_line = str(writer_code)+str(python_writer_code)
            f = open(error_page_class, 'w')
            f.write(code_line)
            f.close()

        except Exception as err:
            log_msg.error(err)

    def loadmodule(self):

        path = [os.path.dirname(__file__)+ str("/") +str("Functions"), str(host) + str("/") + "model"]
        listpath = [path[0], path[1]]


        i = 0
        lclass = {}

        for pl in listpath:

            current_dir = os.path.join(pl)

            current_module_name = os.path.splitext(os.path.basename(current_dir))[0]

            for file in glob.glob(os.path.join(current_dir + "/*.py")):
                name = os.path.splitext(os.path.basename(file))[0]

                i = i + 1
                # Ignore __ files
                ++i
                if name.startswith("__init__"):
                    continue
                if name is not "__init__":
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
