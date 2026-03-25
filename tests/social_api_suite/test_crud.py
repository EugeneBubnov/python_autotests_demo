from datetime import datetime

import allure
import jsonpath
import pytest


@allure.epic("Social api")
@allure.feature("CRUD")
@allure.title("Проверить жизненный цикл пользователя по api")
@pytest.mark.api
def test_crud_demo(auth_service, user_service, user):
    with allure.step("Зарегистрироваться под ролью: Новый пользователь"):
        reg_response = auth_service.register(
            login=user.username, password=user.password
        )
        register_json = reg_response.json()

        assert reg_response.status_code == 201
        assert register_json.get("username") == user.username, (
            f"Expected username: {user.username}, but: {register_json.get('username')}"
        )
        assert register_json.get("password") is not None, (
            "Expected is not None password"
        )
    with allure.step("Получить информацию о пользователе"):
        # Получить уникальный Id пользователя
        all_users = user_service.get_all_users_as_list().json()
        current_user = jsonpath.findall(
            f"$[?@.username == '{user.username}']", all_users
        )[0]

        assert current_user.get("id") is not None, "Expected id is not None"
        user.unique_id = current_user.get("id")

        current_user_expected_fields = {
            "username": user.username,
            "email": "",
            "first_name": "",
            "last_name": "",
        }
        for key, value in current_user_expected_fields.items():
            assert current_user.get(key) == value, (
                f"Expected {key}: {value}, but: {current_user.get(key)}"
            )
        # Проверить информацию в профиле
        user_profile_response = user_service.get_user_profile(user)
        user_profile_json = user_profile_response.json()

        today_date = datetime.now().strftime("%Y-%m-%d")
        expected_profile_info = {
            "id": user.unique_id,
            "email": "",
            "first_name": "",
            "last_name": "",
            "date_joined": today_date,
            "birth_date": None,
            "city": "",
            "country": "",
            "family_status": "q",
            "gender": "N",
        }

        assert user_profile_response.status_code == 200
        for key, value in expected_profile_info.items():
            if key == "date_joined":
                assert str(value) in user_profile_json.get(key), (
                    f"Expected {key} in date: {value}, but: {user_profile_json.get(key)}"
                )
            else:
                assert value == user_profile_json.get(key), (
                    f"Expected {key}: {value}, but: {user_profile_json.get(key)}"
                )
    with allure.step("Изменить пароль и обновить информацию в профиле пользователя"):
        # Изменить пароль
        old_password = user.password
        new_password = f"new_{user.password}"

        change_pass_response = user_service.change_user_password(user, new_password)
        change_pass_json = change_pass_response.json()

        assert change_pass_response.status_code == 200
        expected_password_info = {
            "old_password": old_password,
            "new_password1": new_password,
            "new_password2": new_password,
        }
        for key, value in expected_password_info.items():
            assert value == change_pass_json.get(key), (
                f"Expected {key}: {value}, but: {key}: {change_pass_json.get(key)}"
            )
        user.password = new_password

        # Обновить информацию в профиле
        new_info = {
            "username": "newEug",
            "first_name": "newEugene",
            "last_name": "newBub",
            "email": "newnew@invalidggmail.comscv",
            "city": "Ottawa",
            "country": "Canada",
            "family_status": "a",
            "gender": "M",
            "birth_date": "2012-08-24",
        }

        update_profile_response = user_service.update_user_profile(
            user, updating_dict=new_info
        )
        update_profile_json = update_profile_response.json()

        assert update_profile_response.status_code == 200
        for key, value in new_info.items():
            assert value == update_profile_json.get(key), (
                f"Expected {key}: {value}, but: {key}: {update_profile_json.get(key)}"
            )

        user.update_user(**new_info)
    with allure.step("Удалить пользователя"):
        delete_response = user_service.delete_user(user)
        assert delete_response.status_code == 204

        # Убедиться, что пользователь удалён успешно
        all_users = user_service.get_all_users_as_list().json()
        all_users_list = jsonpath.findall("$.*.username", all_users)
        print(all_users_list)
        assert user.username not in all_users_list
