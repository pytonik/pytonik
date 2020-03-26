# Author : BetaCodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by BetaCodings on 2/25/20.
from pytonik import Version, Config
import sys, os, re, pkg_resources
from pytonik.Log import Log


#Handles installation of pytonik project dependencies
class requirement:

    def __getattr__(self, item):
        return item

    def __init__(self):
        return None

    #The ``run``` method trigger Terminal command using `os` module and support both
    #windows, linux, mac os, ubuntu etc.  
    def run(self, pacakage, dir=""):
        dir_new = ' --install-option="--prefix={dir} "'.format(dir=dir) if dir != "" else ""
        cmd = "pip install {dir}{pacakage}".format(dir=dir_new, pacakage=pacakage)

        try:

            terminal = os.popen(cmd).read()
            print(terminal)
        except Exception as err:
            try:
                terminal =  os.system(cmd)
                print(terminal)
            except Exception as err:
                print(err)
                Log().critical(err)

    def rf(self, dir=""):

        if os.path.isdir(os.getcwd() + '/public'):
            host = os.getcwd()  # os.path.dirname(os.getcwd())

        else:
            host = os.path.dirname(os.getcwd())

        DS = str("/")

        requirepath = host + DS + "requirements.txt"
        if os.path.isfile(requirepath) == True:

            try:
                fb = open(requirepath, "r")
                ne_package = re.findall(r"\S+", fb.read())
                for l in ne_package:
                    self.check_package(l, dir)
                fb.close()
            except Exception as err:
                print(err)
                Log().error(err)
        else:
            print("Requirement file is not Found in this directory")



    def check_package(self, package, dir=""):

        installed_packages = pkg_resources.working_set
        installed_packages_list = sorted(["%s==%s" % (i.key, i.version) for i in installed_packages])
        package_n  = ""
        newpackage = package.split('==')[0]
        lis = []
        for packall in installed_packages_list:
            lis.append(str(str(packall).split('==')[0]).lower())


        if str(newpackage).lower() not in lis :
            self.run(package, dir)