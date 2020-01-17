"""
@file: Base64Encrypt.py
@time: 2020/1/16 15:45
@description: Simplified 3d des encryption.
"""
import binascii

from Crypto.Cipher import DES3

from pyencrypt.encrypt.Encrypt import Encrypt


class Des3Encrypt(Encrypt):
    KEY = ''

    def encrypt(self, value: str) -> str:
        des = DES3.new(bytes(self.KEY, encoding="utf8"), DES3.MODE_ECB)
        text = value + (8 - (len(value) % 8)) * '='
        encrypt_text = des.encrypt(text.encode())
        return str(binascii.b2a_hex(encrypt_text))

    def decrypt(self, value: str) -> str:
        des = DES3.new(bytes(self.KEY, encoding="utf8"), DES3.MODE_ECB)
        text = value + (8 - (len(value) % 8)) * '='
        decrrpt_text = des.decrypt(str.encode(text))
        return binascii.b2a_hex(decrrpt_text)

    def key(self, value: str):
        if len(value) > 16:
            self.KEY = value[0, 16]
        else:
            self.KEY = value.ljust(16, '0')
        pass
