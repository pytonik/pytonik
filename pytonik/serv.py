import cgitb
import base64
import traceback
import socket
import argparse
import locale
import os
import re
import sys
import time
import warnings
from pytonik.cmd import lang
from pytonik import Version
from pytonik import serv 
import traceback
from socketserver import ThreadingMixIn
try:
    from BaseHTTPServer import BaseHTTPRequestHandler
except Exception as e:
    from http.server import BaseHTTPRequestHandler, HTTPServer


def run(host="", path="", port=6060, server_pro="HTTP/1.1"):
    
    server = HTTPServer

    path = str(path).replace("\\", "/") if path != "" else str(os.getcwd()).replace("\\", "/")
    
    
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
                if os.path.isfile(str(path) +spes+"public"+spes+"index.py") == True:
                    vpath = "public"+spes+"index.py"


                elif os.path.isfile(str(path) +spes+"public"+spes+"home.py") == True:
                    vpath == "public"+spes+"home.py"

                App = im.load_source('App.App', path + spes + vpath)
                mimetype = 'text/html'
                App.App.put(path=path, host=host, port=port, para=self.path, remoter_addr = self.client_address[0], remoter_port=self.client_address[1], script_file=str(path)+str(spes)+(vpath), server_proto=server_pro, server_ver=self.server_version, protocol_ver=self.protocol_version)
                        
                self.rendering(mimetype=mimetype, content=App.App.runs(), code=200)

            elif self.path != spes:
                
                if "." not in str(self.path):

                    if str(self.path) != "":
                        if os.path.isfile(str(path) +spes+"public"+spes+"index.py") == True:
                            vpath = "public"+spes+"index.py"


                        elif os.path.isfile(str(path) +spes+"public"+spes+"home.py") == True:
                            vpath = "public"+spes+"home.py"


                        App = im.load_source('App.App', path +spes+ vpath)
                        mimetype = 'text/html'
                        
                        App.App.put(path=path, host=host, port=port, para=self.path, remoter_addr = self.client_address[0], remoter_port=self.client_address[1], script_file=str(path)+str(spes)+(vpath), server_proto=server_pro, server_ver=self.server_version, protocol_ver=self.protocol_version)
                        
                        if isinstance(App.App.runs(), tuple):
                            if App.App.runs()[0] == "404" or App.App.runs()[0] == "405" or App.App.runs()[0] == "400":
                                self.error(App.App.runs()[0], App.App.runs()[1])
                            elif App.App.runs()[0] == "307":
                                self.redirect(App.App.runs()[0], App.App.runs()[1])
                        else:
                            self.rendering(mimetype=mimetype, content=App.App.runs())
                            
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

            elif content !="":
                self.wfile.write(bytes(str(content).encode()))
            else:
                return False

        def error(self, code, e_url, code_re = 301):
            
            self.send_response(int(code_re))
            self.send_header('Location', "{e_url}".format(e_url=e_url))
            self.send_error(code=int(code), message=Version.HTTP_CODE.get(code, ""))
            self.end_headers()
            
        def redirect(self, code, re_url, code_re = 307):
                self.send_response(int(code_re))
                self.send_header('Location', "{re_url}".format(re_url=re_url))
                self.send_error(code=int(code), message=Version.HTTP_CODE.get(code, ""))
                self.end_headers()
                
         
    class ThreadedHTTPServer(ThreadingMixIn, server):
        """Moomins live here"""
        
    server = ThreadedHTTPServer((host, port), httpv)
    server.serve_forever()

        