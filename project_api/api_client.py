import json
import logging

import requests
from requests import Response

logging.basicConfig(
    level=logging.INFO,
    format="\n[%(asctime)s | %(levelname)s]: %(message)s",
)
logger = logging.getLogger(__name__)


class ApiClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()

        self.response_data = None
        self.response_text = None
        self.status = None

    def set_token(self, token: str):
        self.session.headers.update({"Authorization": f"Bearer {token}"})

    def _build_url(self, path: str) -> str:
        base = self.base_url.rstrip("/")
        path = path.lstrip("/")
        return f"{base}/{path}"

    def get(self, path: str, **kwargs) -> Response:
        url = self._build_url(path)
        log_msg = f"\nREQUEST HAS BE SENT: GET {url}"

        if "headers" in kwargs and kwargs["headers"]:
            log_msg += f"\nHEADERS: {json.dumps(kwargs['headers'], indent=2)}"

        if "params" in kwargs and kwargs["params"]:
            log_msg += f"\nPARAMS: {json.dumps(kwargs['params'], indent=2)}"

        response = self.session.get(url, **kwargs)

        if response.status_code >= 400:
            logger.error(f"[{url}] STATUS CODE: {response.status_code}")
        else:
            log_msg += f"\nSTATUS CODE: {response.status_code}"

        try:
            self.response_data = response.json()
            log_msg += f"\nRESPONSE:\n{json.dumps(self.response_data, indent=2, ensure_ascii=False)}"
        except json.JSONDecodeError:
            if response.text:
                self.response_text = response.text
                log_msg += f"\nRESPONSE-TEXT: {self.response_text[:1000]}"
            else:
                log_msg += "\nRESPONSE: empty response-body"

        logger.info(log_msg)

        return response

    def post(self, path: str, **kwargs):
        url = self._build_url(path)

        log_msg = f"\nREQUEST HAS BE SENT: POST {url}"

        if "headers" in kwargs and kwargs["headers"]:
            log_msg += f"\nHEADERS: {json.dumps(kwargs['headers'], indent=2)}"

        if "params" in kwargs and kwargs["params"]:
            log_msg += f"\nPARAMS: {json.dumps(kwargs['params'], indent=2)}"

        if "json" in kwargs and kwargs["json"]:
            log_msg += (
                f"\nJSON:\n{json.dumps(kwargs['json'], indent=2, ensure_ascii=False)}"
            )
        elif "data" in kwargs and kwargs["data"]:
            log_msg += f"\nDATA: {kwargs['data']}"

        if "files" in kwargs and kwargs["files"]:
            log_msg += f"\nFILES: {list(kwargs['files'].keys())}"

        response = self.session.post(url, **kwargs)

        if response.status_code >= 400:
            logger.error(f"[{url}] STATUS CODE: {response.status_code}")
        else:
            log_msg += f"\nSTATUS CODE: {response.status_code}"

        try:
            self.response_data = response.json()
            log_msg += f"\nRESPONSE:\n{json.dumps(self.response_data, indent=2, ensure_ascii=False)}"
        except json.JSONDecodeError:
            if response.text:
                self.response_text = response.text
                log_msg += f"\nRESPONSE-TEXT: {self.response_text[:1000]}"
            else:
                log_msg += "\nRESPONSE: empty response-body"

        logger.info(log_msg)

        return response

    def put(self, path: str, **kwargs):
        url = self._build_url(path)

        log_msg = f"\nREQUEST HAS BE SENT: PUT {url}"

        if "headers" in kwargs and kwargs["headers"]:
            log_msg += f"\nHEADERS: {json.dumps(kwargs['headers'], indent=2)}"

        if "params" in kwargs and kwargs["params"]:
            log_msg += f"\nPARAMS: {json.dumps(kwargs['params'], indent=2)}"

        if "json" in kwargs and kwargs["json"]:
            log_msg += (
                f"\nJSON:\n{json.dumps(kwargs['json'], indent=2, ensure_ascii=False)}"
            )
        elif "data" in kwargs and kwargs["data"]:
            log_msg += f"\nDATA: {kwargs['data']}"

        if "files" in kwargs and kwargs["files"]:
            log_msg += f"\nFILES: {list(kwargs['files'].keys())}"

        response = self.session.put(url, **kwargs)

        if response.status_code >= 400:
            logger.error(f"[{url}] STATUS CODE: {response.status_code}")
        else:
            log_msg += f"\nSTATUS CODE: {response.status_code}"

        try:
            self.response_data = response.json()
            log_msg += f"\nRESPONSE:\n{json.dumps(self.response_data, indent=2, ensure_ascii=False)}"
        except json.JSONDecodeError:
            if response.text:
                self.response_text = response.text
                log_msg += f"\nRESPONSE-TEXT: {self.response_text[:1000]}"
            else:
                log_msg += "\nRESPONSE: empty response-body"

        logger.info(log_msg)

        return response

    def patch(self, path: str, **kwargs):
        url = self._build_url(path)

        log_msg = f"\nREQUEST HAS BE SENT: PATCH {url}"

        if "headers" in kwargs and kwargs["headers"]:
            log_msg += f"\nHEADERS: {json.dumps(kwargs['headers'], indent=2)}"

        if "params" in kwargs and kwargs["params"]:
            log_msg += f"\nPARAMS: {json.dumps(kwargs['params'], indent=2)}"

        if "json" in kwargs and kwargs["json"]:
            log_msg += (
                f"\nJSON:\n{json.dumps(kwargs['json'], indent=2, ensure_ascii=False)}"
            )
        elif "data" in kwargs and kwargs["data"]:
            log_msg += f"\nDATA: {kwargs['data']}"

        if "files" in kwargs and kwargs["files"]:
            log_msg += f"\nFILES: {list(kwargs['files'].keys())}"

        response = self.session.patch(url, **kwargs)

        if response.status_code >= 400:
            logger.error(f"[{url}] STATUS CODE: {response.status_code}")
        else:
            log_msg += f"\nSTATUS CODE: {response.status_code}"

        try:
            self.response_data = response.json()
            log_msg += f"\nRESPONSE:\n{json.dumps(self.response_data, indent=2, ensure_ascii=False)}"
        except json.JSONDecodeError:
            if response.text:
                self.response_text = response.text
                log_msg += f"\nRESPONSE-TEXT: {self.response_text[:1000]}"
            else:
                log_msg += "\nRESPONSE: empty response-body"

        logger.info(log_msg)

        return response

    def delete(self, path: str, **kwargs):
        url = self._build_url(path)
        log_msg = f"\nREQUEST HAS BE SENT: DELETE {url}"

        if "headers" in kwargs and kwargs["headers"]:
            log_msg += f"\nHEADERS: {json.dumps(kwargs['headers'], indent=2)}"

        if "params" in kwargs and kwargs["params"]:
            log_msg += f"\nPARAMS: {json.dumps(kwargs['params'], indent=2)}"

        response = self.session.delete(url, **kwargs)

        if response.status_code >= 400:
            logger.error(f"[{url}] STATUS CODE: {response.status_code}")
        else:
            log_msg += f"\nSTATUS CODE: {response.status_code}"

        try:
            self.response_data = response.json()
            log_msg += f"\nRESPONSE:\n{json.dumps(self.response_data, indent=2, ensure_ascii=False)}"
        except json.JSONDecodeError:
            if response.text:
                self.response_text = response.text
                log_msg += f"\nRESPONSE-TEXT: {self.response_text[:1000]}"
            else:
                log_msg += "\nRESPONSE: empty response-body"

        logger.info(log_msg)

        return response
