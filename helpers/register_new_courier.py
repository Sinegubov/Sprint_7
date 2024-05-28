from faker import Faker

fake = Faker(locale="ru_RU")


class CourierGenerator:

    @staticmethod
    def generate_data():
        login = fake.text(max_nb_chars=10)
        password = fake.password(length=6, special_chars=False, digits=True, upper_case=True, lower_case=True)
        firstname = fake.name()
        return login, password, firstname

    def generate_courier_payload(self):
        login, password, firstname = self.generate_data()
        payload = {
            "login": login,
            "password": password,
            "firstName": firstname
        }
        return payload

    @staticmethod
    def random_string_id():
        return str(fake.random_int(min=100000, max=10000000))
