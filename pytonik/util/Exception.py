# Author : BetaCodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by BetaCodings on 2/24/20.

from pytonik.Log import Log

class LogError(Exception):
    
    def __getattr__(self, item):
        return item

    def __init__(self, error=""):
         self.error = error
         
    def __str__(self):
        return self.error


class TemplateError(Exception):
    pass


class TemplateContextError(TemplateError):

    def __init__(self, context_var):
        self.context_var = context_var


    def __str__(self):
        Log('').error("cannot resolve '{}'".format(self.context_var))
        return "cannot resolve '{}'".format(self.context_var)


class TemplateSyntaxError(TemplateError):

    def __init__(self, error_syntax):
        self.error_syntax = error_syntax

    def __str__(self):
        Log('').error(" '{}' seems like invalid syntax".format(self.error_syntax))
        return "'{}' seems like invalid syntax".format(self.error_syntax)

