import requests
import allure
import pytest
import json
from helpers.register_new_courier import CourierGenerator
from helpers.data import URL


@allure.feature('Проверка удаления курьера')
class TestCourierCreate:
    @allure.title('Проверяем, что курьер может авторизоваться, код возврата 200 и в ответе не пустой id')
    def test_courier_delete(self, payload=CourierGenerator.generate_courier_payload()):
        data = {
            "login": payload["login"],
            "password": payload["password"]
        }
        requests.post(URL.COURIER_URL, data=data)
        response_id = requests.post(URL.COURIER_LOGIN_URL, data=data).json()["id"]
        response = requests.delete(f"{URL.COURIER_URL}/{response_id}")
        assert response.status_code == 200
        assert response.text == '{"ok":true}'

    @allure.title('Проверяем, запрос с несуществующим id')
    def test_delete_courier_with_bad_id(self, courier_id=CourierGenerator.bad_courier_id()):
        response = requests.delete(f"{URL.COURIER_URL}/{courier_id}")
        assert response.status_code == 404
        assert response.json()["message"] == "Курьера с таким id нет."

    @allure.title('Проверяем, запрос без id')
    def test_delete_courier_without_id(self):
        response = requests.delete(f"{URL.COURIER_URL}")
        assert response.status_code == 404
        assert response.json()["message"] == "Not Found."
