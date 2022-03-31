from boto.s3.connection import S3Connection

import os
import psycopg2
import sys
import uuid


#secret link no one can find out!
DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cur = conn.cursor() 

def get_menu_all():
    s = "select * from restbestmenu;"
    cur.execute(s)
    table = cur.fetchall()
    conn.commit()
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
    print("")
    print("")
    print("")
    print(table)
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


def exec_delete_items(table_id, item_id, amount):
    s = """ 
        DELETE FROM restbesttables
        WHERE id  IN (
            SELECT id 
            FROM restbesttables rt
            WHERE rt.table_id = %s
            AND rt.item_id = %s
            limit %s) 
        """ %(table_id,item_id,amount )
    print(s)
    cur.execute(s)
    conn.commit()
    return s

        

def delete_items(og_list, dif_list):
    n_og_list = []

    for x in og_list:
        for n in og_list[x]:
            a = n[0]
            b = n[5]
            t = (x,a,b)
            n_og_list.append(t)
    print("")
    print("")
    print("")
    print("this is n_og_list")
    print(n_og_list)


    n_dif_list = []
    if "Submit" in dif_list:
        del dif_list['Submit']
    for x in dif_list:
        c = dif_list[x]
        x = x.split(", ")
        t = (x[0],int(x[1]),int(c))
        n_dif_list.append(t)

    print("")
    print("")
    print("this is n_dif_list")
    print(n_dif_list)

 

    items = []
    for a in n_og_list:
        for b in n_dif_list:
            if a[0] == b[0] and a[1] == b[1] and a[2] != b[2]:
                t = (a[0],str(a[1]),str(a[2]-b[2]))
                items.append(t)

    print("")
    print("")
    print("")
    print("items to delete")
    print(items)

    for x in items:
        table_id = x[0]
        item_id = x[1]
        amount = x[2]
        exec_delete_items(table_id,item_id,amount)


    