import pytest
import requests

from data import URL, Order
from helpers import CourierGenerator


@pytest.fixture(scope='function')
def create_order():
    response_create_order = requests.post(URL.ORDER_URL, json=Order.payload)
    track = response_create_order.json()['track']
    return track


@pytest.fixture(scope='function')
def take_id_order(create_order):
    track = create_order
    response_get_id_order = requests.get(f'{URL.ORDER_GET_URL}{track}')
    id_order = response_get_id_order.json()['order']['id']
    return id_order


@pytest.fixture(scope='function')
def create_courier():
    login_pass = CourierGenerator().register_new_courier_and_return_login_password()
    response_post = requests.post(URL.COURIER_LOGIN_URL, data=login_pass)
    courier_id = response_post.json()['id']
    yield courier_id
    requests.delete(f'{URL.COURIER_DELETE_URL}/{courier_id}')
