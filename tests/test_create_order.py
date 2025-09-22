import allure
import pytest
import requests

from config import CREATE_ORDER_ENDPOINT_URL
from data.data_for_order_creation import DataForOrderCreation


class TestOrderCreation:

    @allure.title('Проверка создания заказа')
    @allure.description('Проверка успешного создания ордера с валидными данными')
    @pytest.mark.parametrize('body', DataForOrderCreation.VALID_ORDER_CREATION_DATA)
    def test_create_order_valid_data_order_is_created(self, body):
        response = requests.post(CREATE_ORDER_ENDPOINT_URL, json=body)
        assert response.status_code == 201
        assert 'track' in response.json()