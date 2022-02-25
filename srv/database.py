import os
from contextlib import contextmanager

import psycopg2


@contextmanager
def connect_database():
    conn = psycopg2.connect(
        host="db",
        database=os.environ["POSTGRES_DB"],
        user=os.environ["POSTGRES_USER"],
        password=os.environ["POSTGRES_PASSWORD"],
        port="5432",
    )

    try:
        yield conn
    finally:
        conn.close()


def create_circle_table(conn):
    cur = conn.cursor()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS circles (id uuid PRIMARY KEY, colour text, x float4, y float4, r float4, created_at timestamp with time zone);"
    )
    conn.commit()


def create_rect_table(conn):
    cur = conn.cursor()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS rectangles (id uuid PRIMARY KEY, colour text, x float4, y float4, w float4, h float4, created_at created_at timestamp with time zone);"
    )
    conn.commit()


def get_circles(conn, beg_time, end_time):
    curr = conn.cursor()

    query = build_time_query(beg_time, end_time)

    curr.execute(f"SELECT * FROM circles{query}")

    circles = curr.fetchall()

    return circles


def get_rectangles(conn, beg_time, end_time):
    curr = conn.cursor()

    query = build_time_query(beg_time, end_time)


    curr.execute(f"SELECT * FROM rectangles{query}")

    rectangles = curr.fetchall()

    return rectangles

def build_time_query(beg_time, end_time):
    if beg_time is None and end_time is None:
        return ""
    elif beg_time is None:
        return f" WHERE created_at<={end_time}"
    elif end_time is None:
        return f" WHERE created_at>={beg_time}"
    else: 
        return f" WHERE created_at BETWEEN {beg_time} AND {end_time}"


def insert_rect(conn, rect):
    curr = conn.cursor()

    curr.execute(
        f"INSERT INTO rectangles VALUES ('{rect['id']}', '{rect['colour']}', '{rect['x']}', '{rect['y']}', '{rect['w']}', '{rect['h']}', CURRENT_TIMESTAMP);"
    )
    conn.commit()


def insert_circle(conn, circle):
    curr = conn.cursor()

    curr.execute(
        f"INSERT INTO circles VALUES ('{circle['id']}', '{circle['colour']}', '{circle['x']}', '{circle['y']}', '{circle['r']}', CURRENT_TIMESTAMP);"
    )
    conn.commit()


def del_rect(conn, id):
    curr = conn.cursor()

    curr.execute(f"DELETE FROM rectangles WHERE id={id}")
    conn.commit()


def del_circle(conn, id):
    curr = conn.cursor()

    curr.execute(f"DELETE FROM circles WHERE id={id}")
    conn.commit()
