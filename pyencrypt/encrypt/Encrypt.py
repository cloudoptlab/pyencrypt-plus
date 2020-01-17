"""
@file: Encrypt.py
@time: 2020/1/16 11:50
@description: Interface for encrypt.
"""
import abc


class Encrypt(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def encrypt(self, value: str) -> str:
        pass

    @abc.abstractmethod
    def decrypt(self, value: str) -> str:
        pass

    @abc.abstractmethod
    def key(self, value: str):
        pass
