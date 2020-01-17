"""
@file: MD5Encrypt.py
@time: 2020/1/16 15:45
@description: Simplified md5 encryption.
"""
from Crypto.Hash.MD5 import MD5Hash

from pyencrypt.encrypt.Encrypt import Encrypt


class Md5Encrypt(Encrypt):
    def encrypt(self, value: str) -> str:
        md5 = MD5Hash()
        md5.update(value.encode("utf-8"))
        return str(md5.hexdigest())

    def decrypt(self, value: str) -> str:
        pass

    def key(self, value: str):
        pass
