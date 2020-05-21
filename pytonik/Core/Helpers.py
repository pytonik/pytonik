###
# Author : Betacodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by Betacodings on 2019.
###


import importlib
import os
import sys
import re
from pytonik.Editor import HTMLeditor
from pytonik import Log


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
            dirF = list(filter(None, fileExists))
            template_dir = host + DS + 'views' + DS + dirF[0] + DS
            engine = dirF[1]

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
            return err

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
            return err


if "url" not in dir(os):

    def url(path="", lang=False):
        from pytonik.Router import Router
        from pytonik.util.Variable import Variable

        ront = Router()
        env_os = Variable()
        DS, p, url = "", "",  ""
        seturl = ront.out("HTTP_HOST")+str(":")+str(env_os.out("SERVER_PORT", '')) if env_os.out(
            "HTTP_HOST") == "localhost" or env_os.out("HTTP_HOST") == "127.0.0.1" else env_os.out("HTTP_HOST")

        if ront.out("HTTPS", "") == 'on':

            url = str("https://") + seturl.replace(":80", "") + "/" + ront.alllanguages.get(ront.getLanguages(), ront.getLanguages()) if lang == True else str(
                "https://") + seturl.replace(":80", "")
        else:
            url = str("http://") + seturl.replace(":80", "") + "/" + ront.alllanguages.get(ront.getLanguages(),
                                                                                           ront.getLanguages()) if lang == True else str("http://") + seturl.replace(":80", "")

        if path == "":
            DS = ""
        else:
            if path[:1] == "/":
                p = path[1:]
                DS = "/"
            else:
                p = path
                DS = "/"

        return url + DS + p

if "public_path" not in dir(os):
    def public_path(path=""):
        DS = str('/')
        return url(DS+'public'+DS+path)


if "covert_list_dict" not in dir(os):
    def covert_list_dict(list):
        itlist = iter(list)
        try:
            return dict(zip(itlist, itlist))
        except Exception as err:
            log_msg.error(err)
            return err


if "mvc_dir" not in dir(os):
    def mvc_dir(path, permission=""):
        dpp = path[len(str(path))-1]
        if '/' in dpp:
            newpath = path[:-1]
        else:
            newpath = path

        if os.path.isdir(os.getcwd() + '/public'):
            host = str(os.getcwd()).replace("\\", "/")  # os.path.dirname(os.getcwd())

        else:
            host = str(os.path.dirname(os.getcwd())).replace("\\", "/") 

        DS = str("/")
        dir_s = host + newpath + DS
        dir_res = ""
        if os.path.exists(dir_s) == True:
            dir_res = dir_s
        else:
            try:
                os.mkdir(dir_s)
                dir_res = dir_s
            except Exception as err:
                try:
                    os.makedirs(dir_s)
                    dir_res = dir_s
                except Exception as err:
                    dir_res = dir_s
        if permission != "":
            try:
                os.chmod(path=dir_s, mode=permission)
            except Exception as err:
                dir_res = dir_s

        return dir_res


if "key_tag" not in dir(os):
    def key_tag(tag, url="/", css=""):

        pattern = re.compile("\s*,\s*|\s+$")

        split_tag = [x for x in pattern.split(tag) if x]
        for keyword in split_tag:
            return '<li><a href="{url}" class="{css}">{keyword}</a></li>'.format(css=css, keyword=str(keyword))

if "alphanumeric" not in dir(os):
    def alphanumeric(string):
        return re.sub("[^a-zA-Z0-9]+", " ", string)


if "rand" not in dir(os):
    def rand(limit=0, list=1):
        import random
        num = {
            1: 10,
            2: 120,
            3: 1230,
            4: 12340,
            5: 123450,
            6: 1234560,
            7: 12345670,
            8: 123456780,
            9: 1234567890,
            10: 12345678900,
        }
        for x in range(list):
            ran = random.randint(limit, num[limit])
            return ran
if "iteration" not in dir(os):

    def iteration(dictionary="", itr="pid"):
        i = 0
        if dictionary != "" or dictionary != None:
            dist, apend = [], []
            for l in dictionary:
                i += 1
                ++i
                listv = l
                dist = {itr: i}
                dist.update(listv)
                apend.append(dist)
            return apend
