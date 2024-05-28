import requests
import allure
from data import URL


@allure.feature('Получение списка заказов')
class TestOrdersList:
    @allure.title('Получение списка заказов, код возврата 200 и в ответе не пустой список')
    def test_orders_list(self, url=URL.ORDER_URL):
        response = requests.get(url)
        assert response.status_code == 200
        assert response.json() != ""
