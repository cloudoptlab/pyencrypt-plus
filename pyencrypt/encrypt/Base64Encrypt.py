"""
@file: Base64Encrypt.py
@time: 2020/1/16 15:45
@description: Simplified base64 encryption.
"""
import base64

from pyencrypt.encrypt.Encrypt import Encrypt


class Base64Encrypt(Encrypt):
    def encrypt(self, value: str) -> str:
        return str(base64.b64encode(value.encode('utf-8')), encoding='utf-8')

    def decrypt(self, value: str) -> str:
        return str(base64.b64decode(value.encode('utf-8')), encoding='utf-8')

    def key(self, value: str):
        pass
