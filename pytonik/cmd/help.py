# Author : BetaCodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by BetaCodings on 1/19/20.



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
from pytonik.cmd import start
from pytonik.cmd import server
from pytonik.cmd import install
from pytonik.cmd import doc
from pytonik import Version
from pytonik import serv 
from pytonik.Functions.url import url
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
        and bundles of component to reuse while deploying the framework.
        
        
        """))

    parser.add_argument('-q', '--quit', action='store_true', dest='quit',
                        default=None,
                        help=__('quit mode'))

    parser.add_argument('--version', '-v', action='version', dest='show_version',
                        version='Pytonik %s' % Version.VERSION_TEXT)

    parser.add_argument('start', metavar='PROJECT_DIR', default='all', nargs='?',
                        help=__('Terminal Command'))
    
    return parser


def ask(d: Dict) -> None:
    
    if len(d) > 0:
        if d.get('start', '') == 'start':
            return start.main(sys.argv[1:])

        if d.get('start', '') == 'server':
            return server.main(sys.argv[1:])

        if d.get('start', '') == 'install' :
            return install.main(sys.argv[1:])
        
        if d.get('start', '') == 'version' :
            print('Pytonik %s' % Version.VERSION_TEXT)
        
        if d.get('start', '') == 'doc' or d.get('start', '') =="docs":
            return doc.main(sys.argv[1:])
        
        if d.get('start', '') == 'quit':
            return sys.exit(-1)
        

        if d.get('start', '') == 'all':
            return help_notes()

        if d.get('quit', '') is True:
            return sys.exit(-1)
            
    else:
        return help_notes()
    

def help_notes():
    cnt_text = """
    Pytonik is a python framework built to enhance web development
    fast and easy, also help web developers to build more apps with less codes.
    it uses expressive architectural pattern, structured on model view controller MVC
    and bundles of component to reuse while deploying the framework.

    usage: 
    Options and arguments (and corresponding environment variables):

    pytonik [option]
    ================
    start     			: Create new pytonik project to an assign directory
    server     			: Run pytonik Server from an assign project directory
    install 			: Install pytonik requirement from an assign directory
    doc     			: Read Pytonik Documentation (doc) or (docs)
    version     		: Pytonik Version (-v) or (--version)

    direct command [pytonik-option]
    ===============================
    pytonik-start     	: Create a new pytonik project to an assign directory
    pytonik-server     	: Run pytonik Server from an assign project directory
    pytonik-install     : Install pytonik requirement from an assign directory
    pytonik-docs     	: Read Pytonik Documentation
    """

    print(cnt_text)

def main(argv: List[str] = sys.argv[1:]) -> int:
    # parse options
    parser = get_parser()
    try:
        args = parser.parse_args(argv)

    except SystemExit as err:
        return err.code
    d = vars(args)
    ask(d)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
