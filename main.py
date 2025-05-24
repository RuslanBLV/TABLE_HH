from src.hh_api import DBManager
import psycopg2

conn = psycopg2.connect(
    host='localhost',
    database='test',
    user='postgres',
    password='12345',
)
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS employers (
        employer_id SERIAL PRIMARY KEY,
        employer VARCHAR(255),
        url VARCHAR
    )
""")
conn.commit()

cur.close()
conn.close()

