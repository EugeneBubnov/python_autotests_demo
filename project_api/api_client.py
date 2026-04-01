import json as json_lib
import logging
import os
import sys
from typing import Any, Dict, Optional

import requests
from requests import Response

# Полностью очищаем все существующие настройки логирования
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

# Создаем свой логгер
logger = logging.getLogger(__name__)

# Создаем handler с простым текстовым выводом (без цветов)
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(
    logging.Formatter(
        fmt="[%(asctime)s | %(levelname)s]: %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )
)

# Добавляем handler только к нашему логгеру
logger.addHandler(handler)
logger.setLevel(logging.INFO)

# Отключаем propagation (чтобы логи не шли в корневой логгер)
logger.propagate = False

# Отключаем ANSI цвета в выводе
os.environ["PYTEST_ADDOPTS"] = "--color=no"
os.environ["FORCE_COLOR"] = "0"
os.environ["NO_COLOR"] = "1"

# Отключаем логи от библиотек
logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("pytest").setLevel(logging.CRITICAL)


class ApiClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()

        self.response_data = None
        self.response_text = None

    def _build_url(self, path: str) -> str:
        base = self.base_url.rstrip("/")
        path = path.lstrip("/")
        return f"{base}/{path}"

    def _format_json(self, data: Any) -> str:
        return json_lib.dumps(data, indent=2, ensure_ascii=False)

    def _log_request(
        self,
        method: str,
        url: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        json: Optional[Dict[str, Any]] = None,
        data: Optional[Any] = None,
        **kwargs,
    ):
        log_msg = f"\n[{method}]: Request sent: {url}"

        if headers:
            log_msg += f"\n[HEADERS]: {self._format_json(headers)}"

        if params:
            log_msg += f"\n[PARAMS]: {self._format_json(params)}"

        if json:
            log_msg += f"\n[JSON]:\n{self._format_json(json)}"
        elif data:
            log_msg += f"\n[DATA]: {data}"

        if "files" in kwargs and kwargs["files"]:
            log_msg += f"\n[FILES]: {list(kwargs['files'].keys())}"

        return log_msg

    def _log_response(self, response: Response) -> str:
        log_msg = f"\n[STATUS CODE]: {response.status_code}"

        try:
            data = response.json()
            self.response_data = data
            log_msg += f"\n[RESPONSE]:\n{self._format_json(data)}"
        except json_lib.JSONDecodeError:
            text = response.text
            self.response_text = text

            if text:
                log_msg += f"\n[RESPONSE-TEXT]: {text[:1000]}"
            else:
                log_msg += "\n[RESPONSE]: empty"

        return log_msg

    def _request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        json: Optional[Dict[str, Any]] = None,
        data: Optional[Any] = None,
        **kwargs,
    ) -> Response:
        url = self._build_url(endpoint)

        request_logs = self._log_request(
            method=method,
            url=url,
            params=params,
            headers=headers,
            json=json,
            data=data,
            **kwargs,
        )

        response = self.session.request(
            method=method,
            url=url,
            params=params,
            headers=headers,
            json=json,
            data=data,
            **kwargs,
        )

        response_logs = self._log_response(response)
        logger.info(f"{request_logs}\n{response_logs}")

        return response

    def get(
        self,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        **kwargs,
    ) -> Response:
        return self._request(
            method="GET",
            endpoint=endpoint,
            params=params,
            headers=headers,
            **kwargs,
        )

    def post(
        self,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        json: Optional[Dict[str, Any]] = None,
        data: Optional[Any] = None,
        **kwargs,
    ) -> Response:
        return self._request(
            method="POST",
            endpoint=endpoint,
            params=params,
            headers=headers,
            json=json,
            data=data,
            **kwargs,
        )

    def put(
        self,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        json: Optional[Dict[str, Any]] = None,
        data: Optional[Any] = None,
        **kwargs,
    ) -> Response:
        return self._request(
            method="PUT",
            endpoint=endpoint,
            params=params,
            headers=headers,
            json=json,
            data=data,
            **kwargs,
        )

    def patch(
        self,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        json: Optional[Dict[str, Any]] = None,
        data: Optional[Any] = None,
        **kwargs,
    ) -> Response:
        return self._request(
            method="PATCH",
            endpoint=endpoint,
            params=params,
            headers=headers,
            json=json,
            data=data,
            **kwargs,
        )

    def delete(
        self,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        **kwargs,
    ) -> Response:
        return self._request(
            method="DELETE",
            endpoint=endpoint,
            params=params,
            headers=headers,
            **kwargs,
        )
