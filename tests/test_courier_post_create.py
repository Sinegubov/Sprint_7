import requests
import allure
import pytest
from data import URL, Messages
from helpers import CourierGenerator


@allure.feature('Проверка регистрации курьера')
class TestPostCourierCreate:
    @allure.title('Проверяем, что при успешном создании курьера возвращается код 201 и статус "ok":true')
    def test_courier_create(self, url=URL.COURIER_URL):
        login, password, firstname = CourierGenerator().generate_data()
        payload = {
            "login": login,
            "password": password,
            "firstName": firstname
            }
        response = requests.post(url, data=payload)
        assert response.status_code == 201
        assert response.text == Messages.OK
        CourierGenerator().delete_courier(login, password)

    @allure.title('Проверяем, что нельзя создать двух одинаковых курьеров')
    def test_courier_create_twice(self, url=URL.COURIER_URL):
        login, password, firstname = CourierGenerator().generate_data()
        payload = {
            "login": login,
            "password": password,
            "firstName": firstname
            }
        response = requests.post(url, data=payload)
        assert response.status_code == 201
        response_twice = requests.post(url, data=payload)
        assert response_twice.status_code == 409
        assert response_twice.json()["message"] == Messages.CREATE_TWICE
        CourierGenerator().delete_courier(login, password)

    @pytest.mark.parametrize("payload",
                             [
                                 {"login": "", "password": "123", "firstName": "Ivan"},
                                 {"login": "bar", "password": "", "firstName": "Petr"},
                                 {"login": "", "password": "", "firstName": "Oleg"},
                                 {"login": "", "password": "321", "firstName": ""},
                                 {"login": "foobar", "password": "", "firstName": ""}
                             ])
    @allure.title('Проверка, что без обязательных данных (логин, пароль) курьер не создается')
    def test_courier_create_bad_payload_negative(self, payload, url=URL.COURIER_URL):
        response = requests.post(url, data=payload)
        assert response.status_code == 400
        assert response.json()["message"] == Messages.CREATE_BAD_PAYLOAD
