import psycopg2
from typing import List, Tuple, Union
from src.hh_vacansy import (result_list_vacancies, result_list_employees)

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
        vacancies VARCHAR(255),
        salary int,
        currency VARCHAR,
        url VARCHAR
    );
""")
cur.execute(f"""
    DROP TABLE employees;
    CREATE TABLE employees (
        employees_id SERIAL PRIMARY KEY,
        company VARCHAR
    );
""")
conn.commit()


class DBManager:
    with conn.cursor() as cursor:
        cursor.executemany("INSERT INTO employees (employees_id, company) VALUES (%s, %s)", result_list_employees)
        cursor.execute("ALTER TABLE vacancies ADD COLUMN employees_id INTEGER REFERENCES employees(employees_id)")
        cursor.executemany("INSERT INTO vacancies (vacancies_id, vacancies, salary, currency, url, employees_id) "
                               "VALUES (%s, %s, %s, %s, %s, %s)", result_list_vacancies)
        conn.commit()

    def __init__(self, host='localhost', database='test', user='postgres', password='12345'):
        self.conn = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )

    def get_all_vacancies(self) -> List[Tuple[int, str, Union[int, None], str, str, str]]:
        # получает список всех вакансий с указанием названия компании,
        # названия вакансии и зарплаты и ссылки на вакансию.
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT vacancies.vacancies_id, vacancies.vacancies, vacancies.salary, vacancies.currency,"
                           " vacancies.url, employees.company AS company FROM vacancies JOIN employees "
                           "ON vacancies.employees_id = employees.employees_id;")
            rows = cursor.fetchall()
            return rows

    def get_companies_and_vacancies_count(self) -> List[Tuple[str, int]]:
        # получает список всех компаний и количество вакансий у каждой компании
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT employees.company, COUNT(*) AS vacancies FROM vacancies JOIN employees "
                           "ON vacancies.employees_id = employees.employees_id GROUP BY company")
            self.conn.commit()
            rows = cursor.fetchall()
            return rows

    def get_avg_salary(self) -> List[Tuple[Union[float, None]]]:
        # получает среднюю зарплату по вакансиям
        with self.conn.cursor() as cursor:
            cursor.execute('SELECT AVG(salary) AS avg_salary FROM vacancies')
            self.conn.commit()
            rows = cursor.fetchall()
            return rows

    def get_vacancies_with_higher_salary(self) -> List[Tuple]:
        # получает список всех вакансий, у которых зарплата выше средней по всем вакансиям
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT * FROM vacancies WHERE salary::numeric > (SELECT AVG(salary::numeric) "
                           "FROM vacancies)")
            self.conn.commit()
            rows = cursor.fetchall()
            return rows

    def get_vacancies_with_keyword(self) -> List[Tuple]:
        #  получает список всех вакансий, в названии которых содержатся переданные в метод слова
        keyword = input("Введите название вакансии для поиска: ")
        with self.conn.cursor() as cursor:
            cursor.execute(f"SELECT * FROM vacancies WHERE vacancies LIKE '{keyword}%'")
            self.conn.commit()
            rows = cursor.fetchall()
            return rows

