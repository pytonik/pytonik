###
# Author : Betacodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by Betacodings on 2019.
###

from pytonik.Editor.Compiler import Compiler

class Template(object):
    def __init__(self, contents):
        self.contents = contents
        self.root = Compiler(self.contents).compile()

    def render(self, **kwargs):
        
        return str(self.root.render(kwargs)).replace('\ufeff', ' ').replace('\u20a6', ' ')