import requests
from data import Constants
from faker import Faker
import allure

faker = Faker()

class TestLoginCourier:
    @classmethod
    def setup_class(cls):
        cls.courier_data = {
            'login': faker.user_name(),
            'password': faker.password(),
            'firstName': faker.first_name()
        }
        requests.post(Constants.URL_COURIER, json=cls.courier_data)

    @classmethod
    def teardown_class(cls):
        login_payload = {
            'login': cls.courier_data['login'],
            'password': cls.courier_data['password']
        }
        response = requests.post(Constants.URL_LOGIN, json=login_payload)
        courier_id = response.json()['id']
        requests.delete(f'{Constants.URL_DELETE}{courier_id}')

    @allure.title('Проверка успешной авторизации курьера')
    def test_login_success(self):
        payload = {
            'login': self.courier_data['login'],
            'password': self.courier_data['password']
        }
        response = requests.post(Constants.URL_LOGIN, json=payload)
        assert response.status_code == 200 and response.json()['id'] is not None, \
            f'Status code is {response.status_code}, body={response.json()['id']}'

    @allure.title('Проверка получения ошибки при авторизации курьера без поля Логин')
    def test_login_without_field_shows_error(self):
        payload = {
            'password': self.courier_data['password']
        }
        response = requests.post(Constants.URL_LOGIN, json=payload)
        assert response.status_code == 400 and response.json() == Constants.BODY_NO_FIELD_LOG, \
            f'Status code is {response.status_code}, body={response.json()}'

    @allure.title('Проверка получения ошибки при авторизации курьера с неправильным паролем')
    def test_login_with_wrong_pass_shows_error(self):
        payload = {
            'login': self.courier_data['login'],
            'password': faker.password()
        }
        response = requests.post(Constants.URL_LOGIN, json=payload)
        assert response.status_code == 404 and response.json() == Constants.BODY_WRONG_PASS, \
            f'Status code is {response.status_code}, body={response.json()}'