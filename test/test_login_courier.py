import allure
from urls import Urls
from conftest import courier,courier_without_login
import requests
from data import Response
class TestCreateCourier:

    @allure.title('Авторизация курьера. Позитивный тест')
    def test_avtorization_courier(self, courier):
        requests.post(f'{Urls.BASE_URL}{Urls.COURIERS_URL}', data=courier)
        response = requests.post(f'{Urls.BASE_URL}{Urls.COURIERS_LOGIN}', data=courier)
        assert response.status_code == 200 and id != ''

    @allure.title('Авторизация курьера без указания логина. Негативный тест')
    def test_create_courier_data_without_login(self, courier_without_login):
        response = requests.post(f'{Urls.BASE_URL}{Urls.COURIERS_LOGIN}', data=courier_without_login)
        assert (response.status_code == 400) and (response.json()["message"] == Response.no_data_to_log_in)

    @allure.title('Авторизация курьера с несуществующей парой логин-пароль. Негативный тест')
    def test_authorization_error_if_no_log(self,courier):
          response =  requests.post(f'{Urls.BASE_URL}{Urls.COURIERS_LOGIN}',data = courier)
          assert response.status_code == 404 and response.json()["message"] == Response.account_not_found
