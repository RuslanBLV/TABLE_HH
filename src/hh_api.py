import psycopg2
import requests
from src.hh_vacansy import (result_list, name_company_alfa, name_company_vtb, name_company_efin, name_company_psb,
                            name_company_tbank, name_company_sovcombank, name_company_pao, name_company_bsk,
                            name_company_otp, name_company_bks)

conn = psycopg2.connect(
    host='localhost',
    database='test',
    user='postgres',
    password='12345',
    options='-c client_encoding=UTF8'
)
cur = conn.cursor()

cur.execute(f"""
    DROP TABLE vacancies;
    CREATE TABLE vacancies (
        vacancies_id SERIAL PRIMARY KEY,
        company_id int,
        company VARCHAR,
        vacancies VARCHAR(255),
        salary int,
        currency VARCHAR,
        url VARCHAR
    );
""")
conn.commit()


class DBManager:
    def __init__(self, host='localhost', database='test', user='postgres', password='12345'):
        self.conn = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )

    def get_all_vacancies(self):
        with self.conn.cursor() as cursor:
            cursor.executemany("INSERT INTO vacancies (vacancies_id, company_id, vacancies, salary, currency, url) "
                               "VALUES (%s, %s, %s, %s, %s, %s)", result_list)
            cursor.executemany("UPDATE vacancies SET company = %s WHERE company_id = 80", name_company_alfa)
            cursor.executemany("UPDATE vacancies SET company = %s WHERE company_id = 4181", name_company_vtb)
            cursor.executemany("UPDATE vacancies SET company = %s WHERE company_id = 8643040", name_company_efin)
            cursor.executemany("UPDATE vacancies SET company = %s WHERE company_id = 6591", name_company_psb)
            cursor.executemany("UPDATE vacancies SET company = %s WHERE company_id = 78638", name_company_tbank)
            cursor.executemany("UPDATE vacancies SET company = %s WHERE company_id = 7944", name_company_sovcombank)
            cursor.executemany("UPDATE vacancies SET company = %s WHERE company_id = 89", name_company_pao)
            cursor.executemany("UPDATE vacancies SET company = %s WHERE company_id = 3003159", name_company_bsk)
            cursor.executemany("UPDATE vacancies SET company = %s WHERE company_id = 4394", name_company_otp)
            cursor.executemany("UPDATE vacancies SET company = %s WHERE company_id = 1833", name_company_bks)
            self.conn.commit()
            cursor.execute("SELECT * FROM vacancies")
            rows = cursor.fetchall()
            return rows

    def get_companies_and_vacancies_count(self):
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT company, COUNT(*) AS vacancies FROM vacancies "
                           "GROUP BY company")
            self.conn.commit()

            rows = cursor.fetchall()
            return rows

    def get_avg_salary(self):
        with self.conn.cursor() as cursor:
            cursor.execute('SELECT AVG(salary) AS avg_salary FROM vacancies')
            self.conn.commit()

            rows = cursor.fetchall()
            return rows

    def get_vacancies_with_higher_salary(self):
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT * FROM vacancies WHERE salary::numeric > (SELECT AVG(salary::numeric) "
                           "FROM vacancies)")
            self.conn.commit()

            rows = cursor.fetchall()
            return rows


i = DBManager()
print(i.get_all_vacancies())
print(i.get_companies_and_vacancies_count())
print(i.get_avg_salary())
print(i.get_vacancies_with_higher_salary())
