"""
@file: Base64Encrypt.py
@time: 2020/1/16 15:45
@description: Simplified sha1 encryption.
"""

from Crypto.Hash.SHA1 import SHA1Hash

from pyencrypt.encrypt.Encrypt import Encrypt


class Sha1Encrypt(Encrypt):

    def encrypt(self, value: str) -> str:
        sha1 = SHA1Hash()
        sha1.update(value.encode("utf-8"))
        return str(sha1.hexdigest())

    def decrypt(self, value: str) -> str:
        pass

    def key(self, value: str):
        pass
