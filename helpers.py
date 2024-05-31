from faker import Faker
import allure
import requests
from data import URL


fake = Faker()


class CourierGenerator:

    @staticmethod
    def generate_data():
        login = fake.text(max_nb_chars=12)
        password = fake.password(length=6, special_chars=False, digits=True, upper_case=True, lower_case=True)
        firstname = fake.name()
        return login, password, firstname

    @staticmethod
    def generate_courier_payload():
        login, password, firstname = CourierGenerator.generate_data()
        payload = {
            "login": login,
            "password": password,
            "firstName": firstname
        }
        return payload

    @staticmethod
    @allure.step('Генерация случайного id')
    def random_string_id():
        return str(fake.random_int(min=100000, max=10000000))

    @allure.step('Создаем курьера и получаем логин, пароль и имя')
    def register_new_courier_and_return_login_password(self):
        payload = self.generate_courier_payload()
        data = {
            "login": payload["login"],
            "password": payload["password"]
        }
        requests.post(URL.COURIER_URL, data=data)
        return data

    @allure.step('Удаляем курьера')
    def delete_courier(self, login, password):
        response_post = requests.post(URL.COURIER_LOGIN_URL, data={
            "login": login,
            "password": password,
        })
        courier_id = response_post.json()['id']
        requests.delete(f'{URL.COURIER_DELETE_URL}/{courier_id}')
