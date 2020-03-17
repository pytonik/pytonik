###
# Author : Betacodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by Betacodings on 2019.
###

import hashlib
import os
import re
import binascii
from pytonik import Version


class Hash:

    def __getattr__(self, item):
        return item

    def __init__(self):
        self.salt = ""
        self.hash_str = ""
        self.salt_hx = ""
        self.type_hx = ""
        self.key_hx = ""
        self.mp_str = ""
        self.hx_mp = {}

    def md5(self, provide_string,  encode='utf-8'):
        if encode == "utf-8":
            hashlibS = hashlib.md5(
                str(provide_string).encode(encode)).hexdigest()
        else:
            hashlibS = hashlib.md5(str(provide_string).encode(
                'utf-8')).hexdigest().encode(encode)

        return hashlibS

    def sha1(self, provide_string,  encode='utf-8'):

        if encode == "utf-8":
            hashlibS = hashlib.sha1(
                str(provide_string).encode(encode)).hexdigest()
        else:
            hashlibS = hashlib.sha1(str(provide_string).encode(
                'utf-8')).hexdigest().encode(encode)

        return hashlibS

    def sha224(self, provide_string,  encode='utf-8'):
        if encode == "utf-8":
            hashlibS = hashlib.sha224(
                str(provide_string).encode(encode)).hexdigest()
        else:
            hashlibS = hashlib.sha224(str(provide_string).encode(
                'utf-8')).hexdigest().encode(encode)
        return hashlibS

    def sha256(self, provide_string,  encode='utf-8'):
        if encode == "utf-8":
            hashlibS = hashlib.sha256(
                str(provide_string).encode(encode)).hexdigest()
        else:
            hashlibS = hashlib.sha256(str(provide_string).encode(
                'utf-8')).hexdigest().encode(encode)
        return hashlibS

    def sha384(self, provide_string, encode='utf-8'):
        if encode == "utf-8":
            hashlibS = hashlib.sha384(
                str(provide_string).encode(encode)).hexdigest()
        else:
            hashlibS = hashlib.sha384(str(provide_string).encode(
                'utf-8')).hexdigest().encode(encode)
        return hashlibS

    def sha512(self, provide_string,  encode='utf-8'):
        if encode == "utf-8":
            hashlibS = hashlib.sha512(
                str(provide_string).encode(encode)).hexdigest()
        else:
            hashlibS = hashlib.sha512(str(provide_string).encode(
                'utf-8')).hexdigest().encode(encode)

        return hashlibS

    def hex_hash(self, provide_string, hex_type='sha256', salt="", size=60):
        
        if salt == "":
            self.salt = self.type_hash(hex_type, os.urandom(int(size)))
            
        else:
            self.salt = salt
        try:
            self.hash_str = hashlib.pbkdf2_hmac(hex_type, str(provide_string).encode('utf-8'),  bytes(self.salt), 100000)
            self.hash_str = binascii.hexlify(self.hash_str)
            return (self.salt+self.hash_str).decode("ascii")
        except Exception as err:
            self.hash_str = hashlib.pbkdf2_hmac(hex_type, str(provide_string).encode('utf-8'),  self.salt.encode('utf-8'), 100000)
            self.hash_str = binascii.hexlify(self.hash_str).decode("ascii")
            return self.hash_str
        
    def type_hash(self, hex_type="sha256", salt="", encode="ascii"):

        salt_re = ""

        if hex_type == "sha256":

            salt_re = self.sha256(provide_string=salt, encode=encode)

        elif hex_type == "sha384":

            salt_re = self.sha384(provide_string=salt, encode=encode)

        elif hex_type == "sha512":

            salt_re = self.sha512(provide_string=salt, encode=encode)

        elif hex_type == "sha1":

            salt_re = self.sha1(provide_string=salt, encode=encode)

        elif hex_type == "md5":

            salt_re = self.md5(provide_string=salt, encode=encode)
        else:
            salt_re = ""

        return salt_re

    def _s_k_(self, stored_hash=""):

        try:
            if Version.PYVERSION_MA >= 3:
                rehx = Version.HASH_PRE.items()
            else :
                rehx = Version.HASH_PRE.iteritems()

            for k, v in rehx:
                len_hash = len(stored_hash)
                
                if int(k) == len_hash:
                    self.type_hx = v
                    self.salt_hx = stored_hash[:int(int(k)/2)]
                    self.key_hx = stored_hash[int(int(k)/2):]
            return True
            
        except Exception as err:
            return False

    def verify(self, stored_hash, provide_string):
        try:
            if self._s_k_(stored_hash) == True:
               
                get_hash = self.hex_hash(provide_string=provide_string, hex_type=self.type_hx, salt=self.salt_hx)
                
                if get_hash == self.key_hx:
                    return True
                else:
                    return False
            else:
                return False
        except Exception as err:
            
            return False

    def map_hash(self, map_string):
        self.mp_str = map_string
        self.hx_mp[map_string] = {
            'salt': self.salt,
            'key': self.hash_str,
        }
        
        return self.hx_mp

    
    def map_check(self, provide_string):
        self.salt_hx = self.hx_mp[self.mp_str]["salt"]
        self.key_hx = self.hx_mp[self.mp_str]["key"]
        self.atr_hx = Version.HASH_PRE.get(str(len(self.salt_hx)+len(self.key_hx)))
        stored_hash = self.hex_hash(provide_string=provide_string, hex_type=self.atr_hx, salt=self.salt_hx)
        return self.verify(stored_hash, provide_string)
   
  

