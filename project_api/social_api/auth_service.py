import allure
from requests import Response

from project_api.api_client import ApiClient


class AuthService:
    def __init__(self, client: ApiClient):
        self.client = client

    def logout(self) -> Response:
        with allure.step("Разлогиниться. Отправить запрос: [GET] /api/auth/logout"):
            return self.client.get(
                "/api/auth/logout", headers={"Content-Type": "application/json"}
            )

    def register(self, login: str, password: str) -> Response:
        with allure.step("Зарегистрироваться. Отправить запрос: [POST] /api/auth/reg"):
            return self.client.post(
                "/api/auth/reg",
                headers={"Content-Type": "application/json"},
                json={"username": login, "password": password},
            )

    def get_auth_token(self, login: str, password: str) -> Response:
        with allure.step(
            "Получить токен авторизации. Отправить запрос: [POST] /api/auth/token"
        ):
            return self.client.post(
                "/api/auth/token",
                headers={"Content-Type": "application/json"},
                json={"username": login, "password": password},
            )
