import requests
import allure
from data import URL, Messages
from helpers.register_new_courier import CourierGenerator


@allure.feature('Принять заказ по его номеру и id курьера')
class TestGetOrder:
    @allure.title('Успешное принятие заказа')
    def test_accept_order(
            self,
            url=URL.ORDER_ACCEPT_URL,
            payload=CourierGenerator().generate_courier_payload(),
            url_orders_list=URL.ORDER_URL):
        order_id = requests.get(url_orders_list).json()["orders"][1]["id"]
        print(order_id)
        data = {
            "login": payload["login"],
            "password": payload["password"]
        }
        requests.post(URL.COURIER_URL, data=data)
        response_courier = requests.post(URL.COURIER_LOGIN_URL, data=data)
        courier_id = response_courier.json()["id"]
        response = requests.put(f"{url}{order_id}?courierId={courier_id}")
        assert response.status_code == 200
        assert response.text == Messages.OK

    @allure.title('Запрос c несуществующим номером')
    def test_accept_order_bad_id_negative(
            self,
            url=URL.ORDER_ACCEPT_URL,
            payload=CourierGenerator().generate_courier_payload()):
        order_id = CourierGenerator().random_string_id()
        data = {
            "login": payload["login"],
            "password": payload["password"]
        }
        requests.post(URL.COURIER_URL, data=data)
        response_courier = requests.post(URL.COURIER_LOGIN_URL, data=data)
        courier_id = response_courier.json()["id"]
        response = requests.put(f"{url}{order_id}?courierId={courier_id}")
        assert response.status_code == 404
        assert response.json()["message"] == Messages.ACCEPT_ORDER_BAD_ID

    @allure.title('Запрос c несуществующим номером курьера')
    def test_accept_order_bad_courier_id_negative(
            self,
            url=URL.ORDER_ACCEPT_URL,
            url_orders_list=URL.ORDER_URL):
        order_id = requests.get(url_orders_list).json()["orders"][1]["id"]
        courier_id = CourierGenerator().random_string_id()
        response = requests.put(f"{url}{order_id}?courierId={courier_id}")
        assert response.status_code == 404
        assert response.json()["message"] == Messages.ACCEPT_ORDER_BAD_COURIER_ID

    @allure.title('Нет id курьера или id заказа')
    def test_accept_order_no_id_negative(self, url=URL.ORDER_ACCEPT_URL):
        order_id = ""
        courier_id = ""
        response = requests.put(f"{url}{order_id}?courierId={courier_id}")
        assert response.status_code == 404
        assert response.json()["message"] == Messages.DELETE_WITHOUT_ID

    @allure.title('Заказ уже был в работе')
    def test_accept_twice_negative(
            self,
            url=URL.ORDER_ACCEPT_URL,
            payload=CourierGenerator().generate_courier_payload(),
            url_orders_list=URL.ORDER_URL):
        order_id = requests.get(url_orders_list).json()["orders"][1]["id"]
        data = {
            "login": payload["login"],
            "password": payload["password"]
        }
        requests.post(URL.COURIER_URL, data=data)
        response_courier = requests.post(URL.COURIER_LOGIN_URL, data=data)
        courier_id = response_courier.json()["id"]
        requests.put(f"{url}{order_id}?courierId={courier_id}")
        response = requests.put(f"{url}{order_id}?courierId={courier_id}")
        assert response.status_code == 409
        assert response.json()["message"] == Messages.ACCEPT_ORDER_TWICE
