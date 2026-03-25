from typing import Dict

import allure
from requests import Response

from models.user import User
from project_api.api_client import ApiClient


class UserService:
    def __init__(self, client: ApiClient):
        self.client = client

    def get_all_users_as_list(self) -> Response:
        with allure.step(
            "Получить список всех пользователей. Отправить запрос: [GET] /api/user/all"
        ):
            return self.client.get(
                endpoint="/api/user/all", headers={"Content-Type": "application/json"}
            )

    def get_user_profile(self, user: User) -> Response:
        with allure.step(
            "Получить информацию из профиля пользователя."
            f"Отправить запрос: [GET] /api/user/{user.unique_id}"
        ):
            return self.client.get(
                endpoint=f"/api/user/{user.unique_id}",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Basic {user.basic_token}",
                },
            )

    def change_user_password(self, user: User, new_password: str) -> Response:
        with allure.step(
            "Обновить пароль пользователя. Отправить запрос: [PUT] /api/user/password"
        ):
            return self.client.put(
                endpoint="/api/user/password",
                headers={"Authorization": f"Basic {user.basic_token}"},
                json={
                    "old_password": user.password,
                    "new_password1": new_password,
                    "new_password2": new_password,
                },
            )

    def update_user_profile(
        self, user: User, updating_dict: Dict[str, str]
    ) -> Response:
        with allure.step(
            "Обновить профиль пользователя. "
            f"Отправить запрос: [PATCH] /api/user/update/profile/{user.unique_id if user.unique_id else 'None set value'}"
        ):
            return self.client.patch(
                endpoint=f"/api/user/update/profile/{user.unique_id}",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Basic {user.basic_token}",
                },
                json=updating_dict,
            )

    def delete_user(self, user: User) -> Response:
        with allure.step(
            "Удалить пользователя. Отправить запрос: [DELETE] /api/user/delete"
        ):
            return self.client.delete(
                endpoint="/api/user/delete",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Basic {user.basic_token}",
                },
            )
