import logging
import time

class LoggerConfig:
    @staticmethod
    def setup_logger():
        logging.basicConfig(
            format="%(asctime)s -%(levelname)s - %(message)s", level=logging.INFO
        )

class UTCTime:
    @staticmethod
    def get_utc_epoch(minutes_from_now):
        return int(time.time()) + (minutes_from_now * 60)