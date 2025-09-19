import allure
import pytest
import requests

from config import CREATE_COURIER_ENDPOINT_URL
from data.data_for_courier_creation import DataForCourierCreation


class TestCourierCreation:

    SUCCESS_RESPONSE_MESSAGE = '{"ok":true}'
    SIGNUP_ERROR_COURIER_EXISTS_RESPONSE_MESSAGE = '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}'
    SIGNUP_ERROR_REQUIRED_DATA_IS_MISSING = '{"code":400,"message":"Недостаточно данных для создания учетной записи"}'

    @allure.title('Проверка создания курьера с валидными данными')
    @allure.description('Проверка успешного создания курьера с валидными данными')
    def test_create_courier_valid_data_courier_successfully_created(self, new_courier_data, cleanup_created_courier):
        response = requests.post(CREATE_COURIER_ENDPOINT_URL, json=new_courier_data)
        assert response.status_code == 201
        assert response.text == self.SUCCESS_RESPONSE_MESSAGE

        cleanup_created_courier.update(new_courier_data)

    @allure.title('Проверка создания двух одинаковых курьеров')
    @allure.description('Проверка, что нельзя создать одинаковых курьеров')
    def test_create_courier_existing_courier_error_is_returned(self, new_courier_data, cleanup_created_courier):
        requests.post(CREATE_COURIER_ENDPOINT_URL, json=new_courier_data)
        response = requests.post(CREATE_COURIER_ENDPOINT_URL, json=new_courier_data)
        assert response.status_code == 409
        assert response.text == self.SIGNUP_ERROR_COURIER_EXISTS_RESPONSE_MESSAGE

        cleanup_created_courier.update(new_courier_data)

    @allure.title('Проверка создания курьера без обязательных полей')
    @allure.description('Проверка, что нельзя создать курьера без обязательных полей')
    @pytest.mark.parametrize('body', DataForCourierCreation.INVALID_COURIER_CREATION_DATA)
    def test_create_courier_without_required_data_error_is_returned(self, body):
        response = requests.post(CREATE_COURIER_ENDPOINT_URL, json=body)
        assert response.status_code == 400
        assert response.text == self.SIGNUP_ERROR_REQUIRED_DATA_IS_MISSING