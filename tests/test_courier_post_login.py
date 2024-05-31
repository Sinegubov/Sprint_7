import requests
import allure
import pytest
from data import URL, Messages
from helpers import CourierGenerator


@allure.feature('Проверка логина в систему курьера')
class TestPostCourierLogin:
    @allure.title('Проверяем, что курьер может авторизоваться, код возврата 200 и в ответе не пустой id')
    def test_courier_login(self,
                           url_create=URL.COURIER_URL,
                           url=URL.COURIER_LOGIN_URL):
        payload = CourierGenerator().register_new_courier_and_return_login_password()
        requests.post(url_create, data=payload)
        response = requests.post(url, data=payload)
        assert response.status_code == 200
        assert response.json()["id"] != ""
        CourierGenerator().delete_courier(payload["login"], payload["password"])

    @allure.title('Авторизация несуществующим пользователе возвращает ошибку и код 404')
    def test_courier_not_valid_login_negative(self, url=URL.COURIER_LOGIN_URL):
        login, password, firstname = CourierGenerator().generate_data()
        payload = {
            "login": login,
            "password": password
        }
        response = requests.post(url, data=payload)
        assert response.status_code == 404
        assert response.json()["message"] == Messages.LOGIN_INVALID_404

    @pytest.mark.parametrize("payload",
                             [
                                 {"login": "", "password": "123"},
                                 {"login": "anonim", "password": ""}
                             ])
    @allure.title('Проверяем, если какого-то поля нет, запрос возвращает ошибку и код 400')
    def test_courier_incorrect_payload_negative(self, payload):
        response = requests.post(URL.COURIER_LOGIN_URL, data=payload)
        assert response.status_code == 400
        assert response.json()["message"] == Messages.LOGIN_BAD_PAYLOAD
