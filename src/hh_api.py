import psycopg2
from typing import List, Tuple, Union
from src.hh_vacansy import api_vacancies, api_employees
from dotenv import load_dotenv
import os
import sqlite3

load_dotenv()


def recreate_database_postgres():
    dbname = os.getenv('database')
    user = os.getenv('user')
    password = os.getenv('password')
    host = os.getenv('host')


    conn = psycopg2.connect(
        host=host,
        database="postgres",
        user=user,
        password=password
    )
    conn.autocommit = True
    cur = conn.cursor()

    try:
        cur.execute(f"SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE datname='{dbname}';")
        cur.execute(f"DROP DATABASE IF EXISTS {dbname};")
    except Exception as ex:
        print(f"Ошибка при удалении базы: {ex}")

    cur.execute(f"CREATE DATABASE {dbname};")
    cur.close()
    conn.close()
    return f"База данных {dbname} успешно пересоздана."


def create_table():
    conn = psycopg2.connect(
        host=os.getenv('host'),
        database=os.getenv('database'),
        user=os.getenv('user'),
        password=os.getenv('password')
    )
    cur = conn.cursor()

    cur.execute(f"""
        CREATE TABLE employees (
            employees_id SERIAL PRIMARY KEY,
            company VARCHAR
        );
    """)

    cur.execute(f"""
        CREATE TABLE vacancies (
            vacancies_id SERIAL PRIMARY KEY,
            description VARCHAR(255),
            salary int,
            currency VARCHAR,
            url VARCHAR,
            employees_id INT,
            FOREIGN KEY (employees_id) REFERENCES employees (employees_id)
        );
    """)
    return "Таблица создана"


def info_table():
    conn = psycopg2.connect(
        host=os.getenv('host'),
        database=os.getenv('database'),
        user=os.getenv('user'),
        password=os.getenv('password')
    )

    with conn.cursor() as cursor:
        vacancies = api_vacancies()
        employees = api_employees()
        cursor.execute(f"""
                CREATE TABLE employees (
                    employees_id SERIAL PRIMARY KEY,
                    company VARCHAR
                );
            """)
        cursor.execute(f"""
                CREATE TABLE vacancies (
                    vacancies_id SERIAL PRIMARY KEY,
                    description VARCHAR(255),
                    salary int,
                    currency VARCHAR,
                    url VARCHAR,
                    employees_id INT,
                    FOREIGN KEY (employees_id) REFERENCES employees (employees_id)
                );
            """)
        cursor.executemany("INSERT INTO employees (employees_id, company) VALUES (%s, %s)", employees)
        cursor.executemany("INSERT INTO vacancies (vacancies_id, description, salary, currency, url, employees_id) "
                           "VALUES (%s, %s, %s, %s, %s, %s)", vacancies)
        conn.commit()

    conn.commit()
    return "В таблицу внесены данные"


class DBManager:

    def __init__(self, host=os.getenv('host'), database=os.getenv('database'), user=os.getenv('user'),
                 password=os.getenv('password')):
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
            cursor.execute("SELECT vacancies.vacancies_id, vacancies.description, vacancies.salary, vacancies.currency,"
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
            cursor.execute(f"SELECT * FROM vacancies WHERE description LIKE '%{keyword}%'")
            self.conn.commit()
            rows = cursor.fetchall()
            return rows


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

