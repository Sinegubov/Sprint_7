import requests
import allure
from data import URL, Messages
from helpers.register_new_courier import CourierGenerator


@allure.feature('Получение заказа по его номеру')
class TestGetOrder:
    @allure.title('Получение заказа по его номеру')
    def test_get_order(self, list_url=URL.ORDER_URL, order_url=URL.ORDER_GET_URL):
        response_track = requests.get(list_url).json()['orders'][0]['track']
        response = requests.get(f"{order_url}{response_track}")
        assert response.status_code == 200
        assert response.text != ""

    @allure.title('Запрос без номера заказа возвращает ошибку')
    def test_get_order_no_track_negative(self, order_url=URL.ORDER_GET_URL):
        response = requests.get(order_url)
        assert response.status_code == 400
        assert response.json()["message"] == Messages.GET_ORDER_BY_ID_NO_TRACK

    @allure.title('Запрос с несуществующим номером возвращает ошибку')
    def test_get_order_bad_track_negative(self, order_url=URL.ORDER_GET_URL,
                                          response_track=CourierGenerator.random_string_id()):
        response = requests.get(f"{order_url}{response_track}")
        assert response.status_code == 404
        assert response.json()["message"] == Messages.GET_ORDER_BY_ID_BAD_TRACK
