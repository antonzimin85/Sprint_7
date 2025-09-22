class DataForCourierLogin:

    EXISTING_COURIER_CREDENTIALS = {'login': 'piupiupiupiu', 'password': '12345555'}
    INVALID_COURIER_LOGIN_DATA = [
        {'login': 'piupiupiupiu', 'password': ''},
        {'login': '', 'password': '12345555'},
        {'login': '', 'password': ''}
    ]
    NOT_EXISTING_COURIER_CREDENTIALS = [
        {'login': 'piupiupiupiuw', 'password': '12345555'},
        {'login': 'piupiupiupiu', 'password': '123455556'}
    ]