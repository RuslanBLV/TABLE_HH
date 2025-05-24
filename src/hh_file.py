# -*- coding: utf-8 -*-
import psycopg2
from src.hh_api import DBManager
id = DBManager()


conn = psycopg2.connect(
    host='localhost',
    database='test',
    user='postgres',
    password='12345',
    options='-c client_encoding=UTF8'
)
cur = conn.cursor()

cur.execute(f"""
    DROP TABLE employers;
    CREATE TABLE employers (
        employer_id SERIAL PRIMARY KEY,
        employer VARCHAR(255),
        url VARCHAR
    );
""")
cur.execute(f"""INSERT INTO employers (employer_id) VALUES ('1');
""")
conn.commit()

cur.close()
conn.close()
