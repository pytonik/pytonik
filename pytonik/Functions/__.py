# Author : BetaCodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by BetaCodings on 07/11/2019.

from pytonik.Lang import Lang
from pytonik.Controllers import Controllers


class __():

    def __getattr__(self, item):
        return item

    def __call__(self, *args, **kwargs):

        return None

    def __init__(self, *args, **kwargs):
        self.langs = Lang(Controllers().languages)
        self.langs.loadLang()
        if len(args) > 0 or len(kwargs) > 0:
            if all(args) != False:
                self.lg = self.lang(*args, **kwargs)
            else:
                self.lg = self.lang(**kwargs)
		
        return None

    def __str__(self):

        return self.lg


    def lang(self, lang="", defindValue = ''):
        if lang != "":
            return self.langs.get(lang, defindValue)



    def default(self):

        return self.langs.lg
