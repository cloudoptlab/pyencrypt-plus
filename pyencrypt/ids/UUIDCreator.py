"""
@file: UUIDCreator.py
@time: 2020/1/16 12:01
@description: Generating ID based on python.uuid()。
"""
import uuid

from pyencrypt.ids.IdsCreator import IdsCreator


class UUIDCreator(IdsCreator):
    DATACENTER_ID = "DATACENTER"
    WORKER_ID = "WORKER"
    SEQUENCE_ID = "SEQUENCE"

    def set_worker(self, worker_id: str):
        """
        :param worker_id:  Set the work_id, you can be any string or any number.
        """
        self.WORKER_ID = str(worker_id)

    def set_datacenter(self, datacenter_id: str):
        """
        :param datacenter_id:  Set the datacenter_id, you can be any string or any number.
        """
        self.DATACENTER_ID = datacenter_id

    def set_sequence(self, sequence_id: str):
        """
        :param sequence_id:  Set the sequence_id, you can be any string or any number.
        """
        self.SEQUENCE_ID = sequence_id

    def creat(self) -> str:
        return uuid.uuid3(uuid.NAMESPACE_DNS, self.DATACENTER_ID + self.SEQUENCE_ID + self.WORKER_ID)
