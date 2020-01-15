###
# Author : Betacodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by Betacodings on 2019.
###



import importlib, os, sys, re
from ..Editor import HTMLeditor
from .. import Log
log_msg = Log.Log()

class Helpers():

    def __init__(self):
        return None

    def __call__(self, *args, **kwargs):
        return None

if "includeFile" not in dir(os):
    def includeFile(path, datag={}, datal={}):

        host = os.path.dirname(os.getcwd())
        DS = str("/")
        path = '.'+path

        split = path.split('.')

        fileExists = []
        for x in split:

            #fileExists = str(x)
            fileExists.append(x)
        try:
            dirF =  list(filter(None, fileExists))
            template_dir = host + DS + 'views' + DS + dirF[0] + DS
            engine  = dirF[1]


            if os.path.isdir(template_dir) == True:
                dataG = datag
                dataL = datal
                html_file_path = os.path.join(template_dir, "%s.html" % engine)

                with open(html_file_path) as html_file:
                    html = html_file.read()
                return HTMLeditor.Template(html).render(**dataG)

            else:
              return "The file {filepath} does not exists.".format(filepath=template_dir)

        except Exception as err:
                log_msg.error(err)
                return  err

if "callfunc" not in dir(os):
    def callfunc(myfile, myfunc, *args):
        pathname, filename = os.path.split(myfile)
        sys.path.append(os.path.abspath(pathname))
        modname = os.path.splitext(filename)[0]
        mymod = importlib.import_module(modname)
        try:
            result = getattr(mymod, myfunc)(*args)
            return result
        except Exception as err:
                log_msg.error(err)
                return  err


if "url" not in dir(os):
    def url(path = ""):
        http = os.environ.get("HTTPS")
        if http == 'on':
            url = str("https://") + os.environ.get("HTTP_HOST")
        else:
            url = str("http://") + os.environ.get("HTTP_HOST")

        return url+path

if "public_path" not in dir(os):
    def public_path(path = ""):
        DS = str('/');
        return url(DS+'public'+DS+path);


if "covert_list_dict" not in dir(os):
    def covert_list_dict(list):
        itlist = iter(list)
        try:
            return dict(zip(itlist, itlist))
        except Exception as err:
            log_msg.error(err)
            return  err



if "mvc_dir" not in dir(os):
    def mvc_dir(path):
        dpp =  path[len(str(path))-1]
        if '/' in dpp :
            newpath = path[:-1]
        else:
            newpath = path
        host = str(os.path.dirname(os.getcwd()))
        DS = str("/")
        dir = host + DS + newpath + DS
        return dir


if "key_tag" not in dir(os):
    def key_tag(tag, url="/", css=""):

        pattern = re.compile("\s*,\s*|\s+$")

        split_tag = [x for x in pattern.split(tag) if x]
        for keyword in split_tag:
            return '<li><a href="{url}" class="{css}">{keyword}</a></li>'.format(css = css, keyword = str(keyword))
