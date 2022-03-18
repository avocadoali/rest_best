import os
import psycopg2
import sys
import uuid

#secret link no one can find out!
DATABASE_URL = 'postgres://fsumbsrgaxtlat:de8f16f61b254200811418117061c4e5088dd3cd6c10fd7fc24f6ceaeaa1b321@ec2-63-32-7-190.eu-west-1.compute.amazonaws.com:5432/d7fgtf7tf4shmh'
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cur = conn.cursor() 

def test():
    s = "select * from restbest;"
    print("vor cur")
    cur.execute(s)
    table = cur.fetchall()
    conn.commit()
    print(table)
    return table
