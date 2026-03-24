import allure
from requests import Response

from models.user import User
from project_api.api_client import ApiClient


class UserService:
    def __init__(self, client: ApiClient):
        self.client = client

    def all(self) -> Response:
        with allure.step("Получить список всех пользователей"):
            return self.client.get(
                "/user/all", headers={"Content-Type": "application/json"}
            )

    def delete(self, user: User) -> Response:
        with allure.step("Удалить пользователя"):
            return self.client.delete(
                "/user/delete", headers={"Authorization": f"Basic {user.basic_token}"}
            )
