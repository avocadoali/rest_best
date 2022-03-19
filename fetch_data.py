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

def submit_order_by_table(table_ID, item_ID):
    s = "INSERT INTO restbesttables (table_id, item_id) VALUES ( "
    s += table_ID 
    s += ","
    s += item_ID
    s += ");"
    print(s)
    cur.execute(s)
    conn.commit()
    return s


def handle_order_cart(table_ID, list_cart):
    for x in list_cart:
        n = list_cart[x][0]
        item_ID = x
        for i in range(int(n)):
            submit_order_by_table(table_ID, item_ID)


def get_order_of_table(table_ID):
    s = "with get_all as ("
    s +="SELECT rm.id as id, rm.name, rm.type,rm.price "
    s +="FROM restbesttables rt, restbestmenu rm "
    s +="where rt.table_id = "
    s +=table_ID
    s +=" and rm.id = rt.item_id "
    s +="), get_anz as ("
    s +="SELECT rm.id iddd, count(*) cnt "
    s +="FROM restbesttables rt, restbestmenu rm "
    s +="where rt.table_id = "
    s +=table_ID
    s +=" and rm.id = rt.item_id "
    s +="group by rm.id"
    s +=") "
    s +="select distinct * "
    s +="from get_all a, get_anz b "
    s +="where a.id = b.iddd;"
    cur.execute(s)
    table = cur.fetchall()
    conn.commit()
    return table

def get_overview_orders():
    list = get_distinct_table()
    dict = {}
    for x in list:
        temp =  get_order_of_table(x)
        dict[x] = temp
    return dict

def get_distinct_table():
    s = "select distinct(table_id) from restbesttables"
    cur.execute(s)
    table = cur.fetchall()
    conn.commit()
    list = []
    for x in table:
        list.append(str(x[0]))
    return list



