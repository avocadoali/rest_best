import os
import psycopg2
import sys
import uuid

#secret link no one can find out!
DATABASE_URL = 'postgres://nhukilfdhxrgfd:a6a0114dfb6998f09a3eb29c86c659734cf32c07d6f29545998fdd104a1c2195@ec2-54-158-26-89.compute-1.amazonaws.com:5432/d9n45ft7eb89d7'
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cur = conn.cursor() 

def get_menu_all():
    s = "select * from restbestmenu;"
    print("vor cur")
    cur.execute(s)
    table = cur.fetchall()
    conn.commit()
    print(table)
    return table

def get_menu_by_id(id):
    s = "select * from restbestmenu where id = " + id[0]
    for i in id:
        s = " or id=" + i

    print("vor cur")
    cur.execute(s)
    table = cur.fetchall()
    conn.commit()
    print(table)
    return table


