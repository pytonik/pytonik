#!/usr/bin/python

"""
	sphinx.cmd.quickstart
	~~~~~~~~~~~~~~~~~~~~~

	Quickly setup documentation source to work with Sphinx.

	:copyright: Copyright 2007-2019 by the Sphinx team, see AUTHORS.
	:license: BSD, see LICENSE for details.
"""

import argparse
import locale
import os
import re
import sys
import time
import warnings
from pytonik import Version
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

direct = {'controller': 'IndexController.py', 'lang': ['en.py', 'fr.py'], 'model': 'Index.py',
          'public': ['.htaccess', 'index.py'], 'views': 'index.html', '.env': '', '.htaccess': ''}


def context(lg):

    lc = {
        '.htaccess1': """<IfModule mod_rewrite.c>
RewriteEngine on
RewriteRule ^$ public/
RewriteRule (.*) public/$1 [NC,L]
</IfModule>
        """,
        '.htaccess':
        """<IfModule mod_rewrite.c>
DirectoryIndex index.py
Options +ExecCGI
AddHandler cgi-script .py
RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^(.*)$ index.py/$1 [L]
</IfModule>
        """,
        'index.py':
        """#!{}
        \ntry:
        \n  from pytonik import Web
        \nexcept Exception as err:
        \n  exit(err)
        \nApp = Web.App()
        \nApp.runs()

        """.format(os.popen('which python').read()),
         'en.py':'{"lng.test":"sample text"}',
         'fr.py': '{"lng.test":"Exemple de texte"}',
        'index.html':
            """<!DOCTYPE html>
        \n<html lang="en">
<head>
<meta charset="UTF-8">
<title> {{title}}</title>
        \n</head>
<body>
<h1> {{title}}</h1>
\n</body>
</html>
        """,
        'IndexController.py' :
        """from pytonik.Web import App
        \nm = App()
        \ndef index():
            \n  data = {'title': 'Pytonik MVC'}
            \n  m.views('index', data)
            \n

        """,
        '.env':
        """{'route':

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
        'default_languages':'en'}"""

           }

    return lc.get(lg, '')


# function to get input from terminal -- overridden by the test suite
def term_input(prompt: str) -> str:
    if sys.platform == 'win32':
        # Important: On windows, readline is not enabled by default.  In these
        #            environment, escape sequences have been broken.  To avoid the
        #            problem, quickstart uses ``print()`` to show prompt.
        print(prompt, end='')
        return input('')
    else:
        return input(prompt)


def __(l):
    return l


class ValidationError(Exception):
    """Raised for validation errors."""


def is_path(x: str) -> str:
    x = path.expanduser(x)
    if not path.isdir(x):
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
        description=__(""" """))

    parser.add_argument('-q', '--quiet', action='store_true', dest='quiet',
                        default=None,
                        help=__('quiet mode'))
    parser.add_argument('--version', action='version', dest='show_version',
                        version='%%(prog)s %s' % Version.VERSION_TEXT)

    parser.add_argument('path', metavar='PROJECT_DIR', default='.', nargs='?',
                        help=__('project root'))

    return parser


def ask(d: Dict) -> None:
    print(bold('Welcome to the Pytonik MVC Framework %s Start File Structure.' % Version.VERSION_TEXT))

    print(__('''Please enter values for the following settings.
	'''))

    if 'path' in d:
        print(bold('''Selected root path: %s''' % os.getcwd()))
        d['path'] = os.getcwd()

        d['step'] = do_prompt(__(''
                                 'Do you want to create file pytonik in this directory  (y/n)'
                                 ''),
                              'n', boolean)
    else:
        print(__('''Enter the root path for documentation.'''))
        d['path'] = do_prompt(__('Root path for the documentation'), '.', is_path)

    if d.get('step', '') == True:
        if 'project' not in d:
            print(__(''' Provide project name, it will be use in project folder creation, avoid space while typing '''))

            d['project'] = do_prompt(bold('Project name'))
            if d.get('project', '') is not "":

                if os.path.isdir(os.getcwd() + '/' + d.get('project', '')) == False:

                    print(bold('''Project Inprogress ''') + ('please wait..'))

                    try:

                        os.mkdir(os.getcwd() + '/' + d.get('project', ''), mode=0o755)

                        print(bold('Project {} Created Successfully'.format(d.get('project', ''))))

                    except Exception as err:
                        print(red('Unable to create project {} directory'.format(
                            os.getcwd() + '/' + d.get('project', ''))))

                    make_file(direct, d)





                else:
                    d['cont'] = do_prompt(bold('Directory {} already exist, do you want to overwrite directoy (y/n)'.format(d.get('project', ''))),
                                          'n', boolean)
                    if d.get('cont') == True:

                        make_file(direct, d)

                    else:
                        sys.exit(-1)

            else:
                d['quit'] = do_prompt(__('Do you want to quite (y/n)'), 'n', boolean)

    else:
        d['quit'] = do_prompt(__('Do you want to quite (y/n)'), 'n', boolean)

    if d.get('quit', '') == True:
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
            print(bold(('File {} Created Successfully').format(kdir)))

            if os.path.isfile(os.getcwd() + '/' + d.get('project', '') + '/' + str(
                    kdir)) == False:
                try:

                    f = open(os.getcwd() + '/' + d.get('project', '') + '/' + kdir, 'wt',  encoding='utf-8')
                    if kdir == ".htaccess":
                        f.write(context(".htaccess1"))
                    else:
                        f.write(context(kdir))

                    f.close()


                except Exception as err:

                    print(bold(red('Unable to create File  {}'.format(kdir))))

                if os.path.isfile(os.getcwd() + '/' + d.get('project', '') + '/' + str(
                    kdir)) == True:
                    try:
                        os.chmod(os.getcwd() + '/' + d.get('project', '') + '/' + str(kdir), mode=0o600)
                        print(bold('File {} Permission Set {}'.format(kdir, '0600')))
                    except Exception as arr:
                        print(bold(red('Unable to Set file {} permission '.format(kdir))))




        else:

            try:
                os.mkdir(os.getcwd() + '/' + str(d.get('project', '')) + '/' + str(kdir), mode=0o755)

                print(bold('''Folder {} Created Successfully'''.format(kdir)))
            except Exception as err:
                print(bold(red('''Folder  {}  already exist'''.format(kdir))))

            if direct[kdir] is not "":
                if type(direct[kdir]) == list:

                    for ldir in direct[kdir]:
                        if ldir is not "":
                            if os.path.isfile(os.getcwd() + '/' + d.get('project',
                                                                        '') + '/' + str(
                                kdir) + '/' + ldir) == False:
                                try:

                                    f = open(
                                        os.getcwd() + '/' + d.get('project', '') + '/' + str(
                                            kdir) + '/' + ldir, 'wt',  encoding='utf-8')
                                    f.write(context(ldir))
                                    f.close()


                                except Exception as err:

                                    print(bold(red('Unable to create File  {}'.format(ldir))))

                                finally:
                                    print(bold('File {} Created Successfully'.format(ldir)))

                            if os.path.isfile(os.getcwd() + '/' + d.get('project',
                                                                        '') + '/' + str(
                                kdir) + '/' + ldir) == True:

                                if ldir.startswith('.'):
                                    try:
                                        os.chmod(os.getcwd() + '/' + d.get('project', '') + '/' + str(kdir) + '/' + str(ldir), mode=0o600)
                                        print(bold('File {} Permission Set {}'.format(ldir, '0600')))
                                    except Exception as err:

                                        print(bold(red('Unable to Set file {} permission '.format(ldir))))


                                if ldir == "index.py":
                                    try:
                                        os.chmod(os.getcwd() + '/' + d.get('project', '') + '/' + str(kdir) + '/' + str(ldir), mode=0o755)
                                        print(bold('File {} Permission Set {}'.format(ldir, '0755')))

                                    except Exception as err:

                                        print(bold(red('Unable to Set file {} permission '.format(ldir))))


                else:

                    if os.path.isfile(os.getcwd() + '/' + d.get('project', '') + '/' + str(
                            kdir) + '/' + direct[kdir]) == False:

                        try:

                            f = open(os.getcwd() + '/' + d.get('project', '') + '/' + str(
                                kdir) + '/' + direct[kdir], 'w')

                            f.write(context(direct[kdir]))
                            f.close()


                        except Exception as err:

                            print(bold(red('Unable to create File  {}'.format(direct[kdir]))))

                        finally:

                            print(bold('File {} Created Successfully'.format(direct[kdir])))



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
