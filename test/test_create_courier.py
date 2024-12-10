import allure
from data import Response
from urls import Urls
from conftest import courier,courier_without_login
import requests


class TestCreateCourier:

    @allure.title('Создание курьера. Позитивный тест')
    def test_create_courier(self, courier):
        response = requests.post(f'{Urls.BASE_URL}{Urls.COURIERS_URL}', data=courier)
        assert response.status_code == 201 and response.text == Response.reg_successful

    @allure.title('Создание двух одинаковых курьеров. Негативный тест')
    def test_create_two_couriers(self,courier):
        requests.post(f'{Urls.BASE_URL}{Urls.COURIERS_URL}',data = courier)
        response_neg = requests.post(f'{Urls.BASE_URL}{Urls.COURIERS_URL}', data=courier)
        assert (response_neg.status_code == 409) and (response_neg.json()["message"] == Response.log_used)

    @allure.title('Создание курьера без указания логина. Негативный тест ')
    def test_create_courier_data_without_login(self,courier_without_login):
        response = requests.post(f'{Urls.BASE_URL}{Urls.COURIERS_URL}', data=courier_without_login)
        assert (response.status_code == 400) and (response.json()["message"] == Response.not_data_to_create_an_account)