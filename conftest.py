import requests

from pytest import fixture
from faker import Faker
from config import CREATE_COURIER_ENDPOINT_URL, LOGIN_COURIER_ENDPOINT_URL


@fixture(scope='function')
def new_courier_data():
    faker = Faker()
    login = faker.bothify(text='??????????????')
    password = faker.password(length=7, special_chars=False, upper_case=False, digits=False)
    name = faker.first_name()

    return {'login': login, 'password': password, 'name': name}

@fixture(scope='function')
def create_new_courier_and_return_created_courier_data(new_courier_data):

    body = {'login': new_courier_data['login'], 'password': new_courier_data['password']}
    requests.post(CREATE_COURIER_ENDPOINT_URL, json=body)

    return body

@fixture(scope='function')
def cleanup_created_courier():

    data = {}
    yield data

    login_body = {'login': data['login'], 'password': data['password']}
    login_response = requests.post(LOGIN_COURIER_ENDPOINT_URL, json=login_body)
    courier_id = login_response.json().get('id')

    requests.delete(f'{CREATE_COURIER_ENDPOINT_URL}/{courier_id}')