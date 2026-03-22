import requests

from project_api.config import Config


class ApiClient:
    def __init__(self, base_url: str = Config.BASE_URL):
        self.base_url = base_url
        self.session = requests.Session()

        self.session.headers.update({"Accept": "application/json"})

    def set_token(self, token: str):
        self.session.headers.update({"Authorization": f"Bearer {token}"})

    def _build_url(self, path: str) -> str:
        base = self.base_url.rstrip("/")
        path = path.lstrip("/")
        return f"{base}/{path}"

    def get(self, path: str, **kwargs):
        url = self._build_url(path)
        return self.session.get(url, **kwargs)

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
