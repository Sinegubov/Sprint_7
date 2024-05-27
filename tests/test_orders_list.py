import requests
import allure
from helpers.register_new_courier import CourierGenerator
from helpers.data import URL


@allure.feature('Проверка регистрации курьера')
class TestCourierCreate:
    @allure.title('Получение списка заказов')
    def test_courier_create(self, url=URL.ORDER_URL, payload=CourierGenerator.generate_courier_payload()):
        response = requests.get(url)
        print(response.text)
        assert response.status_code == 200
        assert response.json() != ""
