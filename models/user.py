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
