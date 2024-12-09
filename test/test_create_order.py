import pytest
import requests
from data import GenerateOrder
import allure
from urls import Urls


class TestCreateOrder:
    @allure.title('Проверка создания заказа. Позитивный тест')
    @pytest.mark.parametrize('color',GenerateOrder.color)
    def test_create_order(self, color):
        data = GenerateOrder.generate_order
        data['color'] = color
        response = requests.post(f'{Urls.BASE_URL}{Urls.ORDERS_URL}', json=data)
        assert response.status_code == 201 and 'track' in response.text
