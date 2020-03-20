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
import json

log_msg = Log()

try:
    import http.client as htp
    from  http import client
    import urllib as urllib
except Exception as err:
    import httplib as htp
    import urllib2 as urllib


class curl:
    def __getattr__(self, item):

        return item

    def __init__(self):

        self.__var()
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
        self.PORT = "PORT"

        return

    def __var(self):
        self.h = dict()
        self.res = ""
        self.method = ""
        self.params = ""
        self.link = ""
        self.status = ""
        self.reason = ""
        self.path = ""
        self.source_address = None
        self.blocksize = 8192
        self.body = None
        self.conn = ""
        self.http = ""
        self.output = ""
        self.pt = None
        self.tout = socket._GLOBAL_DEFAULT_TIMEOUT


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
            if options != "":
                self.__path(actions)

        if options == self.HEAD:
            self.__method(self.HEAD)
            if actions != "":
                self.__path(actions)

        if options == self.PUT:
            self.__method(self.PUT)
            if actions != "":
                self.__path(actions)

        if options == self.URL:
            self.__url(actions)

        if options == self.PORT:
            self.__port(actions)

        if options == self.CONTENTHEADER:
            self.__contentType(actions)

        if options == self.ACCEPTHEADER:
            self.__accept(actions)

        if options == self.HEADER:
            self.__header(actions)

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

            self.conn.request(self.method, self.path, self.body, self.h)
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
        header = {'Accept': accept}
        return self.array_dict(header)


    def __contentType(self, contT):

        header = {'Content-type': contT}
        return self.array_dict(header)


    def __header(self, header):
        return self.array_dict(header)


    def array_dict(self, ldict):
        ldict = ldict
        return self.h.update(ldict)

    def __port(self, pt):
        self.pt = pt
        return self

    def __path(self, path=""):
        self.path = "/" if path  == "" else path
        return self

    def __timeout(self, tout):
        self.tout = tout
        return self

    def response(self):
        self.status = self.res.status
        self.reason = self.res.reason
        self.output = self.res.read()
        return self

    def result(self, decode=""):
        if decode != "":
            reSlt = self.output.decode(decode)
        else:
            reSlt = self.output

        return reSlt

