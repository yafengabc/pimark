#!/usr/bin/env python3
import MySQLdb
import os
from bottle import template
from sae.const import MYSQL_DB,MYSQL_USER,MYSQL_PASS,MYSQL_HOST,MYSQL_PORT
import sae.kvdb

html="pimark.htm"
html2="gmpimark.htm"
html3="mtgmpimark.htm"

def makehtml():
    db=MySQLdb.connect(MYSQL_HOST,MYSQL_USER,MYSQL_PASS,MYSQL_DB,int(MYSQL_PORT))
    #cur=db.execute("select * from pimark order by PIC asc")
    cur=db.cursor()
    cur.execute("select * from pimark order by PIC asc")
    res=cur.fetchall()
    output=template("makehtml",rows=res,pi="C")

    kv=sae.kvdb.Client()
    kv.set(html,output)
    print("::make html1 ok")
    
    cur.execute("select * from pimark order by GMPI asc")
    res=cur.fetchall()
    output=template("makehtml",rows=res,pi="GMP")
    kv=sae.kvdb.Client()
    kv.set(html2,output)
    print("::make html2 ok")

    cur.execute("select * from pimark order by MTGMPI asc")
    res=cur.fetchall()
    output=template("makehtml",rows=res,pi="MtGMP")
    kv=sae.kvdb.Client()
    kv.set(html3,output)
    print("::make html3 ok")
    
    fi=open('index.htm')
    res=fi.readlines()
    kv.set('index.htm',res)

if __name__=="__main__":
    makehtml()
