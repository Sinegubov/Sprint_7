import requests
import allure
import pytest
from helpers.register_new_courier import CourierGenerator
from helpers.data import URL


@allure.feature('Проверка логина в систему курьера')
class TestCourierLogin:
    @allure.title('Проверяем, что курьер может авторизоваться, код возврата 200 и в ответе не пустой id')
    def test_courier_login(self, url_create=URL.COURIER_URL,
                           url_login=URL.COURIER_LOGIN_URL,
                           payload=CourierGenerator.generate_courier_payload()):
        data = {
            "login": payload["login"],
            "password": payload["password"]
        }
        requests.post(url_create, data=data)
        response_login = requests.post(url_login, data=data)
        assert response_login.status_code == 200
        assert response_login.json()["id"] != ""

    @allure.title('Проверяем, если авторизоваться под несуществующим пользователем, запрос возвращает ошибку и код 404')
    def test_courier_not_valid_login(self, url=URL.COURIER_LOGIN_URL,
                                     payload=CourierGenerator.generate_courier_payload()):
        data = {
            "login": payload["login"],
            "password": payload["password"]
        }
        response_login = requests.post(url, data=data)
        assert response_login.status_code == 404
        assert response_login.json()["message"] == "Учетная запись не найдена"

    @pytest.mark.parametrize("payload",
                             [
                                 {"login": "", "password": CourierGenerator.generate_courier_payload()["password"]},
                                 {"login": CourierGenerator.generate_courier_payload()["login"], "password": ""}
                             ])
    @allure.title('Проверяем, если какого-то поля нет, запрос возвращает ошибку и код 400')
    def test_courier_incorrect_payload(self, payload):
        response_login = requests.post(URL.COURIER_LOGIN_URL, data=payload)
        assert response_login.status_code == 400
        assert response_login.json()["message"] == "Недостаточно данных для входа"
