import datetime
import time
import psycopg2
import os
import sys

def get_url() ->  str:
    # url = os.getenv("DATABASE_URL", None)
    url = os.environ["DATABASE_URL"]
    if url is None:
        print("must set DATABASE URL")
        sys.exit(1)

    return url

def get_connection():
    url = get_url()
    con = psycopg2.connect(url)

    return con

def create_table_name(year: int, month: int) -> str:
    table_name = "log_" + str(year) + "_" + str(month)

    return table_name

def create_table(table_name: str) -> None:

    with get_connection() as con:
        with con.cursor() as cur:
            cur.execute("CREATE TABLE IF NOT EXISTS {} (id serial primary key, money int, \
                        day int, category text, remarks text, posted_at timestamp)".format(table_name))


def drop_table(table_name: str) -> None:

    with get_connection() as con:
        with con.cursor() as cur:
            cur.execute("DROP TABLE IF EXISTS {}".format(table_name))

def insert_data(category: str, table_name: str, money: int,
                day: int, remarks: str) -> None:

    with get_connection() as con:
        with con.cursor() as cur:
            cur.execute("INSERT INTO {} (money, day, category, remarks) \
                        VALUES ({}, {}, {}, {})".format(table_name, money, day, category, remarks))
