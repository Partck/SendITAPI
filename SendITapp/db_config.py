import os
import psycopg2
class DbConfig:
    def __init__(self):
        self.url = os.getenv("URL")
              
    def connection(self, url):
        con = psycopg2.connect(url)
        return con


    def init_db(self):
        con = self.connection(self.url)
        return con


    def create_tables(self):
        conn = self.connection(self.url)
        cursor = conn.cursor()
        queries = self.tables()
        for query in queries:
            cursor.execute(query)
        conn.commit()


    def destroy_tables(self):
        conn = self.connection(self.url)
        curr = conn.cursor()
        parcels = """DROP TABLE IF EXISTS Parcels_table CASCADE;"""
        users = """DROP TABLE IF EXISTS Users_table CASCADE;"""
        queries = [users, parcels]
        for query in queries:
            curr.execute(query)
        conn.commit


    def tables(self):
        users = """CREATE TABLE IF NOT EXISTS Users_table (
        userid VARCHAR (256) PRIMARY KEY,
        name  VARCHAR (256) NOT NULL,
        role VARCHAR (256) NOT NULL DEFAULT 'user',
        email VARCHAR (256) NOT NULL,
        phone VARCHAR (256) NOT NULL,
        password VARCHAR (256) NOT NULL,
        username VARCHAR (256) NOT NULL
        );

        """

        parcels = """CREATE TABLE IF NOT EXISTS Parcels_table (
        parcelid VARCHAR (256) PRIMARY KEY,
        weight VARCHAR (256) NOT NULL,
        destination VARCHAR (256) NOT NULL,
        
        recipient VARCHAR (256) NOT NULL,
        status VARCHAR (256) NOT NULL DEFAULT 'Pending Delivery',
        price VARCHAR (256) NOT NULL,
        userid VARCHAR (256) NOT NULL
        );"""

        queries = [users, parcels]
        return queries