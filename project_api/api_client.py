import json as json_lib
import logging
from typing import Any, Dict, Optional

import requests
from requests import Response

logging.basicConfig(
    level=logging.INFO,
    format=f"\n{'=' * 60}\n[%(asctime)s | %(levelname)s]: %(message)s",
)
logger = logging.getLogger(__name__)


class ApiClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()

        self.response_data = None
        self.response_text = None
        self.status = None

    def _build_url(self, path: str) -> str:
        base = self.base_url.rstrip("/")
        path = path.lstrip("/")
        return f"{base}/{path}"

    def get(
        self,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        **kwargs,
    ) -> Response:
        url = self._build_url(endpoint)
        log_msg = f"Request sent.\n[GET]: {url}"

        if headers:
            log_msg += f"\n[HEADERS]: {json_lib.dumps(headers, indent=2)}"

        if params:
            log_msg += f"\n[PARAMS]: {json_lib.dumps(params, indent=2)}"

        response = self.session.get(url=url, params=params, headers=headers, **kwargs)

        if response.status_code >= 400:
            logger.error(f"[{url}|STATUS CODE]: {response.status_code}")
        else:
            log_msg += f"\n[STATUS CODE]: {response.status_code}"

        try:
            self.response_data = response.json()
            log_msg += f"\n[RESPONSE]:\n{json_lib.dumps(self.response_data, indent=2, ensure_ascii=False)}"
        except json_lib.JSONDecodeError:
            if response.text:
                self.response_text = response.text
                log_msg += f"\n[RESPONSE-TEXT]: {self.response_text[:1000]}"
            else:
                log_msg += "\n[RESPONSE]: empty response-body"

        logger.info(f"{log_msg}")

        return response

    def post(
        self,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        json: Optional[Dict[str, Any]] = None,
        data: Optional[Any] = None,
        **kwargs,
    ) -> Response:
        url = self._build_url(endpoint)

        log_msg = f"Request sent.\n[POST]: {url}"

        if headers:
            log_msg += f"\n[HEADERS]: {json_lib.dumps(headers, indent=2)}"

        if params:
            log_msg += f"\n[PARAMS]: {json_lib.dumps(params, indent=2)}"

        if json:
            log_msg += (
                f"\n[JSON]:\n{json_lib.dumps(json, indent=2, ensure_ascii=False)}"
            )
        elif data:
            log_msg += f"\n[DATA]: {data}"

        if "files" in kwargs and kwargs["files"]:
            log_msg += f"\n[FILES]: {list(kwargs['files'].keys())}"

        response = self.session.post(
            url, params=params, headers=headers, data=data, json=json, **kwargs
        )

        if response.status_code >= 400:
            logger.error(f"[{url}|STATUS CODE]: {response.status_code}")
        else:
            log_msg += f"\n[STATUS CODE]: {response.status_code}"

        try:
            self.response_data = response.json()
            log_msg += f"\n[RESPONSE]:\n{json_lib.dumps(self.response_data, indent=2, ensure_ascii=False)}"
        except json_lib.JSONDecodeError:
            if response.text:
                self.response_text = response.text
                log_msg += f"\n[RESPONSE-TEXT]: {self.response_text[:1000]}"
            else:
                log_msg += "\n[RESPONSE]: empty response-body"

        logger.info(f"{log_msg}")

        return response

    def put(
        self,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        json: Optional[Dict[str, Any]] = None,
        data: Optional[Any] = None,
        **kwargs,
    ) -> Response:
        url = self._build_url(endpoint)

        log_msg = f"Request sent.\n[PUT]: {url}"

        if headers:
            log_msg += f"\n[HEADERS]: {json_lib.dumps(headers, indent=2)}"

        if params:
            log_msg += f"\n[PARAMS]: {json_lib.dumps(params, indent=2)}"

        if json:
            log_msg += (
                f"\n[JSON]:\n{json_lib.dumps(json, indent=2, ensure_ascii=False)}"
            )
        elif data:
            log_msg += f"\n[DATA]: {data}"

        if "files" in kwargs and kwargs["files"]:
            log_msg += f"\n[FILES]: {list(kwargs['files'].keys())}"

        response = self.session.put(
            url, params=params, headers=headers, data=data, json=json, **kwargs
        )

        if response.status_code >= 400:
            logger.error(f"[{url}|STATUS CODE]: {response.status_code}")
        else:
            log_msg += f"\n[STATUS CODE]: {response.status_code}"

        try:
            self.response_data = response.json()
            log_msg += f"\n[RESPONSE]:\n{json_lib.dumps(self.response_data, indent=2, ensure_ascii=False)}"
        except json_lib.JSONDecodeError:
            if response.text:
                self.response_text = response.text
                log_msg += f"\n[RESPONSE-TEXT]: {self.response_text[:1000]}"
            else:
                log_msg += "\n[RESPONSE]: empty response-body"

        logger.info(f"{log_msg}")

        return response

    def patch(
        self,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        json: Optional[Dict[str, Any]] = None,
        data: Optional[Any] = None,
        **kwargs,
    ) -> Response:
        url = self._build_url(endpoint)

        log_msg = f"Request sent.\n[PATCH]: {url}"

        if headers:
            log_msg += f"\n[HEADERS]: {json_lib.dumps(headers, indent=2)}"

        if params:
            log_msg += f"\n[PARAMS]: {json_lib.dumps(params, indent=2)}"

        if json:
            log_msg += (
                f"\n[JSON]:\n{json_lib.dumps(json, indent=2, ensure_ascii=False)}"
            )
        elif data:
            log_msg += f"\n[DATA]: {data}"

        if "files" in kwargs and kwargs["files"]:
            log_msg += f"\n[FILES]: {list(kwargs['files'].keys())}"

        response = self.session.patch(
            url, params=params, headers=headers, data=data, json=json, **kwargs
        )

        if response.status_code >= 400:
            logger.error(f"[{url}] | STATUS CODE]: {response.status_code}")
        else:
            log_msg += f"\n[STATUS CODE]: {response.status_code}"

        try:
            self.response_data = response.json()
            log_msg += f"\n[RESPONSE]:\n{json_lib.dumps(self.response_data, indent=2, ensure_ascii=False)}"
        except json_lib.JSONDecodeError:
            if response.text:
                self.response_text = response.text
                log_msg += f"\n[RESPONSE-TEXT]: {self.response_text[:1000]}"
            else:
                log_msg += "\n[RESPONSE]: empty response-body"

        logger.info(f"{log_msg}")

        return response

    def delete(
        self,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        **kwargs,
    ) -> Response:
        url = self._build_url(endpoint)
        log_msg = f"Request sent.\n[DELETE]: {url}"

        if headers:
            log_msg += f"\n[HEADERS]: {json_lib.dumps(headers, indent=2)}"

        if params:
            log_msg += f"\n[PARAMS]: {json_lib.dumps(params, indent=2)}"

        response = self.session.delete(url, params=params, headers=headers, **kwargs)

        if response.status_code >= 400:
            logger.error(f"{url}\n[STATUS CODE]: {response.status_code}")
        else:
            log_msg += f"\n[STATUS CODE]: {response.status_code}"

        try:
            self.response_data = response.json()
            log_msg += f"\n[RESPONSE]:\n{json_lib.dumps(self.response_data, indent=2, ensure_ascii=False)}"
        except json_lib.JSONDecodeError:
            if response.text:
                self.response_text = response.text
                log_msg += f"\n[RESPONSE-TEXT]: {self.response_text[:1000]}"
            else:
                log_msg += "\n[RESPONSE]: empty response-body"

        logger.info(f"{log_msg}")

        return response
