# Author : BetaCodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by BetaCodings on 1/19/20.


from random import randint
from socketserver import ThreadingMixIn
import cgitb
import base64
import traceback
from http.server import BaseHTTPRequestHandler, CGIHTTPRequestHandler, HTTPServer
from http import HTTPStatus
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
from pytonik.Functions.url import url
from pytonik.App import App as Pytonik
from typing import Any, Callable, Dict, List, Pattern, Union
from pytonik.cmd.console import (  # type: ignore
    colorize, bold, red, green, turquoise, nocolor, color_terminal
)


import webbrowser

cgitb.enable()


try:
    import readline

    if readline.__doc__ and 'libedit' in readline.__doc__:
        readline.parse_and_bind("bind ^I rl_complete")
        USE_LIBEDIT = True
    else:
        readline.parse_and_bind("tab: complete")
        USE_LIBEDIT = False
except ImportError:
    USE_LIBEDIT = False


class ValidationError(Exception):
    """Raised for validation errors."""


def is_path(x: str) -> str:
    x = os.path.expanduser(x)
    if not os.path.isdir(x):
        raise ValidationError(__("Please enter a valid path name."))
    return x


def boolean(x: str) -> bool:
    if x.upper() not in ('Y', 'YES', 'N', 'NO'):
        raise ValidationError(__("Please enter either 'y' or 'n'."))
    return x.upper() in ('Y', 'YES')


def allow_empty(x: str) -> str:
    return x


def nonempty(x: str) -> str:
    if not x:
        raise ValidationError(__("Please enter some text."))
    return x


def __(mes_id):
    try:
        userlang = locale.getlocale()[0]

        l_ = mes_id
        for l in lang.lang:
            if l == str(userlang):
                getla = lang.lang.get(l, '')

                if getla != "":
                    l_ = getla.get(mes_id, '')
                    if l_ != "":
                        l_ = getla.get(mes_id, '')
                    else:
                        l_ = mes_id
                else:
                    l_ = mes_id
    except Exception as arr:
        l_ = mes_id
    return l_


def doTraceBack():
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)
    traceback.print_exception(exc_type, exc_value, exc_traceback,
                              limit=2, file=sys.stdout)
    traceback.print_exc()


if sys.platform == 'win32':
    # On Windows, show questions as bold because of color scheme of PowerShell
    # (refs: #5294).
    COLOR_QUESTION = 'bold'
else:
    COLOR_QUESTION = 'purple'

PROMPT_PREFIX = '> '


def do_prompt(text: str, default: str = None, validator: Callable[[str], Any] = nonempty) -> Union[str, bool]:  # NOQA

    while True:

        if default is not None:
            prompt = PROMPT_PREFIX + '%s [%s]: ' % (text, default)
        else:
            prompt = PROMPT_PREFIX + text + ': '
        if USE_LIBEDIT:
            # Note: libedit has a problem for combination of ``input()`` and escape
            # sequence (see #5335).  To avoid the problem, all prompts are not colored
            # on libedit.
            pass
        else:
            prompt = colorize(COLOR_QUESTION, prompt, input_mode=True)
        x = term_input(prompt).strip()
        if default and not x:
            x = default
        try:
            x = validator(x)
        except ValidationError as err:
            print(red('* ' + str(err)))
            continue
        break
    return x


def term_input(prompt: str) -> str:
    if sys.platform == 'win32':

        print(prompt, end='')
        return input('')
    else:
        return input(prompt)


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        usage='%(prog)s [OPTIONS] <PROJECT_DIR>',
        epilog=__(
            "For more information, visit < https://pytonik.readthedocs.io >."),
        description=__("""Pytonik is a python framework built to enhance web development
        fast and easy, also help web developers to build more apps with less codes.
        it uses expressive architectural pattern, structured on model view controller MVC
        and bundles of component to reuse while deploying the framework."""))

    parser.add_argument('-q', '--quit', action='store_true', dest='quit',
                        default=None,
                        help=__('quit mode'))
    parser.add_argument('--version', action='version', dest='show_version',
                        version='%%(prog)s %s' % Version.VERSION_TEXT)

    parser.add_argument('port', default='6060', nargs='?', )

    return parser


def ask(d: Dict) -> None:
    print(bold(__('Run Pytonik Server.')))

    d['run'] = do_prompt(
        __('Do you want to run this project using default port (y/n)'), 'n', boolean)

    if d.get('run', '') is True:
        serv()

    else:
        d['port'] = do_prompt(__('Enter Custom Port'))
        if d.get('port', '') != "":
            if type(d.get('port', '')):

                askg(d)

            else:
                print(bold(red(__('Enter Only Number'))))
                askg(d)

        else:
            d['quite'] = do_prompt(__('Do you want exit (y/n)'), 'n', boolean)
            if d.get('quite', '') is True:
                sys.exit(-1)
            else:
                askg(d)

        print()


def askg(d):
    serv(port=d.get('port', ''))


def main(argv: List[str] = sys.argv[1:]) -> int:
    # parse options
    parser = get_parser()
    try:
        args = parser.parse_args(argv)

    except SystemExit as err:
        return err.code
    d = vars(args)
    ask(d)


def serv(host="localhost", path="", port=6060, server_pro="HTTP/1.1"):
    # randint(1000, 9999)
    try:
        portno = int(port)
    except Exception as err:
        print(bold(red(__("Accept only int, not String !!"))))
        return False
    server = HTTPServer

    handler = CGIHTTPRequestHandler
    server_address = ("", portno)

    path = str(path).replace("\\", "/") if path != "" else str(os.getcwd()).replace("\\", "/")

    # randint(1000, 9999)
    l = "{}:{}".format(host, portno)

    class pysteveHTTPHandler(BaseHTTPRequestHandler):

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
                App.App.put(path=path, host=host, port=portno, para=self.path, remoter_addr = self.client_address[0], remoter_port=self.client_address[1], script_file=str(path)+str(spes)+(vpath), server_proto=server_pro, server_ver=self.server_version, protocol_ver=self.protocol_version)
                        
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
                        
                        App.App.put(path=path, host=host, port=portno, para=self.path, remoter_addr = self.client_address[0], remoter_port=self.client_address[1], script_file=str(path)+str(spes)+(vpath), server_proto=server_pro, server_ver=self.server_version, protocol_ver=self.protocol_version)
                        
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
                self.errro("404")
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

    try:

        server = ThreadedHTTPServer((host, portno), pysteveHTTPHandler)
        print(bold(green("Pytonik development server running on " + str(l))))
        server.serve_forever()

    except Exception as err:
        try:
            server = ThreadedHTTPServer((host, portno), pysteveHTTPHandler)
            print(bold(green("Pytonik development server running on " + str(l))))
            server.serve_forever()
        except Exception as err:
            print(bold(red("Something went wrong: Default port already in use")))



if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
