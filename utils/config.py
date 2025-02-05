import logging
import time
import random
import string
import uuid
import os


class LoggerConfig:
    @staticmethod
    def setup_logger():
        logging.basicConfig(
            format="%(asctime)s -%(levelname)s - %(message)s", level=logging.INFO
        )

class UTCTime:
    @staticmethod
    def get_utc_epoch(minutes_from_now: int = 10):
        return int(time.time()) + (minutes_from_now)

class NameGenerator:
    @staticmethod
    def generate_campaign_name():
        """Generates a random campaign name using UUID"""
        return f"Campaign_{uuid.uuid4().hex[:6]}"  # Example: Campaign_A1B2C3

    @staticmethod
    def generate_campaign_name_short():
        """Generates a short random campaign name with numbers"""
        return f"Campaign_{random.randint(1000, 9999)}"  # Example: Campaign_4523

    @staticmethod
    def generate_campaign_name_custom(prefix="Test"):
        """Generates a campaign name with a custom prefix"""
        random_part = "".join(
            random.choices(string.ascii_uppercase + string.digits, k=5)
        )
        return f"{prefix}_{random_part}"  # Example: Test_XYZ12



class AppConfig:

    BASE_URL = os.getenv(
        "API_BASE_URL", "http://localhost:7070"
    )  
    @staticmethod
    def get_base_url():
        return AppConfig.BASE_URL
