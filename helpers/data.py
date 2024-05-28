class URL:
    BASE_URL = "https://qa-scooter.praktikum-services.ru/"
    ORDER_URL = f"{BASE_URL}api/v1/orders/"
    ORDER_GET_URL = f"{BASE_URL}/api/v1/orders/track?t="
    COURIER_URL = f"{BASE_URL}api/v1/courier"
    COURIER_LOGIN_URL = f"{BASE_URL}api/v1/courier/login"


class Order:
    payload = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha"
    }
