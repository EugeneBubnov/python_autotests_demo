import base64
from dataclasses import dataclass
from typing import Optional

from faker import Faker


@dataclass
class User:
    username: str
    password: str
    first_name: str
    last_name: str
    birth_date: str
    email: str

    token: Optional[str] = None
    unique_id: Optional[str] = None

    gender: Optional[str] = None
    family_status: Optional[str] = None
    country: Optional[str] = None

    @classmethod
    def create_random_user(cls):
        faker = Faker(locale="ru-RU")
        return cls(
            username=faker.user_name(),
            password=faker.password(),
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            birth_date=str(faker.date_of_birth(minimum_age=18, maximum_age=80)),
            email=faker.free_email(),
        )

    @property
    def basic_token(self) -> str:
        data = f"{self.username}:{self.password}"
        data_bytes = data.encode("utf-8")
        return base64.b64encode(data_bytes).decode("utf-8")

    def update_user(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        return self
