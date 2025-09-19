import allure
import requests

from config import ORDER_LIST_ENDPOINT_URL

class TestOrderList:

    @allure.title('Проверка списка заказов')
    @allure.description('Проверяем, что возвращается список заказов')
    def test_get_order_list_order_list_is_returned(self):
        response = requests.get(ORDER_LIST_ENDPOINT_URL)

        assert response.status_code == 200
        assert isinstance(response.json()['orders'], list)
        assert len(response.json()['orders']) > 0