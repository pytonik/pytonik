# Author : BetaCodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by BetaCodings on 1/19/20.


import argparse
import locale
import os
import re
import sys
import time
import warnings
from pytonik import Version
from typing import Any, Callable, Dict, List, Pattern, Union

import webbrowser

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

def __(string):
    return string


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        usage='%(prog)s [OPTIONS] <PROJECT_DIR>',
        epilog=__("For more information, visit < https://pytonik.readthedocs.io >."),
        description=__("""Pytonik is a python framework built to enhance web development
        fast and easy, also help web developers to build more apps with less codes.
        it uses expressive architectural pattern, structured on model view controller MVC
        and bundles of component to reuse while deploying the framework."""))

    parser.add_argument('-q', '--quit', action='store_true', dest='quit',
                        default=None,
                        help=__('quit mode'))
    parser.add_argument('--version', action='version', dest='show_version',
                        version='%%(prog)s %s' % Version.VERSION_TEXT)

    parser.add_argument('path', metavar='PROJECT_DIR', default='.', nargs='?',
                        help=__('project root'))

    return parser


def main(argv: List[str] = sys.argv[1:]) -> int:
    # parse options
    parser = get_parser()
    try:
        args = parser.parse_args(argv)

    except SystemExit as err:
        return err.code
    d = vars(args)
    import http.server
    import socketserver

    class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            if self.path == '/':
                self.path = 'docs'
            if self.path.endswith('favicon.ico'):
                    return
            if self.path.endswith('robots.txt'):
                    return
            if self.path.endswith('favicon.ico'):
                    return
            return http.server.SimpleHTTPRequestHandler.do_GET(self)

    # Create an object of the above class
    handler_object = MyHttpRequestHandler

    PORT = 6061
    url = "localhost"
    #my_server = socketserver.TCPServer((url, PORT), handler_object)

    l = "https://pytonik.readthedocs.io/en/latest/" #"http://{}:{}".format(url, PORT)
    print("Documentation Link {}".format(l))
    try:
        webbrowser.open_new(l)
    except Exception as err:
        print(err)
    # Star the server
    #my_server.serve_forever()



if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))