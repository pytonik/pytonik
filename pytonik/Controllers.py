###
# Author : Betacodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by Betacodings on 2019.
###

from pytonik import App


class Controllers(App):
    global data
    global model
    global params

    def getDate(self):
        return self.data

    def getModel(self):
        return self.model

    def getParams(self):
        return self.params

    def __init__(self, datag={}, datal={}):
        self.App = App
        self.datag = datag
        self.datal = datal
        self.params = self.App.getRouters()
        self.keys = dict()
