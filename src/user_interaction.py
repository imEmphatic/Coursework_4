from src.connection_api import HH
from src.json_class import GetJson

get_hh = HH()
my_vacancy = GetJson()


class UserInteraction:
    """Класс по поиску вакансий"""
    def __init__(self):
        pass

    @staticmethod
    def get_vacancies():
        """Вывод вакансий по ключевым словам"""
        name_vacancies = input(
            """Введите ключевые слова для поиска вакансий на сайте hh.ru (например название профессии):\n""")
        if get_hh.get_vacancies(100, name_vacancies) == []:
            print('Желаемые вакансии не найдены')
        else:
            vac = get_hh.get_vacancies(100, name_vacancies)
            my_vacancy.write_data(vac)
            vacanc = my_vacancy.get_vacancies()
            for i in vacanc:
                print(f'{i}\n')

    # def comparison(self):
    #     zp = int(input("Укажите желаемую зарплату и на экране останутся только подходящие вакансии\n"))
    #     # vacanc = my_vacancy.get_vacancies()
    #     for i in vacanc:
    #         if i.salary_from >= zp:
    #             print(f'{i}\n')
    #
    @staticmethod
    def top_n():
        """Вывод вакансий с самой большой зарплатой"""
        top_vac = int(input('Сколько вакансий показать с самой большой зарплатой?\nВведите число:\n'))
        vacanc = my_vacancy.get_vacancies()
        vacanc.sort(key=lambda vacanc: vacanc.salary_from, reverse=True)  # сортируем список вакансий по з/п
        for i in range(0, top_vac):
            print(f'{vacanc[i]}\n')
