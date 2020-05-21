# Author : BetaCodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by BetaCodings on 19/11/2019.

from datetime import datetime, date, timedelta


class now:

    def __getattr__(self, item):
        return item

    def __init__(self, *args, **kwargs):

        self.fmt = ""
        self.date_time = ""
        if len(args) > 0 or len(kwargs) > 0:

            if all(args) != False:
                self.ag_o = self.datetime(*args, **kwargs)
            else:
                self.ag_o = self.datetime(**kwargs)

        return None

    def __str__(self):
        return self.ag_o


    def ago(self, string="", format=""):

        self.date_time = string

        self.fmt = self.format(format)
        delta = self.delta()
        if delta.find(',') > 0:
            days, hours = delta.split(',')
            days = int(days.split()[0].strip())
            hours, minutes = hours.split(':')[0:2]
        else:
            hours, minutes = delta.split(':')[0:2]
            days = 0
        days, hours, minutes = int(days), int(hours), int(minutes)
        datelets = []
        years, months, xdays = None, None, None
        plural = lambda x: 's' if x != 1 else ''
        if days >= 365:
            years = int(days / 365)
            datelets.append('%d year%s' % (years, plural(years)))
            days = days % 365
        if days >= 30 and days < 365:
            months = int(days / 30)
            datelets.append('%d month%s' % (months, plural(months)))
            days = days % 30
        if not years and days > 0 and days < 30:
            xdays = days
            datelets.append('%d day%s' % (xdays, plural(xdays)))
        if not (months or years) and hours != 0:
            datelets.append('%d hour%s' % (hours, plural(hours)))
        if not (xdays or months or years):
            datelets.append('%d minute%s' % (minutes, plural(minutes)))

        return ', '.join(datelets) + ' ago.'




    def delta(self):
        current_datetime = datetime.now()

        try:
            return str(current_datetime - self.fmt)
        except Exception as err:
            return err


    def format(self, fmt=''):

        fmt = '%Y-%m-%d %H:%M:%S' if fmt == "" else  fmt
        try:
            return datetime.strptime(self.date_time, fmt)
        except Exception as err:
            return err

    def time(self, format='%H:%M:%S'):
        try:
            return datetime.strftime(datetime.now(), format)

        except Exception as err:
            return err

    def unix(self, type="int"):
        try:
            import time
            if type == "float":
                return time.time()
            else:
                return int(time.time())
        except Exception as err:
            return err
            
    def date(self, format="%Y-%m-%d"):
        try:
            return datetime.strftime(datetime.now(), format)

        except Exception as err:
            return err

    def datetime(self, format="%Y-%m-%d %H:%M:%S"):

        try:
            return datetime.strftime(datetime.now(), format)

        except Exception as err:
            return err

    def create(self, string="", oldformat="%Y-%m-%d %H:%M:%S", newformat="%d-%m-%Y"):

        try:

            dt = datetime.strptime(str(string), str(oldformat))
            return dt.strftime(str(newformat))

        except Exception as err:
            return err

    def timestamp(self, string = ""):

        try:
            date_s = datetime.fromtimestamp(int(string)) if string !="" else datetime.now().strftime("%s")

            return date_s

        except Exception as err:
            return err

    def past(self, days=0,  seconds=0,minutes=0,hours=0, weeks=0):
        try:
            return  datetime.now() - timedelta(days=int(days), seconds=int(seconds),minutes=int(minutes), hours=int(hours), weeks=int(weeks))
        except Exception as err:
            return err


    def future(self, days=0,  seconds=0,minutes=0,hours=0, weeks=0):
        try:
            return  datetime.now() + timedelta(days=int(days), seconds=int(seconds),minutes=int(minutes), hours=int(hours), weeks=int(weeks))
        except Exception as err:
            return err


    def subtract(self, date1='', format1='',  date2='', format2=''):

        try:
            d1 = datetime.strptime(date1, format1)

            d2 = datetime.strptime(date2, format2)
            return abs((d2 - d1).days)
        except Exception as err:
            return err







