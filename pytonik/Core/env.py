# Author : BetaCodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by BetaCodings on 2/24/20.


class env:



    def __init__(self):
        return None

    def _e(self):

        from pytonik import Version, Config


        import sys, os

        if os.path.isdir(os.getcwd() + '/public'):
            host = os.getcwd()  # os.path.dirname(os.getcwd())

        else:
            host = os.path.dirname(os.getcwd())

        DS = str("/")

        envpath = host + DS + ".env"

        if os.path.isfile(envpath) == True:

            try:
                f = open(envpath, "r")
                return f.read()
            except Exception as err:
                   print(err)
        else:

            print(".env file not found")
