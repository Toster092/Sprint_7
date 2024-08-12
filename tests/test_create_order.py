import requests
from data import Constants
import pytest
import allure

class TestCreateOrder():
    @pytest.mark.parametrize('color,expected_result', [([-1], 'BLACK'),
                                                       ([-1], 'GRAY'),
                                                       ([-1], ['BLACK', 'GRAY']),
                                                       ([-1], None)])
    @allure.title('Проверка успешного создания заказа с выбором цвета')
    def test_create_order(self, color, expected_result):
        payload = {
            "firstName": "Leo",
            "lastName": "Fernandes",
            "address": "stadium Dynamo",
            "metroStation": 28,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Blue White Dynamite",
            "color": []
        }
        response = requests.post(Constants.URL_ORDERS, json=payload)
        assert response.status_code == 201 and response.json()['track'] is not None, \
            f'Status code is {response.status_code}, body={response.json()['track']}'