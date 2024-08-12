import requests
from data import Constants
import allure

class TestOrderList():
    @allure.title('Проверка успешного получения списка заказов')
    def test_get_order_list_success(self):
        response = requests.get(Constants.URL_ORDERS)
        assert response.status_code == 200 and response.json()['orders'] is not None, \
            f'Status code is {response.status_code}, body={response.json()['orders']}'