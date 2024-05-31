import requests
import allure
from data import URL, Messages
from helpers import CourierGenerator


@allure.feature('Проверка удаления курьера')
class TestDeleteCourier:
    @allure.title('Проверка удаления курьера со всеми полями')
    def test_courier_delete(self, url_login=URL.COURIER_LOGIN_URL, url=URL.COURIER_URL):
        data = CourierGenerator().register_new_courier_and_return_login_password()
        response_id = requests.post(url_login, data=data).json()["id"]
        response = requests.delete(f"{url}/{response_id}")
        assert response.status_code == 200
        assert response.text == Messages.OK

    @allure.title('Проверяем, запрос с несуществующим id курьера')
    def test_courier_delete_with_bad_id(self, url=URL.COURIER_URL):
        courier_id = CourierGenerator().random_string_id()
        response = requests.delete(f"{url}/{courier_id}")
        assert response.status_code == 404
        assert response.json()["message"] == Messages.DELETE_BAD_ID

    @allure.title('Проверяем, запрос без id')
    def test_courier_delete_without_id(self, url=URL.COURIER_URL):
        response = requests.delete(url)
        assert response.status_code == 404
        assert response.json()["message"] == Messages.DELETE_WITHOUT_ID
