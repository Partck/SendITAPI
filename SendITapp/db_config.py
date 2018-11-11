import os
import psycopg2

host = "localhost"
user = "pyper"
db_name = "SendIT_db"
password = "QWERTY"
port = 5432

url = "host ={} user = {}, pasword, port"
con = psycopg2.connect(url)
cur = con.cursor()
cursor.execute(sql)


def connection(url):
    con = psycopg2.connect(url)
    return con


def init_db():
    con = connection(url)
    return con

def create_tables():
    conn = connection(url)
    cursor = conn.cursor()
    queries = tables()
    for query in queries:
        cursor.execute(query)
    conn.commit()


def destroy_tables():
    pass


def tables():
    pass