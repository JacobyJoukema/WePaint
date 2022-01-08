from contextlib import contextmanager

import psycopg2
import os
    
@contextmanager
def connect_database():
    conn = psycopg2.connect(
        host="localhost",
        database="wepaint",
        user="wepaint",
        password=os.getenv("DB_PASS"),
        port="5432")

    try:
        yield conn
    finally:
        conn.close()

def create_circle_table(conn):
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS circles (id uuid PRIMARY KEY, colour text, x float4, y float4, r float4);')
    conn.commit()

def create_rect_table(conn):
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS rectangles (id uuid PRIMARY KEY, colour text, x float4, y float4, w float4, h float4);')
    conn.commit()


def get_circles(conn):
    curr = conn.cursor()

    curr.execute("SELECT * FROM circles")

    circles = curr.fetchall()

    return (circles)

def get_rectangles(conn):
    curr = conn.cursor()

    curr.execute("SELECT * FROM rectangles")

    rectangles = curr.fetchall()

    return (rectangles)

def insert_rect(conn, rect):
    curr = conn.cursor()

    curr.execute(f"INSERT INTO rectangles VALUES ('{rect['id']}', '{rect['colour']}', '{rect['x']}', '{rect['y']}', '{rect['w']}', '{rect['h']}');")
    conn.commit()

def insert_circle(conn, circle):
    curr = conn.cursor()

    curr.execute(f"INSERT INTO circles VALUES ('{circle['id']}', '{circle['colour']}', '{circle['x']}', '{circle['y']}', '{circle['r']}');")
    conn.commit()


def del_rect(conn, id):
    curr = conn.cursor()

    curr.execute(f"DELETE FROM rectangles WHERE id={id}")
    conn.commit()


def del_circle(conn, id):
    curr = conn.cursor()

    curr.execute(f"DELETE FROM circles WHERE id={id}")
    conn.commit()
