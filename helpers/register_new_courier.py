from faker import Faker

fake = Faker(locale="ru_RU")


class CourierGenerator:
    @staticmethod
    def generate_courier_payload():
        login = fake.text(max_nb_chars=10)
        password = fake.password(length=6, special_chars=False, digits=True, upper_case=True, lower_case=True)
        firstname = fake.name()
        payload = {"login": login, "password": password, "firstName": firstname}
        return payload

    @staticmethod
    def bad_courier_id():
        return str(fake.random_int(min=1000000, max=100000000))

