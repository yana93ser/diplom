from dataclasses import dataclass


@dataclass
class Users:
    email: str
    phone: str


test_user = Users(
    email='test@mail.ru',
    phone='123456789'
)
