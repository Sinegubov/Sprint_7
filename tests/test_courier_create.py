import requests
import allure
import pytest
from helpers.register_new_courier import CourierGenerator
from data import URL, Messages


@allure.feature('Проверка регистрации курьера')
class TestCourierCreate:
    @allure.title('Проверяем, что при успешном создании курьера возвращается код 201 и статус "ok":true')
    def test_courier_create(self, url=URL.COURIER_URL, payload=CourierGenerator.generate_courier_payload()):
        response = requests.post(url, data=payload)
        assert response.status_code == 201
        assert response.text == '{"ok":true}'

    @allure.title('Проверяем, что нельзя создать двух одинаковых курьеров')
    def test_courier_create_two_same_negative(self, url=URL.COURIER_URL,
                                              payload=CourierGenerator.generate_courier_payload()):
        response = requests.post(url, data=payload)
        assert response.status_code == 201
        response_twice = requests.post(url, data=payload)
        assert response_twice.status_code == 409
        assert response_twice.json()["message"] == Messages.CREATE_TWICE

    @pytest.mark.parametrize("payload",
                             [
                                 {"login": "", "password": "123", "firstName": "Ivan"},
                                 {"login": "bar", "password": "", "firstName": "Petr"},
                                 {"login": "", "password": "", "firstName": "Oleg"},
                                 {"login": "", "password": "321", "firstName": ""},
                                 {"login": "foobar", "password": "", "firstName": ""}
                             ])
    @allure.title('Проверка, что без обязательных данных (логин, пароль) курьер не создается')
    def test_courier_create_bad_payload_negative(self, payload):
        response = requests.post(URL.COURIER_URL, data=payload)
        assert response.status_code == 400
        assert response.json()["message"] == Messages.CREATE_BAD_PAYLOAD
