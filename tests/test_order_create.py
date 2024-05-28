import requests
import allure
import pytest
import json
from data import URL, Order


@allure.feature('Проверка создания заказа')
class TestOrderCreate:
    @pytest.mark.parametrize("data",
                             [
                                 {"color": "[BLACK]"},
                                 {"color": "[BLACK, GREY]"},
                                 {"color": "[GREY]"},
                                 {"color": "[]"},
                             ])
    @allure.title('Проверка создания заказа c разными вариантами цветов самоката')
    def test_order_create(self, data, url=URL.ORDER_URL):
        payload = Order.payload.update(data)
        payload_string = json.dumps(payload)
        response = requests.post(url, data=payload_string)
        assert response.status_code == 201
        assert response.json()["track"] != ""
