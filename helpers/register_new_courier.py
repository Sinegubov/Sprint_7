import requests
from faker import Faker
from helpers.data import URL

fake = Faker(locale="ru_RU")


class CourierGenerator:
    @staticmethod
    def generate_courier_payload():
        login = fake.text(max_nb_chars=10)
        password = fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
        firstname = fake.name()
        payload = {"login": login, "password": password, "firstName": firstname}
        return payload
