import os
import psycopg2

url = "dbname = 'd8osr4jq6ahd25' host = 'ec2-54-204-36-249.compute-1.amazonaws.com' port = '5432'\
     user = 'jkaegobpsrhntk' password = 'ee912001d1be919a6e88385a69e75f54f4c757ca9ca5293ea25e28b29d267148'"


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
    conn = connection(url)
    curr = conn.cursor()
    parcels = """DROP TABLE IF EXISTS Parcels_table CASCADE;"""
    users = """DROP TABLE IF EXISTS Users_table CASCADE;"""
    queries = [users, parcels]
    for query in queries:
        curr.execute(query)
    conn.commit


def tables():
    users = """CREATE TABLE IF NOT EXISTS Users_table (
    userid VARCHAR (256) PRIMARY KEY,
    name  VARCHAR (256) NOT NULL,
    role VARCHAR (256) NOT NULL DEFAULT 'user',
    email VARCHAR (256) NOT NULL UNIQUE,
    phone VARCHAR (256) NOT NULL UNIQUE,
    password VARCHAR (256) NOT NULL,
    username VARCHAR (256) NOT NULL
    );

    """

    parcels = """CREATE TABLE IF NOT EXISTS Parcels_table (
    parcelid VARCHAR (256) PRIMARY KEY,
    weight VARCHAR (256) NOT NULL,
    destination VARCHAR (256) NOT NULL,
    sender VARCHAR (256) NOT NULL,
    recipient VARCHAR (256) NOT NULL,
    status VARCHAR (256) NOT NULL DEFAULT 'Pending Delivery',
    price VARCHAR (256) NOT NULL,
    userid VARCHAR (256) NOT NULL
    );"""

    queries = [users, parcels]
    return queries