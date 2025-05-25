from src.hh_api import DBManager


def interface():
    print("Основные команды:\nПолучить список всех компаний и количество вакансий у каждой компании - 1\n"
          "Получить список всех вакансий с указанием названия компании, названия вакансии и зарплаты и "
          "ссылки на вакансию - 2\nПолучить среднюю зарплату по вакансиям - 3\nПолучить список всех вакансий, "
          "у которых зарплата выше средней по всем вакансиям - 4\nПолучить список всех вакансий, в названии "
          "которых содержатся переданные в метод слова - 5")
    user_word = int(input("Введите цифру: "))
    if user_word == 1:
        user_result = DBManager()
        return user_result.get_companies_and_vacancies_count()
    elif user_word == 2:
        user_result = DBManager()
        return user_result.get_all_vacancies()
    elif user_word == 3:
        user_result = DBManager()
        return user_result.get_avg_salary()
    elif user_word == 4:
        user_result = DBManager()
        return user_result.get_vacancies_with_higher_salary()
    elif user_word == 5:
        user_result = DBManager()
        return user_result.get_vacancies_with_keyword()


print(interface())
