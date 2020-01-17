"""
@file: SnowFlakeCreator.py
@time: 2020/1/16 12:01
@description: Generating ID based on snowflake algorithm。
"""
import time

from pyencrypt.ids.IdsCreator import IdsCreator


class SnowFlakeCreator(IdsCreator):
    twepoch = 1288834974657
    datacenter_id_bits = 5
    worker_id_bits = 5
    sequence_id_bits = 12
    max_datacenter_id = 1 << datacenter_id_bits
    max_worker_id = 1 << worker_id_bits
    max_sequence_id = 1 << sequence_id_bits
    max_timestamp = 1 << (64 - datacenter_id_bits - worker_id_bits - sequence_id_bits)
    DATACENTER_ID = 1
    WORKER_ID = 1
    SEQUENCE_ID = 1

    def set_worker(self, worker_id: int):
        """
        :param worker_id:  Set the work_id, you can be any number.
        """
        self.WORKER_ID = worker_id

    def set_datacenter(self, datacenter_id: int):
        """
        :param datacenter_id:  Set the datacenter_id, you can be any number.
        """
        self.DATACENTER_ID = datacenter_id

    def set_sequence(self, sequence_id: int):
        """
        :param sequence_id:  Set the sequence_id, you can be any number.
        """
        self.SEQUENCE_ID = sequence_id

    def creat(self) -> str:
        return str(self.make_snowflake())

    def make_snowflake(self, timestamp_ms=time.time() * 1000, twepoch=twepoch):
        """
        generate a twitter-snowflake id, based on
        https://github.com/twitter/snowflake/blob/master/src/main/scala/com/twitter/service/snowflake/IdWorker.scala
        :param: timestamp_ms time since UNIX epoch in milliseconds
        """
        sid = ((int(
            timestamp_ms) - twepoch) % self.max_timestamp) << self.datacenter_id_bits << self.worker_id_bits << self.sequence_id_bits
        sid += (self.DATACENTER_ID % self.max_datacenter_id) << self.worker_id_bits << self.sequence_id_bits
        sid += (self.WORKER_ID % self.max_worker_id) << self.sequence_id_bits
        sid += self.SEQUENCE_ID % self.max_sequence_id

        return sid
