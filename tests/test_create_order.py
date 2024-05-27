import requests
import allure
import pytest
from helpers.register_new_courier import CourierGenerator
from helpers.data import URL


@allure.feature('Проверка регистрации курьера')
class TestCourierCreate:
    def test_courier_create(self, url=URL.COURIER_URL, payload=CourierGenerator.generate_courier_payload()):
        response = requests.post(url, data=payload)
        assert response.status_code == 201
        assert response.text == '{"ok":true}'