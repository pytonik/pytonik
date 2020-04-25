#!/usr/bin/python

import argparse
import locale
import os
import re
import sys
import time
import warnings
from pytonik.cmd import lang
from pytonik import Version
from pytonik.cmd import server
from typing import Any, Callable, Dict, List, Pattern, Union
from pytonik.cmd.console import (  # type: ignore
    colorize, bold, green, red, turquoise, nocolor, color_terminal
)
import shutil
import zipfile

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

PROMPT_PREFIX = '> '

if sys.platform == 'win32':
    # On Windows, show questions as bold because of color scheme of PowerShell
    # (refs: #5294).
    COLOR_QUESTION = 'bold'
else:
    COLOR_QUESTION = 'purple'


def pathwhich():
    pat = ""
    if sys.platform == 'win32':
        path = os.environ['PATH'].split(';')

        for p in path:
            if "Python" in p:
                # python.exe
                if 'python.exe' in p:
                    pat = p
                else:

                    if p[-1] == '\"' or p[-1] == '/':
                        pat = p[:-1] + '\"' + str("python.exe")
                        break
                    else:
                        pat = str(p) + "\'" + str("python.exe")
                        break

    else:
        try:
            pat = os.popen('which python').read()
        except Exception as arr:
            try:
                pat = os.environ['__PYVENV_LAUNCHER__']
            except Exception as arr:
                print(arr)
    return pat.replace("'", '')


# function to get input from terminal -- overridden by the test suite
def term_input(prompt: str) -> str:
    if sys.platform == 'win32':

        print(prompt, end='')
        return input('')
    else:
        return input(prompt)


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
    return str(l_)


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

    parser.add_argument('path', metavar='PROJECT_DIR', default='.', nargs='?',
                        help=__('project root'))

    return parser


def ask(d: Dict) -> None:
    print(bold(__('Welcome to the Pytonik MVC Framework %s Start File Structure.' %
                  Version.VERSION_TEXT)))

    print(__('Please enter values for the following settings.'))

    if 'path' in d:
        print(bold(__('''Selected root path: %s''' % os.getcwd())))
        d['path'] = os.getcwd()

        d['step'] = do_prompt(__('Do you want to create file pytonik in this directory  (y/n)'),
                              'n', boolean)

    if d.get('step', '') is True:

        if 'project' not in d:

            print(__('''Provide project name, it will be use in project folder creation, avoid space while typing'''))

            d['project'] = do_prompt(bold('Project name'))
            if d.get('project', '') != "":

                if os.path.isdir(os.getcwd() + '/' + d.get('project', '')) is False:

                    print(bold(__('Project In-progress, please wait..')))

                    try:

                        os.mkdir(os.getcwd() + '/' +
                                 d.get('project', ''), mode=0o755)

                        print(
                            bold(__('Project {} Created Successfully'.format(d.get('project', '')))))

                    except Exception as err:
                        print(red('Unable to create project {} directory'.format(
                            os.getcwd() + '/' + d.get('project', ''))))

                    make_file(d)

                else:
                    msg = red(
                        __('Directory Already exist, overwrite ? (y/n)'.format(projectname=d.get('project', ''))))
                    d['cont'] = do_prompt(msg, 'n', boolean)
                    if d.get('cont') is True:

                        make_file(d)

                    else:
                        sys.exit(-1)

            else:
                d['quit'] = do_prompt(
                    __('Do you want to quit (y/n)'), 'n', boolean)

    else:
        d['quit'] = do_prompt(__('Do you want to quit (y/n)'), 'n', boolean)

    if d.get('quit', '') is True:
        sys.exit(-1)

    print()


def make_file(d):
    dst = os.getcwd() + '/' + d.get('project', '')
    try:

        src = os.path.dirname(os.path.abspath(__file__))

        zip_folder = src + '/land.zip'

        zip_folder = zip_folder.replace('\\', '/')

        with zipfile.ZipFile(zip_folder) as zf:
            zf.extractall(dst)

        print(bold(green(__('Project {} Is ready...'.format(d.get('project', ''))))))
    except Exception as err:
        try:

            src = os.path.dirname(os.path.abspath(__file__)) + "/land"

            for f in os.listdir(src):
                s = os.path.join(src, f)
                dt = os.path.join(dst, f)
                if os.path.isdir(s):
                    shutil.copytree(s, dt)
                else:
                    shutil.copy2(s, dt)

            print(bold(green(__('Project {} Is ready...'.format(d.get('project', ''))))))
        except Exception as err:
            print(err)

    # write / update python path
    dst_path = dst+"/public/index.py"
    dst_path_log = dst+"/app.log"
    if os.path.isfile(dst_path) == True:
        index_file = """{}
try:
\n  from pytonik import Web
\nexcept Exception as err:
\n  exit(err)
\nApp = Web.App()
\nApp.runs()
""".format("#!" + str(pathwhich()))
        file_open = open(dst_path, 'w+')
        file_open.write(index_file)
        try:
            os.chmod(dst_path, mode=0o755)
            os.chmod(dst_path_log, mode=0o777)
            print(bold(green(__('Permission Done...'))))

        except Exception as err:

            print(bold(red(__('Unable to Set permission '))))


def main(argv: List[str] = sys.argv[1:]) -> int:
    # parse options
    parser = get_parser()
    try:
        args = parser.parse_args(argv)

    except SystemExit as err:
        return err.code

    d = vars(args)
    ask(d)

    return ""


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
