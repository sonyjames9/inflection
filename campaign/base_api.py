import requests
import logging
from utils.config import LoggerConfig

LoggerConfig.setup_logger()
logger = logging.getLogger(__name__)


class BaseAPI:
    def __init__(self, base_url) -> None:
        self.base_url = base_url
        self.session = requests.Session()

    def get(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"GET {url}")
        response = self.session.get(url)
        self._log_response(response)
        return response.json(), response.status_code

    def post(self, endpoint, data):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"POST {url} - Payload: {data}")
        response =  self.session.post(url, json=data)
        return response.json(), response.status_code

    def patch(self, endpoint, data):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"PATCH {url} - Payload: {data}")
        response =  self.session.patch(url, json=data)
        self._log_response(response)
        return response.json(), response.status_code

    def _log_response(self, response):
        logger.info(f"Response Code: {response.status_code}")
        logger.info(f"Response Body: {response.text}")
