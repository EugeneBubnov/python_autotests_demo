import pytest

from models.user import User
from project_api.api_client import ApiClient
from project_api.config import Config
from project_api.social_api.auth_service import AuthService
from project_api.social_api.user_service import UserService


@pytest.fixture
def auth_service():
    api_client = ApiClient(base_url=Config.SOCIAL_API_URL)
    service = AuthService(api_client)
    yield service
    api_client.session.close()


@pytest.fixture
def user_service():
    api_client = ApiClient(base_url=Config.SOCIAL_API_URL)
    service = UserService(api_client)
    yield service
    api_client.session.close()


@pytest.fixture
def user():
    return User.create_random_user()
