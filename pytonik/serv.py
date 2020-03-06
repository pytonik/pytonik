import cgitb
import base64
import traceback

import ssl
import argparse
import locale
import os
import re
import sys
import time
import warnings
from pytonik.cmd import lang
from pytonik import Version
from pytonik.util.Variable import Variable 
from typing import Any, Callable, Dict, List, Pattern, Union
from pytonik.cmd.console import (  # type: ignore
    colorize, bold, red, green, turquoise, nocolor, color_terminal
)
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

    class httpv(BaseHTTPRequestHandler):

        def do_GET(self):
            spes = "/"
            try:
                import imp as im
            except Exception as err:
                import importlib as im

            mimetype = ""
            sys.path.insert(0, os.path.dirname(__file__))

            path_info = self.path

            os.chdir(path)
            vpath = ""

            if self.path == spes:
                if os.path.isfile(str(path) + spes+"public"+spes+"index.py") == True:
                    vpath = "public"+spes+"index.py"

                elif os.path.isfile(str(path) + spes+"public"+spes+"home.py") == True:
                    vpath == "public"+spes+"home.py"

                App = im.load_source('App.App', path + spes + vpath)
                mimetype = 'text/html'
                App.App.put(path=path, host=host, port=port, para=self.path, remoter_addr=self.client_address[0], remoter_port=self.client_address[1], script_file=str(
                    path)+str(spes)+(vpath), server_proto=server_pro, server_ver=self.server_version, protocol_ver=self.protocol_version)

                self.rendering(mimetype=mimetype,
                               content=App.App.runs(), code=200)

            elif self.path != spes:

                if "." not in str(self.path):

                    if str(self.path) != "":
                        if os.path.isfile(str(path) + spes+"public"+spes+"index.py") == True:
                            vpath = "public"+spes+"index.py"

                        elif os.path.isfile(str(path) + spes+"public"+spes+"home.py") == True:
                            vpath = "public"+spes+"home.py"

                        App = im.load_source('App.App', path + spes + vpath)
                        mimetype = 'text/html'

                        App.App.put(path=path, host=host, port=port, para=self.path, remoter_addr=self.client_address[0], remoter_port=self.client_address[1], script_file=str(
                            path)+str(spes)+(vpath), server_proto=server_pro, server_ver=self.server_version, protocol_ver=self.protocol_version)

                        if isinstance(App.App.runs(), tuple):
                            if App.App.runs()[0] == "404" or App.App.runs()[0] == "405" or App.App.runs()[0] == "400":
                                self.error(App.App.runs()[
                                           0], App.App.runs()[1])
                            elif App.App.runs()[0] == "307":
                                self.redirect(
                                    App.App.runs()[0], App.App.runs()[1])
                        else:
                            self.rendering(mimetype=mimetype,
                                           content=App.App.runs())

            if self.path.endswith('favicon.ico'):
                return
            try:
                for mime in Version.MIME_TYPES:
                    if self.path.endswith(mime['ext']):
                        self.rendering(path=path, mimetype=mime[
                            'type'], mode=mime['mode'], code=200)

            except Exception as err:
                doTraceBack()

        def do_POST(self):
            self.do_GET()

        def do_HEAD(self):
            self.do_GET()

        def rendering(self, path="", mimetype="", mode='r', encoding="utf-8", content="", code=200):

            self.send_response(code)
            self.send_header('Content-type', mimetype)
            self.end_headers()
            if path != "":

                f = open(path+self.path, mode)
                readv = ""
                if mode == "rb":
                    readv = f.read()
                else:
                    readv = bytes(str(f.read()).encode('utf-8'))

                self.wfile.write(readv)

                f.close()

            elif content != "":
                self.wfile.write(bytes(str(content).encode()))
            else:
                return False

        def error(self, code, e_url, code_re=301):

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
        cert = ssl.get_server_certificate((hostname, portnumber))
        varb.put("HTTPS", "on")
        vars_http = "https://"
    except Exception as err:
        varb.put("HTTPS", "off")
        vars_http = "http://"
        
    
    try:
        l = host if port == "8080" or port == "80" else "{}:{}".format(host, port)
        if pr == True:
            
            print(bold(green("Pytonik development server running on " + str(vars_http)+str(l))))
        else:
            print(bold(green("Pytonik server running on " +str(vars_http)+ str(l))))
            
        server = ThreadedHTTPServer((host, port), httpv)
        server.serve_forever()
        server.server_close()
    except Exception as err:
        print(bold(red("Something went wrong: Default port already in use")))

    
