import requests
import allure
from urls import Urls

class TestOrder:
    @allure.title('Получение списка заказов. Позитивный тест')
    def test_order_list(self):
        response = requests.get(f'{Urls.BASE_URL}{Urls.ORDERS_URL}')
        assert (response.status_code == 200 and "track" in response.text)
