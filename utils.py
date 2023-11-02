import string
import random


def generate_password(length: int = 10) -> str:
    chars = string.ascii_letters + string.digits

    result = ''
    for _ in range(length):
        result += random.choice(chars)

    return result


def commit_sql(sql: str):
    import sqlite3

    try:
        con = sqlite3.connect('example.db')
        cur = con.cursor()
        cur.execute(sql)
        con.commit()
    finally:
        con.close()
