import random
import string
class GenerateCourier:
    @staticmethod
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @staticmethod

    def generate_courier_data():
    # генерируем логин, пароль и имя курьера
        login = GenerateCourier.generate_random_string(10)
        password = GenerateCourier.generate_random_string(10)
        first_name = GenerateCourier.generate_random_string(10)

    # собираем тело запроса
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
             }
        return payload

    @staticmethod
    def generate_courier_without_login():
    # генерируем логин, пароль и имя курьера
        password = GenerateCourier.generate_random_string(10)
        first_name = GenerateCourier.generate_random_string(10)
    # собираем тело запроса
        payload = {
            "password": password,
            "firstName": first_name
             }
        return payload

class GenerateOrder:
    generate_order = {
            "firstName": "Иван",
            "lastName": "Иванов",
            "address": "Льва Толстого 16",
            "metroStation": "Парк культуры",
            "phone": "+76785423223",
            "rentTime": 2,
            "deliveryDate": "2024-12-12",
            "comment": 'Не грустите '
        }

    color = [['GREY'],['BLACK'],(['GREY'],['BLACK']),['']]
class Response:
    reg_successful = '{"ok":true}'
    not_data_to_create_an_account = "Недостаточно данных для создания учетной записи"
    log_used = 'Этот логин уже используется. Попробуйте другой.'
    no_data_to_log_in = "Недостаточно данных для входа"
    account_not_found = 'Учетная запись не найдена'