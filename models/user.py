import base64
from dataclasses import dataclass
from typing import Optional

from faker import Faker


@dataclass
class User:
    username: str
    password: str
    token: Optional[str] = None

    @classmethod
    def create_random_user(cls):
        faker = Faker(locale="ru-RU")
        return cls(username=faker.user_name(), password=faker.password())

    @property
    def basic_token(self):
        data = f"{self.username}:{self.password}"
        data_bytes = data.encode("utf-8")
        return base64.b64encode(data_bytes).decode("utf-8")
