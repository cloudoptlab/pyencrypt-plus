"""
@file: Base64Encrypt.py
@time: 2020/1/16 15:45
@description: Simplified sha512 encryption.
"""
from Crypto.Hash.SHA512 import SHA512Hash

from pyencrypt.encrypt.Encrypt import Encrypt


class Sha512Encrypt(Encrypt):

    def encrypt(self, value: str) -> str:
        sha512 = SHA512Hash(value.encode("utf-8"), truncate=None)
        return str(sha512.hexdigest())

    def decrypt(self, value: str) -> str:
        pass

    def key(self, value: str):
        pass
