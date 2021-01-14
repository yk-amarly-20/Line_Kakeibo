import datetime
import time
import psycopg2
import os
import sys

def get_url() ->  str:
    url = os.get_env('DATABASE_URL', None)
    if url is None:
        print("must set DATABASE URL")
        sys.exit(1)

    return url

def get_connection():
    url = get_url()
    con = psycopg2.connect(url)

    return con

def create_table(table_name: str) -> None:

    with get_connection() as con:
        with con.cursor() as cur:
            cur.execute("CREATE TABLE IF NOT EXISTS {} (id serial primary key, money int, \
                        day int, catrgory text, created_at timestamp)".format(table_name))


def drop_table(table_name: str) -> None:

    with get_connection() as con:
        with con.cursor() as cur:
            cur.execute("DROP TABLE IF EXISTS {}".format(table_name))
