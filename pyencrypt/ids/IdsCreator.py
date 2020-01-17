"""
@file: IdsCreatorInterface.py
@time: 2020/1/16 11:50
@description: Interface for creating random, non repeating IDS.
"""
import abc


class IdsCreator(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def set_worker(self, worker_id):
        pass

    @abc.abstractmethod
    def set_datacenter(self, datacenter_id):
        pass

    @abc.abstractmethod
    def set_sequence(self, sequence_id):
        pass

    @abc.abstractmethod
    def creat(self) -> str:
        pass
