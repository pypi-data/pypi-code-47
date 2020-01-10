import time
import logging


class pavisSnowflake:
    def __init__(self, worker_id, data_center_id):
        self.log = logging.getLogger(__name__)

        self.twepoch = 1142974214000

        self.worker_id_bits = 5
        self.data_center_id_bits = 5
        self.max_worker_id = -1 ^ (-1 << self.worker_id_bits)
        self.max_data_center_id = -1 ^ (-1 << self.data_center_id_bits)
        self.sequence_bits = 12
        self.worker_id_shift = self.sequence_bits
        self.data_center_id_shift = self.sequence_bits + self.worker_id_bits
        self.timestamp_left_shift = self.sequence_bits + \
            self.worker_id_bits + self.data_center_id_bits
        self.sequence_mask = -1 ^ (-1 << self.sequence_bits)

        self._snowflakeGenerator = self._generator(1, 1)

    def snowflake_to_timestamp(self, _id):
        _id = _id >> 22
        _id += self.twepoch
        _id = _id / 1000
        return _id

    def _generator(self, worker_id, data_center_id, sleep=lambda x: time.sleep(x/1000.0)):
        assert worker_id >= 0 and worker_id <= self.max_worker_id
        assert data_center_id >= 0 and data_center_id <= self.max_data_center_id

        last_timestamp = -1
        sequence = 0

        while True:
            timestamp = int(time.time()*1000)

            if last_timestamp > timestamp:
                log.warning(
                    "clock is moving backwards. waiting until %i" % last_timestamp)
                sleep(last_timestamp-timestamp)
                continue

            if last_timestamp == timestamp:
                sequence = (sequence + 1) & self.sequence_mask
                if sequence == 0:
                    log.warning("sequence overrun")
                    sequence = -1 & self.sequence_mask
                    sleep(1)
                    continue
            else:
                sequence = 0

            last_timestamp = timestamp

            yield (
                ((timestamp-self.twepoch) << self.timestamp_left_shift) |
                (data_center_id << self.data_center_id_shift) |
                (worker_id << self.worker_id_shift) |
                sequence)

    def next(self):
        return next(self._snowflakeGenerator)
