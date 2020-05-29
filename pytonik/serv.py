import cgitb
import base64
import traceback
import cgi
import ssl
import argparse
import locale
import os
import re
import sys
import time
import json
import warnings
from pytonik.cmd import lang
from pytonik import Version
from pytonik.util.Variable import Variable
from typing import Any, Callable, Dict, List, Pattern, Union
from pytonik.cmd.console import (  # type: ignore
    colorize, bold, red, green, turquoise, nocolor, color_terminal
)

try:
    from http import cookies as cook
except Exception as err:
    import Cookie as cook

from socketserver import ThreadingMixIn

try:
    from BaseHTTPServer import BaseHTTPRequestHandler
except Exception as err:
    from http.server import BaseHTTPRequestHandler, HTTPServer
try:
    import socket
except Exception as err:
    from socket import socket

try:
    import http.client as htp
    from http import client
    import urllib as urllib
except Exception as err:
    import httplib as htp
    import urllib2 as urllib

varb = Variable()


def run(host="", path="", port=6060, server_pro="HTTP/1.1", ssl_ip="", ssl_port="", pr=False):
    server = HTTPServer

    path = str(path).replace(
        "\\", "/") if path != "" else str(os.getcwd()).replace("\\", "/")

    spes = "/"
    vpath = ""

    try:
        import imp as im
    except Exception as err:
        import importlib as im

    mimetype = ""
    sys.path.insert(0, os.path.dirname(__file__))
    os.chdir(path)

    cookie_v = cook

    class httpv(BaseHTTPRequestHandler):

        def do_GET(self):

            path_info = self.path
            
            
            form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={
                    'REQUEST_METHOD': "GET",
                    'CONTENT-TYPE': self.headers['Centent-Type']
                }
            )
            if self.path == spes:
                if os.path.isfile(str(path) + spes + "public" + spes + "index.py") == True:
                    vpath = "public" + spes + "index.py"

                elif os.path.isfile(str(path) + spes + "public" + spes + "home.py") == True:
                    vpath = "public" + spes + "home.py"
                elif os.path.isfile(str(path) + spes + "public" + spes + "default.py") == True:
                    vpath = "public" + spes + "default.py"

                App = im.load_source('App.App', path + spes + vpath)
                mimetype = 'text/html'
                if "." not in path_info :
                    
                    
                    App.App.put(method="GET", accept_lang=self.headers["Accept-Language"],
                            http_connect=self.headers["Connection"], http_user_agt=self.headers["User-Agent"],
                            http_encode=self.headers["Accept-Encoding"], path=path, host=host, port=port,
                            para=path_info, remoter_addr=self.client_address[
                                0], remoter_port=self.client_address[1],
                            script_file=str(
                                path) + str(spes) + (vpath), server_proto=server_pro, server_ver=self.server_version,
                            protocol_ver=self.protocol_version)
                    runs_response = App.App.runs(formData=form)
                    if isinstance(runs_response, tuple) == True:

                        if str(runs_response[0]) == "404" or str(runs_response[0]) == "405" or str(
                                runs_response[0]) == "400":

                            self.error(runs_response[0], runs_response[1])

                        elif str(runs_response[0]) == "307":

                            self.redirect(runs_response[0], runs_response[1])
                        else:

                            self.rendering(mimetype=mimetype,
                                        content=runs_response)

                    else:
                        self.rendering(mimetype=mimetype, content=runs_response)

            elif self.path != spes:

                if "." not in str(self.path):

                    if str(self.path) != "":
                        if os.path.isfile(str(path) + spes + "public" + spes + "index.py") == True:
                            vpath = "public" + spes + "index.py"

                        elif os.path.isfile(str(path) + spes + "public" + spes + "home.py") == True:
                            vpath = "public" + spes + "home.py"

                        elif os.path.isfile(str(path) + spes + "public" + spes + "default.py") == True:

                            vpath = "public" + spes + "default.py"

                        App = im.load_source('App.App', path + spes + vpath)
                        mimetype = 'text/html'
                        if "." not in path_info:
                            
                            
                            App.App.put(method="GET", accept_lang=self.headers["Accept-Language"],
                                        http_connect=self.headers["Connection"], http_user_agt=self.headers["User-Agent"],
                                        http_encode=self.headers["Accept-Encoding"], path=path, host=host, port=port,
                                        para=path_info, remoter_addr=self.client_address[0],
                                        remoter_port=self.client_address[1], script_file=str(
                                path) + str(spes) + (vpath), server_proto=server_pro, server_ver=self.server_version,
                                protocol_ver=self.protocol_version)

                            runs_response = App.App.runs(formData=form)
                            if isinstance(runs_response, tuple) == True:

                                if str(runs_response[0]) == "404" or str(runs_response[0]) == "405" or str(
                                        runs_response[0]) == "400":

                                    self.error(runs_response[0], runs_response[1])

                                elif str(runs_response[0]) == "307":

                                    self.redirect(
                                        runs_response[0], runs_response[1])
                                else:

                                    self.rendering(mimetype=mimetype,
                                                content=runs_response)

                            else:
                                self.rendering(mimetype=mimetype,
                                            content=runs_response)

            if self.path.endswith('favicon.ico'):
                return
            try:
                for mime in Version.MIME_TYPES:
                    if self.path.endswith(mime['ext']):
                        self.rendering(
                            path=path, mimetype=mime['type'], mode=mime['mode'], code=200)
                    else:
                        split_path = str(self.path).split('?')
                        if split_path[0].endswith(mime['ext']):
                            self.rendering(
                            path=path, mimetype=mime['type'], mode=mime['mode'], code=200)


            except Exception as err:
                if self.path.endswith(self.path):
                    if os.path.isfile(str(path) + spes + "public" + spes + "index.py") == True:
                        vpath = "public" + spes + "index.py"

                    elif os.path.isfile(str(path) + spes + "public" + spes + "home.py") == True:
                        vpath = "public" + spes + "home.py"

                    elif os.path.isfile(str(path) + spes + "public" + spes + "default.py") == True:
                        vpath = "public" + spes + "default.py"

                    App = im.load_source('App.App', path + spes + vpath)
                    code = "500"
                    App.App.put(status=code)
                    pth = str(os.path.dirname(
                        os.path.abspath(__file__))).replace("\\", "/")
                    f = open(pth + "/cmd/errd/index.html", "r")
                    content = str(f.read()).format(code=code, name=Version.AUTHOR, message=Version.HTTP_CODE.get(
                        code, ""), version=Version.VERSION_TEXT)
                    self.wfile.write(bytes(str(content).encode()))

        def do_POST(self):
            path_info = self.path
           
            form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={
                    'REQUEST_METHOD': "POST",
                    'CONTENT-TYPE': self.headers['Content-Type']
                }
            )

            # text/plain; charset=utf-8
            if os.path.isfile(str(path) + spes + "public" + spes + "index.py") == True:
                vpath = "public" + spes + "index.py"

            elif os.path.isfile(str(path) + spes + "public" + spes + "home.py") == True:
                vpath = "public" + spes + "home.py"

            else:
                vpath = "public" + spes + "default.py"

            App = im.load_source('App.App', path + spes + vpath)
            mimetype = 'text/html'
            if "." not in path_info :
                
                
                App.App.put(method="POST", accept_lang=self.headers["Accept-Language"],
                            http_connect=self.headers["Connection"], http_user_agt=self.headers["User-Agent"],
                            http_encode=self.headers["Accept-Encoding"], path=path, host=host, port=port, para=path_info,
                            remoter_addr=self.client_address[0], remoter_port=self.client_address[1], script_file=str(
                    path) + str(spes) + (vpath), server_proto=server_pro, server_ver=self.server_version,
                    protocol_ver=self.protocol_version)

                self.rendering(mimetype=mimetype, code=200,
                            content=App.App.runs(formData=form))

        def do_HEAD(self):
            self.do_GET()

        def do_PUT(self):
            self.do_POST()

        def rendering(self, path="", mimetype="", mode='r', encoding="utf-8", content="", code=200):

            self.send_response(int(code))
            self.send_header('Content-type', mimetype)
            self.end_headers()
            if path != "":

                f = open(path + self.path, mode)
                readv = ""
                if mode == "rb":
                    readv = f.read()
                else:
                    readv = bytes(str(f.read()).encode('utf-8'))

                self.wfile.write(readv)

                f.close()

            elif content != "":
                self.wfile.write(bytes(str(content).encode()))

        def error(self, code, e_url, code_re=307):
            self.send_response(int(code_re))
            self.send_header('Location', "{e_url}".format(e_url=e_url))
            self.send_error(
                code=int(code), message=Version.HTTP_CODE.get(code, ""))
            self.end_headers()

        def redirect(self, code, re_url, code_re=307):
            self.send_response(int(code_re))
            self.send_header('Location', "{re_url}".format(re_url=re_url))
            self.send_error(
                code=int(code), message=Version.HTTP_CODE.get(code, ""))
            self.end_headers()

    class ThreadedHTTPServer(ThreadingMixIn, server):
        """Moomins live here"""

    hostname = ssl_ip if ssl_ip != "" else host
    portnumber = int(ssl_port) if ssl_port != "" else int(port)
    vars_http = ""
    try:
        context = ssl.create_default_context()

        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                # print(ssock.version())
                data = json.dumps(ssock.getpeercert())
        varb.put("HTTPS", "on")
        vars_http = "https://"
        # print(ssock.getpeercert())
    except Exception as err:
        try:
            cert = ssl.get_server_certificate((hostname, int(portnumber)))
            varb.put("HTTPS", "on")
            vars_http = "https://"
        except Exception as err:
            varb.put("HTTPS", "off")
            vars_http = "http://"

    try:
        l = host if str(port) == "8080" or str(port) == "80" else "{}:{}".format(
            host, port)
        if pr == True:

            print(
                bold(green("Pytonik development server running on " + str(vars_http) + str(l))))
        else:
            print(bold(green("Pytonik server running on " + str(vars_http) + str(l))))

        server = ThreadedHTTPServer((host, port), httpv)
        server.serve_forever()
        server.server_close()
    except Exception as err:
        print(bold(red("Something went wrong: Default port already in use")))
