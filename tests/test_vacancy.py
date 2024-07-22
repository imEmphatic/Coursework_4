from src.vacancy import Vacancy

test_class = Vacancy('Название проффесии', None, 'ссылка', 'описание')

def test_validate_salary():
    test_class.validate_salary(None)
    assert test_class.salary_from == 0

def test_str():
    assert test_class.__str__() == f"""Профессия: Название проффесии
Зарплата от 0 руб. до 0 руб.
url: ссылка
Название компании: описание"""