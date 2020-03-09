# Author : BetaCodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by BetaCodings on 2/24/20.

class Exception:

    def __getattr__(self, item):
        return item

    def __init__(self, error=""):
         self.error = error
         print(error)

