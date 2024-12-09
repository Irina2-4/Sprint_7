import pytest
from data import GenerateCourier

@pytest.fixture(scope='function')
def courier():
    payload = GenerateCourier.generate_courier_data()
    yield payload

@pytest.fixture(scope='function')
def courier_without_login():
    data_payload = GenerateCourier.generate_courier_without_login()
    yield data_payload
