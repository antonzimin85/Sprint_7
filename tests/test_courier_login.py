import allure
import pytest
import requests

from config import LOGIN_COURIER_ENDPOINT_URL
from data.data_for_courier_login import DataForCourierLogin


class TestCourierLogin:

    LOGIN_ERROR_REQUIRED_DATA_IS_MISSING = '{"code":400,"message":"Недостаточно данных для входа"}'
    LOGIN_ERROR_INVALID_CREDENTIALS = '{"code":404,"message":"Учетная запись не найдена"}'

    @allure.title('Проверка логина курьера с валидными данными')
    @allure.description('Проверка успешного логина курьера с валидными данными')
    def test_courier_login_successfully_logged_in(self, create_new_courier_and_created_courier_data, cleanup_created_courier):
        response = requests.post(LOGIN_COURIER_ENDPOINT_URL, json=create_new_courier_and_created_courier_data)
        assert response.status_code == 200
        assert 'id' in response.json()

        cleanup_created_courier.update(create_new_courier_and_created_courier_data)

    @allure.title('Проверка логина курьера без обязательных данных')
    @allure.description('Проверка, что нельзя авторизоваться без обязательных данных')
    @pytest.mark.parametrize('body', DataForCourierLogin.INVALID_COURIER_LOGIN_DATA)
    def test_courier_login_without_required_data_error_is_returned(self, body):
        response = requests.post(LOGIN_COURIER_ENDPOINT_URL, json=body)
        assert response.status_code == 400
        assert response.text == self.LOGIN_ERROR_REQUIRED_DATA_IS_MISSING

    @allure.title('Проверка логина курьера с невалидным логином или паролем')
    @allure.description('Проверка, что нельзя авторизоваться с невалидным логином или паролем')
    @pytest.mark.parametrize('body', DataForCourierLogin.NOT_EXISTING_COURIER_CREDENTIALS)
    def test_courier_login_invalid_credentials_error_is_returned(self, body):
        response = requests.post(LOGIN_COURIER_ENDPOINT_URL, json=body)
        assert response.status_code == 404
        assert response.text == self.LOGIN_ERROR_INVALID_CREDENTIALS
