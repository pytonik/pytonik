# Author : BetaCodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by BetaCodings on 1/19/20.


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
from typing import Any, Callable, Dict, List, Pattern, Union
from pytonik.cmd.console import (  # type: ignore
    colorize, bold, red, green, turquoise, nocolor, color_terminal
)

import webbrowser

cgitb.enable()

from random import randint

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


def do_prompt(text: str, default: str = None, validator: Callable[[str], Any]=nonempty) -> Union[str, bool]:  # NOQA

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
            d['quite'] = do_prompt(__('Do you want exite (y/n)'), 'n', boolean)
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


def serv(path="", port=6060):
    ##randint(1000, 9999)

    try:
        portno = int(port)
    except Exception as err:
        print(bold(red(__("Accept only int, not String !!"))))
        return False
    server = HTTPServer

    handler = CGIHTTPRequestHandler
    server_address = ("", portno)

    path = str(path) if path != "" else str(os.getcwd())

    handler.cgi_directories = [path]
    handler.cgi_info = {}

    url = "localhost"

    # randint(1000, 9999)
    l = "{}:{}".format(url, portno)

    class pysteveHTTPHandler(BaseHTTPRequestHandler):

        def do_GET(self):
            try:
                import imp as im
            except Exception as err:
                import importlib as im

            mimetype = ""
            sys.path.insert(0, os.path.dirname(__file__))

            path_info = self.path

            os.chdir(path)

            if self.path == "/":
                if os.path.isfile(str(path) + "/public/index.py") == True:
                    vpath = "public/index.py"
                    env_set(path, url, portno, self.path)

                elif os.path.isfile(str(path) + "/public/home.py") == True:
                    vpath = "public/home.py"
                    env_set(path, url, portno, self.path)
                App = im.load_source('App.App', path + "/" + vpath)
                mimetype = 'text/html'
                self.send_response(200)
                self.send_header('Content-type', mimetype)
                self.end_headers()
                self.wfile.write(bytes(str(App.App.runs()).encode()))
            elif self.path != "/":

                if "." not in str(self.path):
                    if str(self.path) != "":
                        if os.path.isfile(str(path) + "/public/index.py") == True:
                            lpath = "public/index.py"
                            env_set(path, url, portno, self.path)

                        elif os.path.isfile(str(path) + "/public/home.py") == True:
                            lpath = "public/home.py"
                            env_set(path, url, portno, self.path)

                        App = im.load_source('App.App', path + "/" + lpath)
                        mimetype = 'text/html'
                        self.send_response(200)
                        self.send_header('Content-type', mimetype)
                        self.end_headers()
                        self.wfile.write(bytes(str(App.App.runs()).encode()))

            try:
                from pytonik import Version
                for mime in Version.MIME_TYPES:
                    if self.path.endswith(mime['ext']):
                        self.render(path=path, mimetype=mime[
                                    'type'], mode=mime['mode'])

            except Exception as err:
                self.send_response(404)
                self.send_error(404, 'File Not Found: %s' % self.path)
                doTraceBack()

        def do_POST(self):
            self.do_GET()

        def do_HEAD(self):
            self.do_GET()

        def render(self, path, mimetype, mode='r', encoding="utf-8"):
            f = open(path + '/' + self.path, mode)
            self.send_response(200)
            self.send_header('Content-type', mimetype)
            self.end_headers()
            if mode == "rb":
                readv = f.read()
            else:
                readv = bytes(str(f.read()).encode('utf-8'))
            self.wfile.write(readv)
            f.close()
            return readv

    class ThreadedHTTPServer(ThreadingMixIn, server):
        """Moomins live here"""

    try:

        server = ThreadedHTTPServer((url, portno), pysteveHTTPHandler)
        print(green("Pytonik development server running on " + str(l)))
        webbrowser.open_new(l)
        server.serve_forever()

    except Exception as err:
        try:
            server = ThreadedHTTPServer((url, portno), pysteveHTTPHandler)
            print(green("Pytonik development server running on " + str(l)))
            server.serve_forever()
        except Exception as err:
            print(red("Something went wrong: Default port already in use"))


def env_set(path, host, port, para="", status=200, accept=""):
    uri = path.split('/')[-1]
    env = {
        "PATH_INFO": str(path),
        "HTTP_HOST": str(host),
        "SERVER_PORT": str(port),
        "REDIRECT_STATUS": str(status),
        'HTTP_ACCEPT': accept,
        'DOCUMENT_ROOT': os.path.basename(path),
        'SERVER_SOFTWARE': "Pytonik",
        'PATH_TRANSLATED': path + "/public",
        "REQUEST_URI": str(host) + ":" + str(port) + "/" + str(uri) + str(para),

    }

    if Version.PYVERSION_MA <= 2:
        lt = env.iteritems()
    else:
        lt = env.items()
    if os.environ.get("REQUEST_URI", "") != "" or os.environ.get("REQUEST_URI", "") != None:
        try:
            del os.environ["REQUEST_URI"]
        except Exception as err:
            os.environ.clear()
            os.environ.update(dict(env))

    i = 0
    for c, (k, v) in enumerate(lt):
        i += 1
        os.environ.setdefault(k, str(v).encode())
        ++i
    os.environ.update(dict(REQUEST_URI=os.environ.get("REQUEST_URI")))


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
