from src.connection_api import HH

test_api = HH()

def test_get_url():
    """тест на верное подключение к hh.ru"""
    assert test_api.get_url() == 'https://api.hh.ru/vacancies'
def test_connection_api():
    """проверка подключения"""
    assert str(test_api.get_response(1, "python")) == '<Response [200]>'

def test_get_vacancion():
    assert type(test_api.get_vacancies(1, 'python')) == list