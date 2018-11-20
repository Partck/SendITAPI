import os
import psycopg2

"""
url = "dbname = 'd8osr4jq6ahd25' host = 'ec2-54-204-36-249.compute-1.amazonaws.com' port = '5432'\
     user = 'jkaegobpsrhntk' password = 'ee912001d1be919a6e88385a69e75f54f4c757ca9ca5293ea25e28b29d267148'"
"""

url = "dbname = 'senditdb' host = 'localhost' port = '5432'\
     user = 'sendit_user' password = 'qwerty'"


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