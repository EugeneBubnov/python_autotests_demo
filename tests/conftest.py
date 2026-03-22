import pytest

from project_api.api_client import ApiClient


@pytest.fixture
def api_client():
    return ApiClient()
