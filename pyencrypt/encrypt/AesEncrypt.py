"""
@file: MD5Encrypt.py
@time: 2020/1/16 15:45
@description: Simplified aes encryption.
"""
import base64

from Crypto.Cipher import AES

from pyencrypt.encrypt.Encrypt import Encrypt


class AesEncrypt(Encrypt):
    KEY = ''

    def encrypt(self, value: str) -> str:
        key_bytes = bytes(self.KEY, encoding='utf-8')
        iv = key_bytes
        cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
        content_padding = self.pkcs7_padding(value)
        encrypt_bytes = cipher.encrypt(bytes(content_padding, encoding='utf-8'))
        result = str(base64.b64encode(encrypt_bytes), encoding='utf-8')
        return result

    def decrypt(self, value: str) -> str:
        key_bytes = bytes(self.KEY, encoding='utf-8')
        iv = key_bytes
        cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
        encrypt_bytes = base64.b64decode(value)
        decrypt_bytes = cipher.decrypt(encrypt_bytes)
        result = str(decrypt_bytes, encoding='utf-8')
        result = self.pkcs7_un_padding(result)
        return result

    def key(self, value: str):
        if len(value) > 16:
            self.KEY = value[0, 16]
        else:
            self.KEY = value.ljust(16, '0')
        pass

    def pkcs7_padding(self, value):
        bs = AES.block_size  # 16
        length = len(value)
        bytes_length = len(bytes(value, encoding='utf-8'))
        # In UTF-8 encoding, English takes up 1 byte, while Chinese takes up 3 bytes.
        padding_size = length if (bytes_length == length) else bytes_length
        padding = bs - padding_size % bs
        # Chr (padding) looks at the conventions with other languages, some of which use '\ 0'
        padding_text = chr(padding) * padding
        return value + padding_text

    def pkcs7_un_padding(self, value):
        length = len(value)
        un_padding = ord(value[length - 1])
        return value[0:length - un_padding]
