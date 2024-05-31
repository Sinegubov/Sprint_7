import requests
import allure
from data import URL, Messages
from helpers import CourierGenerator


@allure.feature('Принять заказ по его номеру и id курьера')
class TestPutOrderAccept:
    @allure.title('Успешное принятие заказа')
    def test_accept_order(self, take_id_order, create_courier, url=URL.ORDER_ACCEPT_URL):
        id_order = take_id_order
        id_courier = create_courier
        response = requests.put(f"{url}{id_order}?courierId={id_courier}")
        assert response.status_code == 200
        assert response.text == Messages.OK

    @allure.title('Запрос c несуществующим id номером')
    def test_accept_order_bad_id_negative(self, create_courier, url=URL.ORDER_ACCEPT_URL):
        id_order = CourierGenerator().random_string_id()
        id_courier = create_courier
        response = requests.put(f'{url}{id_order}?courierId={id_courier}')
        assert response.status_code == 404
        assert response.json()["message"] == Messages.ACCEPT_ORDER_BAD_ID

    @allure.title('Запрос c несуществующим id курьера')
    def test_accept_order_bad_courier_id_negative(self, take_id_order, url=URL.ORDER_ACCEPT_URL):
        id_courier = CourierGenerator().random_string_id()
        id_order = take_id_order
        response = requests.put(f'{url}{id_order}?courierId={id_courier}')
        assert response.status_code == 404
        assert response.json()["message"] == Messages.ACCEPT_ORDER_BAD_COURIER_ID

    @allure.title('Нет id заказа')
    def test_accept_order_no_id_negative(self, create_courier, url=URL.ORDER_ACCEPT_URL):
        id_courier = create_courier
        response = requests.put(f"{url}?courierId={id_courier}")
        # Баг. Присылается 'code:404,message:Not Found'
        assert response.status_code == 404
        assert response.json()["message"] == Messages.DELETE_WITHOUT_ID

    @allure.title('Нет id курьера')
    def test_accept_order_no_id_courier_negative(self, take_id_order, url=URL.ORDER_ACCEPT_URL):
        id_order = take_id_order
        id_courier = ""
        response = requests.put(f"{url}{id_order}?courierId={id_courier}")
        # Баг. Присылается 'code:404,message:Not Found'
        assert response.status_code == 400
        assert response.json()["message"] == Messages.ACCEPT_ORDER_NO_ID

    @allure.title('Заказ уже был в работе')
    def test_accept_twice_negative(self, take_id_order, create_courier, url=URL.ORDER_ACCEPT_URL):
        id_order = take_id_order
        id_courier = create_courier
        requests.put(f"{url}{id_order}?courierId={id_courier}")
        response = requests.put(f"{url}{id_order}?courierId={id_courier}")
        assert response.status_code == 409
        assert response.json()["message"] == Messages.ACCEPT_ORDER_TWICE
