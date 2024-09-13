import mysql.connector
import os
from dotenv import load_dotenv
from pathlib import Path
import sys

env_path = str(Path(__file__).absolute().parents[1] / "config.env")
load_dotenv(env_path)

sys.path.append(os.environ.get("API_PATH"))


def get_mysql_connection():
    conn_string = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"), port=os.getenv("MYSQL_PORT"), user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"), db=os.getenv("MYSQL_DB"), )
    return conn_string


def get_result(query):
    mysql_conn = get_mysql_connection()
    cursor_str = mysql_conn.cursor()
    cursor_str.execute(query)
    row = cursor_str.fetchall()
    field_names = [i[0] for i in cursor_str.description]
    mysql_conn.close()
    return row, field_names


def put_result(query, data):
    mysql_conn = get_mysql_connection()
    cursor_str = mysql_conn.cursor()
    cursor_str.execute(query, data)
    mysql_conn.commit()
    mysql_conn.close()
    return cursor_str.rowcount


def exec_qry(query):
    mysql_conn = get_mysql_connection()
    cursor_str = mysql_conn.cursor()
    cursor_str.execute(query)
    mysql_conn.commit()
    mysql_conn.close()
    return cursor_str.rowcount


def call_proc(proc, params):
    mysql_conn = get_mysql_connection()
    cursor_login = mysql_conn.cursor()
    cur_res = cursor_login.callproc(proc, params)
    mysql_conn.commit()
    return cur_res
