###
# Author : Betacodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by Betacodings on 2019.
###


import string
import os
from pytonik import Hash, Log, Version
log_msg = Log.Log()

try:
    import http.client as htp
    from http import client
    import urllib as urllib
except Exception as err:
    import httplib as htp
    import urllib2 as urllib


def limit_string(data="", length=10, readmore=""):
    if data != "":
        info = (data[:int(length)] + str(readmore)
                ) if len(data) > int(length) else data
    else:
        info = ""
    return info


def numberformat(num=int):

    if(int(num) > 1000000000):
        getcount = str(int(round((num/1000000000),)))+str('T')

    elif(num > 1000000):
        getcount = str(int(round((num/1000000), 1)))+str('M')

    elif(num > 1000):
        getcount = str(int(round((num/1000), 1)))+str('K')

    else:
        getcount = str(int(round((num/1), 1)))
    return getcount


def humanbytes(B):
    # Return the given bytes as a human friendly KB, MB, GB, or TB string'
    B = float(B)
    KB = float(1024)
    MB = float(KB ** 2)  # 1,048,576
    GB = float(KB ** 3)  # 1,073,741,824
    TB = float(KB ** 4)  # 1,099,511,627,776

    if B < KB:
        return '{0} {1}'.format(B, 'Bytes' if 0 == B > 1 else 'Byte')
    elif KB <= B < MB:
        return '{0:.2f} KB'.format(B/KB)
    elif MB <= B < GB:
        return '{0:.2f} MB'.format(B/MB)
    elif GB <= B < TB:
        return '{0:.2f} GB'.format(B/GB)
    elif TB <= B:
        return '{0:.2f} TB'.format(B/TB)


def file_get_contents(self, filename, use_include_path=0, context=None, offset=-1, maxlen=-1):
    if (filename.find('://') > 0):
        ret = urllib.urlopen(filename).read()
        if (offset > 0):
            ret = ret[offset:]
        if (maxlen > 0):
            ret = ret[:maxlen]
        return ret
    else:
        fp = open(filename, 'rb')
        try:
            if (offset > 0):
                fp.seek(offset)
            ret = fp.read(maxlen)
            return ret
        except Exception as err:
            log_msg.critical(err)
        finally:
            fp.close()


def creatdatetime(datetimeString, formate="%d-%m-%Y"):
    import datetime

    try:
        date = str(datetimeString).split(" ")[-1][:4]
        return datetime.datetime.strptime(date, formate)
        # return type(datetime.strptime(datetimeString, formate).date())
        # return datetimeString if datetimeString is "" or datetimeString is None  else datetime.strptime(datetimeString, formate).date()
    except Exception as err:
        return err


def datetime(formate="%Y-%m-%d %H:%M:%S"):
    from datetime import datetime

    try:
        return datetime.strftime(datetime.now(), formate)

    except Exception as err:
        return err


def iteri(dictionary="", itr="xid"):
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
