import requests
from data import Constants
from faker import Faker
import allure

faker = Faker()
class TestCreateCourier():
    @classmethod
    def setup_class(cls):
        cls.courier_data = {
            'login': faker.user_name(),
            'password': faker.password(),
            'firstName': faker.first_name()
        }
    def teardown_class(cls):
        login_payload = {
            'login': cls.courier_data['login'],
            'password': cls.courier_data['password']
        }
        response = requests.post(Constants.URL_LOGIN, json=login_payload)
        courier_id = response.json()['id']
        requests.delete(f'{Constants.URL_DELETE}{courier_id}')

    @allure.title('Проверка успешного создания курьера')
    def test_create_courier_success(self):
        payload = self.courier_data
        response = requests.post(Constants.URL_COURIER, json=payload)
        assert response.status_code == 201 and response.json() == Constants.BODY_SUCCESS_REG, \
            f'Status code is {response.status_code}, body={response.json()}'

    @allure.title('Проверка получения ошибки при создании курьера без поля Имя')
    def test_create_courier_without_name_shows_error(self):
        payload = {
            'login': faker.user_name(),
            'password': faker.password()
        }
        response = requests.post(Constants.URL_COURIER, json=payload)
        assert response.status_code == 400 and response.json() == Constants.BODY_NO_FIELD,\
            f'Status code is {response.status_code}, body={response.json()}'

    @allure.title('Проверка получения ошибки при создании курьера без поля Логин')
    def test_create_courier_without_login_shows_error(self):
        payload = {
            'password': faker.password(),
            'firstName': faker.first_name()
        }
        response = requests.post(Constants.URL_COURIER, json=payload)
        assert response.status_code == 400 and response.json() == Constants.BODY_NO_FIELD, \
            f'Status code is {response.status_code}, body={response.json()}'

    @allure.title('Проверка получения ошибки при создании курьера без поля Пароль')
    def test_create_courier_without_password_shows_error(self):
        payload = {
            'login': faker.user_name(),
            'firstName': faker.first_name()
        }
        response = requests.post(Constants.URL_COURIER, json=payload)
        assert response.status_code == 400 and response.json() == Constants.BODY_NO_FIELD, \
            f'Status code is {response.status_code}, body={response.json()}'

    @allure.title('Проверка получения ошибки при создании одинковых курьеров')
    def test_create_same_couriers_shows_error(self):
        payload = self.courier_data
        response = requests.post(Constants.URL_COURIER, json=payload)
        assert response.status_code == 409 and response.json() == Constants.BODY_SAME_LOG, \
            f'Status code is {response.status_code}, body={response.json()}'

