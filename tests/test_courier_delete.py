import requests
import allure
import pytest
import json
from helpers.register_new_courier import CourierGenerator
from helpers.data import URL


@allure.feature('Проверка удаления курьера')
class TestCourierCreate:
    @allure.title('Проверяем, что курьер может авторизоваться, код возврата 200 и в ответе не пустой id')
    def test_courier_delete(self, url_create=URL.COURIER_URL,
                           url_login=URL.COURIER_LOGIN_URL,
                           payload=CourierGenerator.generate_courier_payload()):
        data = {
            "login": payload["login"],
            "password": payload["password"]
        }
        requests.post(url_create, data=data)
        response_id = requests.post(url_login, data=data).json()["id"]
        print(response_id)
        response_id_str = str(response_id)
        courier_id = {"id": response_id}
        print(courier_id)
        response = requests.delete(f"{url_create}:{response_id}", data=courier_id)
        print(response.text)
        assert response.status_code == 200
        assert response.text == '{"ok":true}'
