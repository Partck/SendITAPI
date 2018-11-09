import os
import psycopg2

host = "localhost"
user = "pyper"
db_name = "SendITdb"
password = "qwerty"
port = 5432

url = "host ={} user = {}, pasword, port"
con = psycopg2.connect(url)
cur = con.cursor()
sql = ""
cursor.execute(sql)

def connection(url):
   con = psycopg2.connect(url)
   return con

def init_db():
   con = connection(url)
   return con


def create_tables():
     con = connection(url)
     cur = con.cursor()
     queries = tables()
     for query in queries:
        cur.execute(query)
    con.commit()

def destroy_tables():
   pass

def tables():
    Users = ""
    Parcels = ""
    queries = [Users, Parcels]
    return queries
