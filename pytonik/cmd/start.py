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
    colorize, bold, red, turquoise, nocolor, color_terminal
)

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
    # On Windows, show questions as bold because of color scheme of PowerShell (refs: #5294).
    COLOR_QUESTION = 'bold'
else:
    COLOR_QUESTION = 'purple'

direct = {'controller': 'IndexController.py', 'lang': ['en.py', 'fr.py'], 'model': 'Index.py',
          'public': ['.htaccess', 'index.py'], 'views': 'index.html', '.env': '', '.htaccess': ''}


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


def context(lg):
    lc = ""
    if lg == 'htaccess1':
        lc = """<IfModule mod_rewrite.c>
RewriteEngine on
RewriteRule ^$ public/
RewriteRule (.*) public/$1 [NC,L]
</IfModule> """

    if lg == '.htaccess':
        lc = """<IfModule mod_rewrite.c>
DirectoryIndex index.py
Options +ExecCGI
AddHandler cgi-script .py
RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^(.*)$ index.py/$1 [L]
</IfModule>
                """
    if lg == 'index.py':
        lc = """{}
try:
\n  from pytonik import Web
\nexcept Exception as err:
\n  exit(err)

\nApp = Web.App()
\nApp.runs()
""".format("#!" + str(pathwhich()))

    if lg == 'en.py':
        lc = '{"lng.test":"sample text"}'

    if lg == 'fr.py':
        lc = '{"lng.test":"Exemple de texte"}'

    if lg == 'index.html':
        lc = """<!DOCTYPE html>
            \n<html lang="en">
    <head>
    <meta charset="UTF-8">
    <title> {{title}}</title>
            \n</head>
    <body>
    <h1> {{title}}</h1>
    \n</body>
    </html>"""

    if lg == 'IndexController.py':
        lc = """from pytonik.Web import App
\nm = App()
\ndef index():
\n  data = {'title': 'Pytonik MVC'}
\n  m.views('index', data)
            """
    if lg == '.env':
        lc = """{'route':

            {
                    'default': '',
            },
            \n'dbConnect':
                    {
                    'host': '',
                    'database': '',
                    'password': '',
                    'username': '',
                    'port': '',
                    'prefix': '',
                    'driver': ''
                            },
            \n'languages':
            {
            'en': 'en',
            'fr': 'fr',
            },
            \n'SMTP':
            {
                'server':   '',
                'port':     '',
                'username': '',
                'password': '',
            \n},
            'default_actions': 'index',
            'default_controllers' :'index',
            'default_routes' :'index',
            'default_languages':'en' }"""

    return lc


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
    return l_


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


def ask(d: Dict) -> None:
    print(bold(__('Welcome to the Pytonik MVC Framework %s Start File Structure.' % Version.VERSION_TEXT)))

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

                        os.mkdir(os.getcwd() + '/' + d.get('project', ''), mode=0o755)

                        print(bold(__('Project {} Created Successfully'.format(d.get('project', '')))))

                    except Exception as err:
                        print(red('Unable to create project {} directory'.format(
                            os.getcwd() + '/' + d.get('project', ''))))

                    make_file(direct, d)


                else:
                    d['cont'] = do_prompt(bold(__(
                        'Directory {} already exist, do you want to overwrite directory (y/n)'.format(
                            d.get('project', '')))),
                                          'n', boolean)
                    if d.get('cont') is True:

                        make_file(direct, d)

                    else:
                        sys.exit(-1)

            else:
                d['quit'] = do_prompt(__('Do you want to quit (y/n)'), 'n', boolean)

    else:
        d['quit'] = do_prompt(__('Do you want to quit (y/n)'), 'n', boolean)

    if d.get('quit', '') is True:
        sys.exit(-1)

    print()


def make_file(direct, d):
    itemsv = {}
    if Version.PYVERSION_MA == 3 and Version.PYVERSION_MI > 0:
        itemsv = direct.items()
    elif Version.PYVERSION_MA == 2 and Version.PYVERSION_MI <= 7:
        itemsv = direct.iteritems()

    for kdir, vdir in itemsv:

        if kdir.startswith('.'):
            print(bold(__('File {} Created Successfully').format(kdir)))

            if os.path.isfile(os.getcwd() + '/' + d.get('project', '') + '/' + str(
                    kdir)) is False:

                try:
                    f = open(os.getcwd() + '/' + d.get('project', '') + '/' + kdir, 'w')
                    f.close()
                except Exception as err:
                    print(bold(red(__(('Unable to create File  {}'.format(kdir))))))
                finally:
                    print(bold('File {} Created Successfully'.format(kdir)))

                try:
                    with open(os.getcwd() + '/' + d.get('project', '') + '/' + kdir, 'w+', encoding='utf-8') as f:

                        if kdir == ".htaccess":
                            f.write(context("htaccess1"))
                            f.close()
                        else:
                            f.write(context(kdir))
                            f.close()


                except Exception as err:

                    print(bold(red(__(('Unable to Write File  {}'.format(kdir))))))
                finally:
                    print(bold('File {} Rewrite Successfully'.format(ldir)))

                if os.path.isfile(os.getcwd() + '/' + d.get('project', '') + '/' + str(kdir)) is True:
                    try:
                        os.chmod(os.getcwd() + '/' + d.get('project', '') + '/' + str(kdir), mode=0o600)

                    except Exception as arr:
                        print(bold(red(__('Unable to Set file {} permission '.format(kdir)))))
                    finally:
                        print(bold(__('File {} Permission Set {}'.format(kdir, '0600'))))




        else:

            try:
                os.mkdir(os.getcwd() + '/' + str(d.get('project', '')) + '/' + str(kdir), mode=0o755)

                print(bold(__('''Folder {} Created Successfully'''.format(kdir))))
            except Exception as err:
                print(bold(red(__('''Folder  {}  already exist'''.format(kdir)))))

            if direct[kdir] != "":
                if type(direct[kdir]) == list:

                    for ldir in direct[kdir]:
                        if ldir != "":
                            if os.path.isfile(os.getcwd() + '/' + d.get('project',
                                                                        '') + '/' + str(
                                kdir) + '/' + ldir) is False:

                                try:
                                    f = open(os.getcwd() + '/' + d.get('project', '') + '/' + str(
                                        kdir) + '/' + ldir, 'w+')
                                    f.close()

                                except Exception as err:

                                    print(bold(red(__(('Unable to create File  {}'.format(ldir))))))
                                finally:
                                    print(bold('File {} Created Successfully'.format(ldir)))

                                try:
                                    with open(os.getcwd() + '/' + d.get('project', '') + '/' + str(
                                            kdir) + '/' + ldir, 'w+', encoding='utf-8') as f:
                                        f.write(context(ldir))
                                        f.close()


                                except Exception as err:

                                    print(bold(red('Unable to Write File  {}'.format(ldir))))

                                finally:
                                    print(bold('File {} Rewrite Successfully'.format(ldir)))

                            if os.path.isfile(os.getcwd() + '/' + d.get('project',
                                                                        '') + '/' + str(
                                kdir) + '/' + ldir) is True:

                                if ldir.startswith('.'):
                                    try:
                                        os.chmod(os.getcwd() + '/' + d.get('project', '') + '/' + str(kdir) + '/' + str(
                                            ldir), mode=0o600)
                                        print(bold('File {} Permission Set {}'.format(ldir, '0600')))
                                    except Exception as err:

                                        print(bold(red('Unable to Set file {} permission '.format(ldir))))

                                if ldir == "index.py":
                                    try:
                                        os.chmod(os.getcwd() + '/' + d.get('project', '') + '/' + str(kdir) + '/' + str(
                                            ldir), mode=0o755)
                                        print(bold('File {} Permission Set {}'.format(ldir, '0755')))

                                    except Exception as err:

                                        print(bold(red(__('Unable to Set file {} permission '.format(ldir)))))


                else:

                    if os.path.isfile(os.getcwd() + '/' + d.get('project', '') + '/' + str(
                            kdir) + '/' + direct[kdir]) is False:

                        try:
                            f = open(os.getcwd() + '/' + d.get('project', '') + '/' + str(
                                kdir) + '/' + direct[kdir], 'w+')
                            f.close()

                        except Exception as err:

                            print(bold(red(__(('Unable to create File  {}'.format(kdir))))))

                        finally:

                            print(bold(__('File {} Created Successfully'.format(direct[kdir]))))
                        try:

                            with open(os.getcwd() + '/' + d.get('project', '') + '/' + str(
                                    kdir) + '/' + direct[kdir], 'w+', encoding='utf-8') as f:
                                # context(direct[kdir])
                                f.write(context(direct[kdir]))
                                f.close()


                        except Exception as err:

                            print(bold(red(__('Unable to Write File  {}'.format(direct[kdir])))))

                        finally:
                            print(bold('File {} Rewrite Successfully'.format(direct[kdir])))

    server.serv(os.getcwd() + '/' + d.get('project', ''))


def main(argv: List[str] = sys.argv[1:]) -> int:
    # parse options
    parser = get_parser()
    try:
        args = parser.parse_args(argv)

    except SystemExit as err:
        return err.code

    d = vars(args)
    ask(d)

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
