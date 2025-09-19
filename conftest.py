from pytest import fixture
from faker import Faker

@fixture(scope='function')
def new_courier_data():
    faker = Faker()
    login = faker.user_name()
    password = faker.password(length=7, special_chars=False, digits=False)
    name = faker.first_name()

    return {'login': login, 'password': password, 'name': name}

