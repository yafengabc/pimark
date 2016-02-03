#!/usr/bin/python
# -*- coding:utf-8 -*-  
from bottle import Bottle, run,debug
from bottle import post,request,run,debug,route
import json
import traceback

import makehtml
import MySQLdb
from sae.const import MYSQL_DB,MYSQL_USER,MYSQL_PASS,MYSQL_HOST,MYSQL_PORT
app = Bottle()

@app.get('/:name')
def pimark(name):
    import sae.kvdb
    kv=sae.kvdb.Client()
    return kv.get(name)

@app.get('/')
def index():
    import bottle
    bottle.redirect('/index.htm')

def insertdb(dat):
        print("open the datebase")
        #db=sqlite3.connect("test.db")
        conn=MySQLdb.connect(MYSQL_HOST,MYSQL_USER,MYSQL_PASS,MYSQL_DB,int(MYSQL_PORT))
        db=conn.cursor()
        print("insert into database")
        print (dat)
        dat=dat.replace("'",'"')
        dat=json.loads(dat)
        print (dat)
        if dat["USER"]:
            db.execute("insert into pimark values ('%s','%s','%s','%s','%s','%s','%s','%s')" \
                    %(dat["CPU"],dat["HW"],dat["kernel"],dat["GCC"],dat["PIC"],dat["GMPI"],dat["MTGMPI"],dat["USER"]))
            conn.commit()
        else:
            db.execute("insert into pimark values('%s','%s','%s','%s','%s','%s','%s','%s')" \
                %(dat["CPU"],dat["HW"],dat["kernel"],dat["GCC"],dat["PIC"],dat["GMPI"],"",""))
            db.commit()

@app.post('/send')
def postd():
    try:
        data=request.body
        datas=data.read().decode('utf-8')
        print(datas)
        insertdb(datas)
        makehtml.makehtml()
        return "Post OK\n" 
    except:
        return traceback.format_exc()

@app.get("/install")
def static():
    try:
        import sae.kvdb
        kv=sae.kvdb.Client()
        fi=open('index.htm')
        res=fi.readlines()
        kv.set('index.htm',res)
        fi=open('favicon.ico','rb')
        res=fi.read()
        kv.set('favicon.ico',res)
        fi=open('favicon.gif','rb')
        res=fi.read()
        kv.set('favicon.gif',res)
        return "Installed OK"
    except:
        return traceback.format_exc()




