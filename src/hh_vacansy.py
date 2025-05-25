import requests

# ссылка на компанию Альфа
response_alfa = requests.get("https://api.hh.ru/employers/80")
company_alfa = response_alfa.json()

# ссылка на вакансии банка Альфа
response_alfa_vacancies = requests.get('https://api.hh.ru/vacancies?employer_id=80')
company_vacancies_alfa = response_alfa_vacancies.json()

# Ссылка на компанию ВТБ
response_vtb = requests.get("https://api.hh.ru/employers/4181")
company_vtb = response_vtb.json()

# ссылка на вакансии банка ВТБ
response_vtb_vacancies = requests.get('https://api.hh.ru/vacancies?employer_id=4181')
company_vacancies_vtb = response_vtb_vacancies.json()

# ссылка на компанию efin
response_efin = requests.get("https://api.hh.ru/employers/8643040")
company_efin = response_efin.json()

# ссылка на вакансии банка efin
response_efin_vacancies = requests.get('https://api.hh.ru/vacancies?employer_id=8643040')
company_vacancies_efin = response_efin_vacancies.json()

# ссылка на компанию efin
response_psb = requests.get("https://api.hh.ru/employers/6591")
company_psb = response_psb.json()

# ссылка на вакансии банка efin
response_psb_vacancies = requests.get('https://api.hh.ru/vacancies?employer_id=6591')
company_vacancies_psb = response_psb_vacancies.json()

# ссылка на компанию ТБанк
response_tbank = requests.get("https://api.hh.ru/employers/78638")
company_tbank = response_tbank.json()

# ссылка на вакансии банка ТБанк
response_tbank_vacancies = requests.get('https://api.hh.ru/vacancies?employer_id=78638')
company_vacancies_tbank = response_tbank_vacancies.json()

# ссылка на компанию Совкомбанк
response_sovcombank = requests.get("https://api.hh.ru/employers/7944")
company_sovcombank = response_sovcombank.json()

# ссылка на вакансии банка Совкомбанк
response_sovcombank_vacancies = requests.get('https://api.hh.ru/vacancies?employer_id=7944')
company_vacancies_sovcombank = response_sovcombank_vacancies.json()

# ссылка на компанию ПаоБанк
response_pao = requests.get("https://api.hh.ru/employers/89")
company_pao = response_pao.json()

# ссылка на вакансии банка ПаоБанк
response_pao_vacancies = requests.get('https://api.hh.ru/vacancies?employer_id=89')
company_vacancies_pao = response_pao_vacancies.json()

# ссылка на компанию ООО БСК
response_bsk = requests.get("https://api.hh.ru/employers/3003159")
company_bsk = response_bsk.json()

# ссылка на вакансии банка ООО БСК
response_bsk_vacancies = requests.get('https://api.hh.ru/vacancies?employer_id=3003159')
company_vacancies_bsk = response_bsk_vacancies.json()

# ссылка на компанию ОТП БАНК
response_otp = requests.get("https://api.hh.ru/employers/4394")
company_otp = response_otp.json()

# ссылка на вакансии банка ОТП БАНК
response_otp_vacancies = requests.get('https://api.hh.ru/vacancies?employer_id=4394')
company_vacancies_otp = response_otp_vacancies.json()

# ссылка на компанию БКС
response_bks = requests.get("https://api.hh.ru/employers/1833")
company_bks = response_bks.json()

# ссылка на вакансии банка БКС
response_bks_vacancies = requests.get('https://api.hh.ru/vacancies?employer_id=1833')
company_vacancies_bks = response_bks_vacancies.json()

# добавление в список id вакансий
list_id = []
for n in (company_vacancies_alfa["items"], company_vacancies_vtb["items"], company_vacancies_efin["items"],
          company_vacancies_psb["items"], company_vacancies_tbank["items"], company_vacancies_sovcombank["items"],
          company_vacancies_pao["items"], company_vacancies_bsk["items"], company_vacancies_otp["items"],
          company_vacancies_bks["items"]):
    for i in n:
        list_id.append(i["id"])


# добавление в список зарплаты вакансий
list_salary = []
for n in (company_vacancies_alfa["items"], company_vacancies_vtb["items"], company_vacancies_efin["items"],
          company_vacancies_psb["items"], company_vacancies_tbank["items"], company_vacancies_sovcombank["items"],
          company_vacancies_pao["items"], company_vacancies_bsk["items"], company_vacancies_otp["items"],
          company_vacancies_bks["items"]):
    for i in n:
        if i['salary'] is not None:
            list_salary.append(i['salary']['from'])
        else:
            list_salary.append(None)


# Добавление в список валюты каждой вакансии
list_currency = []
for n in (company_vacancies_alfa["items"], company_vacancies_vtb["items"], company_vacancies_efin["items"],
          company_vacancies_psb["items"], company_vacancies_tbank["items"], company_vacancies_sovcombank["items"],
          company_vacancies_pao["items"], company_vacancies_bsk["items"], company_vacancies_otp["items"],
          company_vacancies_bks["items"]):
    for i in n:
        if i['salary'] is not None:
            list_currency.append(i['salary']['currency'])
        else:
            list_currency.append(None)


# Добавление в список название каждой вакансии
list_name = []
for n in (company_vacancies_alfa["items"], company_vacancies_vtb["items"], company_vacancies_efin["items"],
          company_vacancies_psb["items"], company_vacancies_tbank["items"], company_vacancies_sovcombank["items"],
          company_vacancies_pao["items"], company_vacancies_bsk["items"], company_vacancies_otp["items"],
          company_vacancies_bks["items"]):
    for i in n:
        list_name.append(i['name'])

# Добавление в список url для каждой вакансии
list_url = []
for n in (company_vacancies_alfa["items"], company_vacancies_vtb["items"], company_vacancies_efin["items"],
          company_vacancies_psb["items"], company_vacancies_tbank["items"], company_vacancies_sovcombank["items"],
          company_vacancies_pao["items"], company_vacancies_bsk["items"], company_vacancies_otp["items"],
          company_vacancies_bks["items"]):
    for i in n:
        list_url.append(i['url'])


# Название компании
list_name_company = [company_alfa['name'], company_vtb['name'], company_efin['name'], company_psb['name'],
                     company_tbank['name'], company_sovcombank['name'], company_pao['name'], company_bsk['name'],
                     company_otp['name'], company_bks['name']]


# Добавление в список id компании Альфа
list_id_company = [company_alfa['id'], company_vtb['id'], company_efin['id'], company_psb['id'], company_tbank['id'],
                   company_sovcombank['id'], company_pao['id'], company_bsk['id'], company_otp['id'], company_bks['id']]


# Добавление в список id компаний для каждой вакансии
list_id_company_to_vacancies = []
for n in (company_vacancies_alfa["items"], company_vacancies_vtb["items"], company_vacancies_efin["items"],
          company_vacancies_psb["items"], company_vacancies_tbank["items"], company_vacancies_sovcombank["items"],
          company_vacancies_pao["items"], company_vacancies_bsk["items"], company_vacancies_otp["items"],
          company_vacancies_bks["items"]):
    for i in n:
        list_id_company_to_vacancies.append(i['employer']['id'])

# Соединение всех списков в один для вакансий
result_list_vacancies = list(zip(list_id, list_name, list_salary, list_currency, list_url,
                                 list_id_company_to_vacancies))


# Соединение всех списков в один для компаний
result_list_employees = list(zip(list_id_company, list_name_company))


