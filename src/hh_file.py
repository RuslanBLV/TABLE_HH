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
        data = user_result.get_companies_and_vacancies_count()
        for i in data:
            print(f"Компания: {i[0]}")
            print(f"Количество вакансий: {i[1]}\n")
        return "Конец"
    elif user_word == 2:
        user_result = DBManager()
        data = user_result.get_all_vacancies()
        for i in data:
            print(f"ID вакансии: {i[0]}")
            print(f"Описание: {i[1]}")
            print(f"Зарплата: {i[2]}")
            print(f"Ссылка: {i[4]}")
            print(f"Компания: {i[5]}\n")
        return "Конец"
    elif user_word == 3:
        user_result = DBManager()
        data = user_result.get_avg_salary()
        for i in data:
            print(f"Средняя зарплата вакансий: {i[0]}")
        return "Конец"
    elif user_word == 4:
        user_result = DBManager()
        data = user_result.get_vacancies_with_higher_salary()
        for i in data:
            print(f"ID вакансии: {i[0]}")
            print(f"Описание: {i[1]}")
            print(f"Зарплата: {i[2]}")
            print(f"Валюта: {i[3]}")
            print(f"Ссылка: {i[4]}")
            print(f"ID Компании: {i[5]}\n")
        return "Конец"
    elif user_word == 5:
        user_result = DBManager()
        data = user_result.get_vacancies_with_keyword()
        for i in data:
            print(f"ID вакансии: {i[0]}")
            print(f"Описание: {i[1]}")
            print(f"Зарплата: {i[2]}")
            print(f"Валюта: {i[3]}")
            print(f"Ссылка: {i[4]}")
            print(f"ID Компании: {i[5]}\n")
        return "Конец"
