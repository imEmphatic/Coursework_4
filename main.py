from src.json_class import GetJson
from src.user_interaction import UserInteraction


if __name__ == "__main__":
    print("Здравствуйте!")
    user = UserInteraction()
    user.get_vacancies() #получаем вакансии
    user.top_n() #топ N вакансий

    my_vacancy = GetJson()
    my_vacancy.delete_vacancy()  # очищаем файл vacancies.json