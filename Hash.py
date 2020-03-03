###
# Author : Betacodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by Betacodings on 2019.
###

import hashlib, os
class Hash:

    def __init__(self):
        self.hash = hashlib
        self.hashS = ""
        self.salt = os.urandom(32)
        self.storage = ""


    def md5(self, string = "",  ency = 'utf-8'):
        if string != "":
            self.hashS =  self.hash.md5(string.encode(ency)).hexdigest()
            return self.hashS

    def sha1(self, string = "",  ency = 'utf-8'):
        if string != "":
            self.hashS = self.hash.sha1(string.encode(ency)).hexdigest()
        return self.hashS

    def sha384(self, string="", ency='utf-8'):
        if string != "":
            self.hashS = self.hash.sha384(string.encode(ency)).hexdigest()
        return self.hashS

    def hex_hash(self, string = "",  hashType ='sha256',  salt = "", ency = 'utf-8'):
        if salt == "":
            vsalt = self.salt
        else:
            self.salt = salt
            vsalt = self.salt

        self.hashS = self.hash.pbkdf2_hmac(hashType, string.encode(ency),  vsalt, 100000)


        return self.hashS

    def get_hash_sha256(self, type = 'key'):

        self.storage = self.salt + self.hashS
        value = ""
        if type == "key":
            value = self.storage[:32]
        elif type == "salt":
            value = self.storage[32:]
        else:
            return "Invalid type, choose key or salt"
        return value

    def verify_hash(self, key):

        if self.hashS == key:
            return True
        else:
            return False
