"""
@file: Base64Encrypt.py
@time: 2020/1/16 15:45
@description: Simplified des encryption.
"""
import binascii

from Crypto.Cipher import DES

from pyencrypt.encrypt.Encrypt import Encrypt


class DesEncrypt(Encrypt):
    KEY = ''

    def encrypt(self, value: str) -> str:
        des = DES.new(bytes(self.KEY, encoding="utf8"), DES.MODE_ECB)
        text = value + (8 - (len(value) % 8)) * '='
        encrypt_text = des.encrypt(text.encode())
        return str(binascii.b2a_hex(encrypt_text))

    def decrypt(self, value: str) -> str:
        des = DES.new(bytes(self.KEY, encoding="utf8"), DES.MODE_ECB)
        text = value + (8 - (len(value) % 8)) * '='
        decrrpt_text = des.decrypt(str.encode(text))
        return binascii.b2a_hex(decrrpt_text)

    def key(self, value: str):
        if len(value) > 8:
            self.KEY = value[0, 8]
        else:
            self.KEY = value.ljust(8, '0')
        pass
