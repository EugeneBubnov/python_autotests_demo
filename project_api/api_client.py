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
        # self.session.headers.update({"Accept": "application/json"}) не везде используется
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
        log_msg = f"request has be sent: GET {url}"

        if "headers" in kwargs and kwargs["headers"]:
            log_msg += f"\nheaders : {json.dumps(kwargs['headers'], indent=2)}"

        if "params" in kwargs and kwargs["params"]:
            log_msg += f"\nparams : {json.dumps(kwargs['params'], indent=2)}"

        response = self.session.get(url, **kwargs)

        log_msg += f"\nstatus code: {response.status_code}"

        try:
            self.response_data = response.json()
            log_msg += f"\nresponse:\n{json.dumps(self.response_data, indent=2, ensure_ascii=False)}\n"
        except json.JSONDecodeError:
            if response.text:
                self.response_text = response.text
                log_msg += f"\nresponse-text: {self.response_text[:1000]}\n"
            else:
                log_msg += "\nresponse: Пришёл пустой ответ"

        logger.info(log_msg)

        return response

    def post(self, path: str, **kwargs):
        url = self._build_url(path)
        return self.session.post(url, **kwargs)

    def put(self, path: str, **kwargs):
        url = self._build_url(path)
        return self.session.put(url, **kwargs)

    def patch(self, path: str, **kwargs):
        url = self._build_url(path)
        return self.session.patch(url, **kwargs)

    def delete(self, path: str, **kwargs):
        url = self._build_url(path)
        return self.session.delete(url, **kwargs)
