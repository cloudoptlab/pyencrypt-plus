"""
@file: test_snowflake.py
@time: 2020/1/16 14:19
@description: Test all functions.
"""
import logging
import os, sys

sys.path.append(os.getcwd())
logging.basicConfig(level=logging.DEBUG)


def test_creat_snowflake():
    from pyencrypt.ids.IdsCreator import IdsCreator
    from pyencrypt.ids.SnowFlakeCreator import SnowFlakeCreator
    greator: IdsCreator = SnowFlakeCreator()
    greator.set_datacenter(1)
    greator.set_sequence(2)
    greator.set_worker(3)
    logging.info(greator.creat())


def test_creat_uuid():
    from pyencrypt.ids.IdsCreator import IdsCreator
    from pyencrypt.ids.UUIDCreator import UUIDCreator
    greator: IdsCreator = UUIDCreator()
    greator.set_datacenter("TideSwing")
    greator.set_sequence("10000")
    greator.set_worker(3)
    logging.info(greator.creat())


def test_base64():
    from pyencrypt.encrypt.Encrypt import Encrypt
    from pyencrypt.encrypt.Base64Encrypt import Base64Encrypt
    encrypt: Encrypt = Base64Encrypt()
    temp: str = encrypt.encrypt("Hello World!")
    logging.info(temp)
    logging.info(encrypt.decrypt(temp))


def test_md5():
    from pyencrypt.encrypt.Encrypt import Encrypt
    from pyencrypt.encrypt.Md5Encrypt import Md5Encrypt
    encrypt: Encrypt = Md5Encrypt()
    temp: str = encrypt.encrypt("Hello World!")
    logging.info(temp)


def test_des():
    from pyencrypt.encrypt.Encrypt import Encrypt
    from pyencrypt.encrypt.DesEncrypt import DesEncrypt
    encrypt: Encrypt = DesEncrypt()
    encrypt.key("a")
    temp: str = encrypt.encrypt("Hello World!")
    logging.info(temp)
    logging.info(encrypt.decrypt(temp))


def test_3des():
    from pyencrypt.encrypt.Encrypt import Encrypt
    from pyencrypt.encrypt.Des3Encrypt import Des3Encrypt
    encrypt: Encrypt = Des3Encrypt()
    encrypt.key("a")
    temp: str = encrypt.encrypt("Hello World!")
    logging.info(temp)
    logging.info(encrypt.decrypt(temp))


def test_sha1():
    from pyencrypt.encrypt.Encrypt import Encrypt
    from pyencrypt.encrypt.Sha1Encrypt import Sha1Encrypt
    encrypt: Encrypt = Sha1Encrypt()
    temp: str = encrypt.encrypt("Hello World!")
    logging.info(temp)


def test_sha256():
    from pyencrypt.encrypt.Encrypt import Encrypt
    from pyencrypt.encrypt.Sha256Encrypt import Sha256Encrypt
    encrypt: Encrypt = Sha256Encrypt()
    temp: str = encrypt.encrypt("Hello World!")
    logging.info(temp)


def test_sha512():
    from pyencrypt.encrypt.Encrypt import Encrypt
    from pyencrypt.encrypt.Sha512Encrypt import Sha512Encrypt
    encrypt: Encrypt = Sha512Encrypt()
    temp: str = encrypt.encrypt("Hello World!")
    logging.info(temp)


def test_aes():
    from pyencrypt.encrypt.Encrypt import Encrypt
    from pyencrypt.encrypt.AesEncrypt import AesEncrypt
    encrypt: Encrypt = AesEncrypt()
    encrypt.key('aaa')
    temp: str = encrypt.encrypt("Hello World!")
    logging.info(temp)


def test_rsa():
    from pyencrypt.encrypt.Encrypt import Encrypt
    from pyencrypt.encrypt.RsaEncrypt import RsaEncrypt
    encrypt: Encrypt = RsaEncrypt()
    encrypt.creat_key()
    encrypt.creat_key(2048)
    public_key = '''-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDIldlK6k93+e9vrFXz79kyyhwM
Iom4qDUIQjzVQFNho6tEYtS/7hUHLx8ZEetQ28FYAUqMdMZKDC7udzKkYisrJRg9
CQS6v4aYyhPEtLBfq9eTNhUer70k8Ek4CRtrX3hqN0AkKxBh5wnvtmKVFRquqclF
by8JoVbbGnegI+RA5QIDAQAB
-----END PUBLIC KEY-----'''
    private_key = '''-----BEGIN RSA PRIVATE KEY-----
MIICXQIBAAKBgQDIldlK6k93+e9vrFXz79kyyhwMIom4qDUIQjzVQFNho6tEYtS/
7hUHLx8ZEetQ28FYAUqMdMZKDC7udzKkYisrJRg9CQS6v4aYyhPEtLBfq9eTNhUe
r70k8Ek4CRtrX3hqN0AkKxBh5wnvtmKVFRquqclFby8JoVbbGnegI+RA5QIDAQAB
AoGAK/ObxpzTd3JSWwmr1tT8JnMfVLBftZDT+ACNlFuxOZCTp1sxi3G3dVjHq2Zg
Bdp1QduckmzHAzQqt3FybQ8eroT1SuYlfdu88eK+YteE96Bu0zHlLv+ZNSjYDuBa
TEZCxTazRBAsb7OhOCO/bhkrg2Ag6QrfyD5/mH1PLND9VlkCQQDgjDSTC6SqNVzc
E1Y3ppzT5r1E/vU9Y+QOxpF4waitD4y5exZLZ+6WN05/EWb066KNfZ+NHiWF6p8F
oTq3GSbpAkEA5K5n8XnRvm6df3XqFIWbZzC9HR3vtX2FtcEsxFuV5YqEv8LbVdHb
GUsJjtr0T56RUxqbevwLc2NyOmVhOCXEnQJBAKgs2gN3qPBB3zaE1QIBK1wZaJAQ
VCSSd/AJEFLc2DQlfUQ9x8jaInsnGQdaRT4SbUCDYcgTWA8gVdGlm5AeqmECQBtW
ynBxCuVEXint0+VOL8z/Y6yGdrDw57pZ9Nsow9vkWoh+aDBzXUlB0ku0235lS6Ru
yuXCGjBaVD6s/hlzUnUCQQCX16j6qZDGE62pNtjJ4D2VDi3YgHRuvDAjfqTdxWQB
Zs88n1EGDrKxSDiagbJHHdYgGNzSA9PlVx7/Z+z2VaUV
-----END RSA PRIVATE KEY-----
    '''
    encrypt.key(public_key)
    temp = encrypt.encrypt('Hello World!')
    logging.info(temp)
    encrypt.key(private_key)
    logging.info(encrypt.decrypt(temp))
