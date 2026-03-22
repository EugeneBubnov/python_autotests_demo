import pytest

from project_api.api_client import ApiClient
from project_api.config import Config


@pytest.fixture
def social_api_client():
    return ApiClient(base_url=Config.SOCIAL_API_URL)
