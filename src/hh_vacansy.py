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
for i in company_vacancies_alfa["items"]:
    list_id.append(i["id"])
for i in company_vacancies_vtb["items"]:
    list_id.append(i["id"])
for i in company_vacancies_efin["items"]:
    list_id.append(i["id"])
for i in company_vacancies_psb["items"]:
    list_id.append(i["id"])
for i in company_vacancies_tbank["items"]:
    list_id.append(i["id"])
for i in company_vacancies_sovcombank["items"]:
    list_id.append(i["id"])
for i in company_vacancies_pao["items"]:
    list_id.append(i["id"])
for i in company_vacancies_bsk["items"]:
    list_id.append(i["id"])
for i in company_vacancies_otp["items"]:
    list_id.append(i["id"])
for i in company_vacancies_bks["items"]:
    list_id.append(i["id"])


# добавление в список зарплаты вакансий
list_salary = []
for i in company_vacancies_alfa['items']:
    if i['salary'] is not None:
        list_salary.append(i['salary']['from'])
    else:
        list_salary.append(None)
for i in company_vacancies_vtb['items']:
    if i['salary'] is not None:
        list_salary.append(i['salary']['from'])
    else:
        list_salary.append(None)
for i in company_vacancies_efin['items']:
    if i['salary'] is not None:
        list_salary.append(i['salary']['from'])
    else:
        list_salary.append(None)
for i in company_vacancies_psb['items']:
    if i['salary'] is not None:
        list_salary.append(i['salary']['from'])
    else:
        list_salary.append(None)
for i in company_vacancies_tbank['items']:
    if i['salary'] is not None:
        list_salary.append(i['salary']['from'])
    else:
        list_salary.append(None)
for i in company_vacancies_sovcombank['items']:
    if i['salary'] is not None:
        list_salary.append(i['salary']['from'])
    else:
        list_salary.append(None)
for i in company_vacancies_pao['items']:
    if i['salary'] is not None:
        list_salary.append(i['salary']['from'])
    else:
        list_salary.append(None)
for i in company_vacancies_bsk['items']:
    if i['salary'] is not None:
        list_salary.append(i['salary']['from'])
    else:
        list_salary.append(None)
for i in company_vacancies_otp['items']:
    if i['salary'] is not None:
        list_salary.append(i['salary']['from'])
    else:
        list_salary.append(None)
for i in company_vacancies_bks['items']:
    if i['salary'] is not None:
        list_salary.append(i['salary']['from'])
    else:
        list_salary.append(None)


# Добавление в список валюты каждой вакансии
list_currency = []
for i in company_vacancies_alfa['items']:
    if i['salary'] is not None:
        list_currency.append(i['salary']['currency'])
    else:
        list_currency.append(None)
for i in company_vacancies_vtb['items']:
    if i['salary'] is not None:
        list_currency.append(i['salary']['currency'])
    else:
        list_currency.append(None)
for i in company_vacancies_efin['items']:
    if i['salary'] is not None:
        list_currency.append(i['salary']['currency'])
    else:
        list_currency.append(None)
for i in company_vacancies_psb['items']:
    if i['salary'] is not None:
        list_currency.append(i['salary']['currency'])
    else:
        list_currency.append(None)
for i in company_vacancies_tbank['items']:
    if i['salary'] is not None:
        list_currency.append(i['salary']['currency'])
    else:
        list_currency.append(None)
for i in company_vacancies_sovcombank['items']:
    if i['salary'] is not None:
        list_currency.append(i['salary']['currency'])
    else:
        list_currency.append(None)
for i in company_vacancies_pao['items']:
    if i['salary'] is not None:
        list_currency.append(i['salary']['currency'])
    else:
        list_currency.append(None)
for i in company_vacancies_bsk['items']:
    if i['salary'] is not None:
        list_currency.append(i['salary']['currency'])
    else:
        list_currency.append(None)
for i in company_vacancies_otp['items']:
    if i['salary'] is not None:
        list_currency.append(i['salary']['currency'])
    else:
        list_currency.append(None)
for i in company_vacancies_bks['items']:
    if i['salary'] is not None:
        list_currency.append(i['salary']['currency'])
    else:
        list_currency.append(None)


# Добавление в список название каждой вакансии
list_name = []
for i in company_vacancies_alfa['items']:
    list_name.append(i['name'])
for i in company_vacancies_vtb['items']:
    list_name.append(i['name'])
for i in company_vacancies_efin['items']:
    list_name.append(i['name'])
for i in company_vacancies_psb['items']:
    list_name.append(i['name'])
for i in company_vacancies_tbank['items']:
    list_name.append(i['name'])
for i in company_vacancies_sovcombank['items']:
    list_name.append(i['name'])
for i in company_vacancies_pao['items']:
    list_name.append(i['name'])
for i in company_vacancies_bsk['items']:
    list_name.append(i['name'])
for i in company_vacancies_otp['items']:
    list_name.append(i['name'])
for i in company_vacancies_bks['items']:
    list_name.append(i['name'])


# Добавление в список url для каждой вакансии
list_url = []
for i in company_vacancies_alfa['items']:
    list_url.append(i['url'])
for i in company_vacancies_vtb['items']:
    list_url.append(i['url'])
for i in company_vacancies_efin['items']:
    list_url.append(i['url'])
for i in company_vacancies_psb['items']:
    list_url.append(i['url'])
for i in company_vacancies_tbank['items']:
    list_url.append(i['url'])
for i in company_vacancies_sovcombank['items']:
    list_url.append(i['url'])
for i in company_vacancies_pao['items']:
    list_url.append(i['url'])
for i in company_vacancies_bsk['items']:
    list_url.append(i['url'])
for i in company_vacancies_otp['items']:
    list_url.append(i['url'])
for i in company_vacancies_bks['items']:
    list_url.append(i['url'])


# Название компании
name_alfa = [company_alfa['name']]
name_company_alfa = [(i,) for i in name_alfa]  # преобразование данных в форамат: [('Альфа-Банк',)]
name_vtb = [company_vtb['name']]
name_company_vtb = [(i,) for i in name_vtb]
name_efin = [company_efin['name']]
name_company_efin = [(i,) for i in name_efin]
name_psb = [company_psb['name']]
name_company_psb = [(i,) for i in name_psb]
name_tbank = [company_tbank['name']]
name_company_tbank = [(i,) for i in name_tbank]
name_sovcombank = [company_sovcombank['name']]
name_company_sovcombank = [(i,) for i in name_sovcombank]
name_pao = [company_pao['name']]
name_company_pao = [(i,) for i in name_pao]
name_bsk = [company_bsk['name']]
name_company_bsk = [(i,) for i in name_bsk]
name_otp = [company_otp['name']]
name_company_otp = [(i,) for i in name_otp]
name_bks = [company_bks['name']]
name_company_bks = [(i,) for i in name_bks]


# Добавление в список id компании Альфа
list_id_company = []
list_test = []
for i in company_vacancies_alfa['items']:
     data = i['department']['id']
     list_id_company.append(data[0:2])
for i in company_vacancies_vtb['items']:
     data = i['department']['id']
     list_id_company.append(data[4:8])
for i in company_vacancies_efin['items']:
     data = i['employer']['id']
     list_id_company.append(data)
for i in company_vacancies_psb['items']:
     data = i['employer']['id']
     list_id_company.append(data)
for i in company_vacancies_tbank['items']:
     data = i['employer']['id']
     list_id_company.append(data)
for i in company_vacancies_sovcombank['items']:
     data = i['employer']['id']
     list_id_company.append(data)
for i in company_vacancies_pao['items']:
     data = i['employer']['id']
     list_id_company.append(data)
for i in company_vacancies_bsk['items']:
     data = i['employer']['id']
     list_id_company.append(data)
for i in company_vacancies_otp['items']:
     data = i['employer']['id']
     list_id_company.append(data)
for i in company_vacancies_bks['items']:
     data = i['employer']['id']
     list_id_company.append(data)


# Соединение всех списков в один
result_list = list(zip(list_id, list_id_company, list_name, list_salary, list_currency, list_url))



