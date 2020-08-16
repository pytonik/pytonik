###
# Author : Betacodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by Betacodings on 2019.
###
def Model():
    from . import Model
    return Model


Model().auto()


def App():
    from . import App
    return App.App()


def Version():
    from . import Version as vern
    return vern


def Config():
    from . import Config as Config
    return Config.Config()


def Helpers():
    from .Core import Helpers
    return Helpers


def Session():
    from .Session import Session
    return Session()


def Request():
    from .Request import Request
    return Request()


def Hash():
    from .Hash import Hash
    return Hash()




def Load(m):
    return Model().Model().load(m)


def Functions():
    from .Core import Functions
    return Functions


def Pagination():
    from pytonik.Functions.pagination import pagination
    return pagination


def Validation():
    from pytonik.Functions.validation import validation
    return validation


def curl():
    from pytonik.Functions.curl import curl
    return curl


def now():
    from pytonik.Functions.now import now
    return now


def os():
    from pytonik.Functions.agent import os
    return os


def browser():
    from pytonik.Functions.agent import browser
    return browser


def extend():
    from pytonik.Functions.extend import extend
    return extend


def path():
    from pytonik.Functions.path import path
    return path


def include():
    from pytonik.Functions.include import include
    return include


def File():
    from .Core import File

    return File


def SendEmail(from_send, to_recipient, message_subject="", messege_content=""):
    from .Core.SMTP import SMTP

    return SMTP().send(from_send, to_recipient, message_subject, messege_content)

def mailer():
    from .Core.SMTP import SMTP

    return SMTP()


def Logs():
    from .Log import Log

    return Log()


def url(path="", lang=False):
    from pytonik.Functions.url import url
    return url(path, lang)


def env(key):

    return App().envrin(key)

def encode(source):
    from pytonik.util.Crypt import Crypt
    return Crypt._encode(source)

def decode(source):
    from pytonik.util.Crypt import Crypt
    return Crypt._decode(source)