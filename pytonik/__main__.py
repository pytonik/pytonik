# Author : BetaCodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by BetaCodings on 13/01/2020.


import sys

from pytonik.cmd import start
from pytonik.cmd import server
from pytonik.cmd import doc
from pytonik.cmd import install
from pytonik.cmd import help

if __name__ == '__main__':
    sys.exit(start.main(sys.argv[1:]))

if __name__ == '__main__':
    sys.exit(server.main(sys.argv[1:]))

if __name__ == '__main__':
    sys.exit(doc.main(sys.argv[1:]))

if __name__ == '__main__':
    sys.exit(install.main(sys.argv[1:]))

if __name__ == '__main__':
    sys.exit(help.main(sys.argv[1:]))

