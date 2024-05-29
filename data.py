class URL:
    BASE_URL = "https://qa-scooter.praktikum-services.ru/"
    ORDER_URL = f"{BASE_URL}api/v1/orders/"
    ORDER_ACCEPT_URL = f"{BASE_URL}api/v1/orders/accept/"
    ORDER_GET_URL = f"{BASE_URL}api/v1/orders/track?t="
    COURIER_URL = f"{BASE_URL}api/v1/courier"
    COURIER_DELETE_URL = f"{BASE_URL}/api/v1/courier/"
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
        "comment": "Saske, come back to Konoha",
        "color": ["BLACK"]
    }
    payload_without_color = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha"
    }


class Messages:
    GET_ORDER_BY_ID_NO_TRACK = "Недостаточно данных для поиска"
    GET_ORDER_BY_ID_BAD_TRACK = "Заказ не найден"
    LOGIN_INVALID_404 = "Учетная запись не найдена"
    LOGIN_BAD_PAYLOAD = "Недостаточно данных для входа"
    DELETE_WITHOUT_ID = "Not Found."
    DELETE_BAD_ID = "Курьера с таким id нет."
    CREATE_BAD_PAYLOAD = "Недостаточно данных для создания учетной записи"
    CREATE_TWICE = "Этот логин уже используется. Попробуйте другой."
    ACCEPT_ORDER_NO_ID = "Недостаточно данных для поиска"
    ACCEPT_ORDER_BAD_ID = "Заказа с таким id не существует"
    ACCEPT_ORDER_BAD_COURIER_ID = "Курьера с таким id не существует"
    ACCEPT_ORDER_TWICE = "Этот заказ уже в работе"
    ACCEPT_ORDER_NO_ID_NO_COURIER_ID = "Недостаточно данных для поиска"
    OK = '{"ok":true}'
