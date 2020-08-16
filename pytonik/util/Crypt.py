###
# Author : Betacodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by Betacodings on 2019.
###


from pytonik.Version import *

class Crypt:

    def __getattr__(self, item):
        return item

    def __init__(self):
        
        return None

    @staticmethod
    def _encode(source):
        from pytonik.Functions.now import now
        from pytonik.Functions.rand import rand
        from pytonik.Hash import Hash
        sessionRAND =  Hash().hex_hash(rand().number(8), hex_type="{}".format(HASH_PRE["64"]), size=120)
        sessionTIMER = Hash().hex_hash(now().unix(), hex_type="{}".format(HASH_PRE["192"]), size=80)
        
        try:
            import six
            import base64
            if six.PY3:
                source = str(sessionPREFIX+sessionRAND+source+str(sessionTIMER)).encode('utf-8')
            content = base64.b64encode(source).decode('utf-8')
            return str(content)
        except Exception as err:
            return str(source)

    @staticmethod
    def _decode(source):
        try:
            import six
            import base64
            source = base64.b64decode(str(source)).decode()
            source = source.split("::")
            source = source[1][64:-192]
            try:
                return source if isinstance(int(source), int) == True else source
            except Exception as err:
                return Session()._decode(source)
        except Exception as err:
            return source