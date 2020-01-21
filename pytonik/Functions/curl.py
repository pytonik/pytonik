###
# Author : Betacodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by Betacodings on 2019.
###
from pytonik import Version
from pytonik.Log import Log
import socket
log_msg = Log()

if Version.PYVERSION_MA > 2:
    import http.client as htp
    import  urllib as urllib
else:
    import httplib as htp
    import urllib2 as urllib

class curl:
    
    def __getattr__(self, item):
        return item

    def __init__(self):
        self.URL = "URL"
        self.HTTPHEADER = "HTTPHEADER"
        self.TIMEOUT = "TIMEOUT"
        self.FOLLOWLOCATION = "FOLLOWLOCATION"
        self.CONTENTHEADER = "CONTENTHEADER"
        self.POSTFIELDS = "POSTFIELDS"
        self.ACCEPTHEADER = "ACCEPTHEADER"
        self.POST = 'POST'
        self.GET = 'GET'
        self.HEAD = 'HEAD'
        self.PUT = 'PUT'
        self.PORT  = "PORT"

        self.__var()


        return None

    def __var(self):
        self.res = ""
        self.method = ""
        self.params = ""
        self.headers = {}
        self.link = ""
        self.status = ""
        self.reason = ""
        self.path = ""
        self.pt = None
        self.tout = socket._GLOBAL_DEFAULT_TIMEOUT
        self.source_address = None
        self.blocksize = 8192
        self.body = None
        self.conn = ""
        self.http = ""
        self.output = ""
    
    def set(self, options, actions=""):

        if options == self.POST:
            self.__method(self.POST)
            if actions == 1:
                self.path = ""
            else:
                self.__path(actions)
        if options == self.POSTFIELDS:
            self.__body(actions)

        if options == self.GET:
            self.__method(self.GET)
            if options is not "":
                self.__path(actions)

        if options == self.HEAD:
            self.__method(self.HEAD)
            if actions is not "":
                self.__path(actions)


        if options == self.PUT:
            self.__method(self.PUT)
            if actions is not "":
                self.__path(actions)

        if options == self.URL:
            self.__url(actions)


        if options == self.PORT:
            self.__port(actions)

        if options == self.CONTENTHEADER:
            self.__contentType(actions)

        if options == self.ACCEPTHEADER:
            self.__accept(actions)


        if options == self.TIMEOUT:
            self.__timeout(actions)

        return self
        
    def finish(self):

        try:

            if self.method == self.GET or self.method == self.HEAD:
                if 's' in self.http:
                    self.conn = htp.HTTPSConnection(host=self.link, port=self.pt, timeout=self.tout,
                                                   source_address=self.source_address, blocksize=self.blocksize)
                else:
                    self.conn = htp.HTTPConnection(host=self.link, port=self.pt, timeout=self.tout,
                                                   source_address=self.source_address, blocksize=self.blocksize)
            else:
                if 's' in self.http:
                    self.conn = htp.HTTPSConnection(host=self.link, port=self.pt, timeout=self.tout,
                                                   source_address=self.source_address, blocksize=self.blocksize)
                else:
                    self.conn = htp.HTTPConnection(host=self.link, port=self.pt, timeout=self.tout,
                                                   source_address=self.source_address, blocksize=self.blocksize)

            self.conn.request(self.method, self.path, self.body, self.headers)
            self.res = self.conn.getresponse()
            self.response()
            self.conn.close()
        except Exception as err:
            log_msg.error(err)


        return self


    def __url(self, url=""):
        lh = ['ftps://', 'ftp://', "https://", "http://"]
        for ht in lh:
            if ht in url:
                self.http = ht
                self.link = url.replace(ht, "")
        return self

    def __body(self, body=""):
        self.body = urllib.parse.urlencode(body)
        return self

    def __method(self, method):
        self.method = method
        return self

    def __accept(self, accept):
        headers = {'Accept' : accept}
        self.headers.update(headers)
        return self.headers

    def __contentType(self, contT):
        headers = {'Content-type': contT}
        self.headers.update(headers)
        return self.headers

    def __port(self, pt):
        self.pt = pt
        return self


    def __path(self, path=""):
        self.path = "/" if path is "" else path
        return self


    def __timeout(self, tout):
        self.tout = tout
        return self


    def response(self):
        self.status = self.res.status
        self.reason = self.res.reason
        self.output = self.res.read()
        return self

    def result(self, decode = ""):
        if decode is not "":
            reSlt = self.output.decode(decode)
        else:
            reSlt =  self.output

        return reSlt

