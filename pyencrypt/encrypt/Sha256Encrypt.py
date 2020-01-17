"""
@file: Base64Encrypt.py
@time: 2020/1/16 15:45
@description: Simplified sha256 encryption.
"""

from Crypto.Hash.SHA256 import SHA256Hash

from pyencrypt.encrypt.Encrypt import Encrypt


class Sha256Encrypt(Encrypt):

    def encrypt(self, value: str) -> str:
        sha256 = SHA256Hash()
        sha256.update(value.encode("utf-8"))
        return str(sha256.hexdigest())

    def decrypt(self, value: str) -> str:
        pass

    def key(self, value: str):
        pass
