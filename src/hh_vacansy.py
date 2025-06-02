import requests


def all_id():
    list_id_all = [80, 4181, 8643040, 6591, 78638, 7944, 89, 3003159, 4394, 1833]
    return list_id_all


def api_vacancies():
    list_id_all = all_id()
    list_vacancies = []
    list_id = []
    list_salary = []
    list_currency = []
    list_name = []
    list_url = []
    list_id_company_to_vacancies = []
    for i in list_id_all:
        response_vacancies = requests.get(f'https://api.hh.ru/vacancies?employer_id={i}')
        company_vacancies = response_vacancies.json()
        for items in company_vacancies['items']:
            list_vacancies.append(items)

    for id in list_vacancies:
        list_id.append(id["id"])
    for salary in list_vacancies:
        if salary['salary'] is not None:
            list_salary.append(salary['salary']['from'])
        else:
            list_salary.append(None)
    for currency in list_vacancies:
        if currency['salary'] is not None:
            list_currency.append(currency['salary']['currency'])
        else:
            list_currency.append(None)
    for name in list_vacancies:
        list_name.append(name['name'])
    for url in list_vacancies:
        list_url.append(url['url'])
    for id_company_vacancies in list_vacancies:
        list_id_company_to_vacancies.append(id_company_vacancies['employer']['id'])
    result_list_vacancies = list(zip(list_id, list_name, list_salary, list_currency, list_url,
                                     list_id_company_to_vacancies))
    return result_list_vacancies


def api_employees():
    list_id_all = all_id()
    list_name_company = []
    for i in list_id_all:
        response_employers = requests.get(f"https://api.hh.ru/employers/{i}")
        company_employers = response_employers.json()
        list_name_company.append(company_employers['name'])
    result_list_employees = list(zip(list_id_all, list_name_company))
    return result_list_employees
