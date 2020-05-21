from pytonik.Log import Log
from pytonik.App import App
from pytonik.Functions.validation import validation
import os, random, string

log_msg = Log()
Ap = App()


class rand(validation):
    def __getattr__(self, item):
        return item

    def __init__(self, *args, **kwargs):
        if len(args) > 0 or len(kwargs) > 0:
            if all(args) != False:
                self.pt = self.number(*args, **kwargs)
            else:
                self.pt = self.number(**kwargs)

        return None

    def __str__(self):

        return self.pt

    def number(self, size=6, list=1):

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
        ran = []
        for x in range(list):
            ran.append(str(random.randint(size, num[size])))
            
        return "".join(ran) if self.count(ran) < 2 else ran

    def chars(self, size=6, list=1, transform = "lower"):
        transform_s = string.ascii_uppercase if transform == "upper" else string.ascii_lowercase
        strg =  transform_s + string.digits
        ran = []
        for x in range(list):
            ran.append("".join(random.choices(strg, k=size)))

        return "".join(ran) if self.count(ran) < 2 else ran

    def serial(self, size=3, portion=3, sign='-', transform = "lower"):
        transform_s = string.ascii_uppercase if transform == "upper" else string.ascii_lowercase

        strg = transform_s + string.digits
        i = 0
        ran = []
        for x in range(portion):
            ran.append("".join(random.choices(strg, k=size)))

        return str(sign).join(ran)



