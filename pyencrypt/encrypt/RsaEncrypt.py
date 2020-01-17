"""
@file: RsaEncrypt.py
@time: 2020/1/16 15:45
@description: Simplified rsa encryption.
"""
import base64

from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA

from pyencrypt.encrypt.Encrypt import Encrypt


class RsaEncrypt(Encrypt):
    KEY = ''

    def encrypt(self, value: str) -> str:
        rsakey = RSA.importKey(self.KEY)
        cipher = PKCS1_v1_5.new(rsakey)
        cipher_text = base64.b64encode(cipher.encrypt(bytes(value, encoding='utf-8')))
        return str(cipher_text, encoding='utf-8')

    def decrypt(self, value: str) -> str:
        rsakey = RSA.importKey(self.KEY)
        cipher = PKCS1_v1_5.new(rsakey)
        text = cipher.decrypt(base64.b64decode(bytes(value, encoding='utf-8')), "ERROR")
        return str(text, encoding='utf-8')

    def key(self, value: str):
        self.KEY = value

    def creat_key(self, length=1024):
        random_generator = Random.new().read
        rsa = RSA.generate(length, random_generator)
        private_pem = rsa.exportKey()
        public_pem = rsa.publickey().exportKey()
        print("==========Public Key==========")
        print(str(public_pem, encoding='utf-8'))
        print("==========Private Key==========")
        print(str(private_pem, encoding='utf-8'))
