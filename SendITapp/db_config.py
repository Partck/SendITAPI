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
sql = ""
cursor.execute(sql)



# Has methods
# connection
# init_db
# create_tables
# destroy_tables
# tables