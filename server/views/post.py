#!/usr/bin/env python

#import gevent.monkey
#gevent.monkey.patch_all()
from bottle import post,request,run,debug,route
import bottle
import json
import sqlite3
import makehtml
import sys
app=application=bottle.default_app()
def insertdb(dat):
    print("open the datebase")
    db=sqlite3.connect("/root/server/test.db")
    print("insert into database")
    print (dat)
    dat=dat.replace("'",'"')
    dat=json.loads(dat)
    print (dat)
    if dat["USER"]:
        db.execute("insert into pimark values(?,?,?,?,?,?,?,?)",\
                (dat["CPU"],dat["HW"],dat["kernel"],dat["GCC"],dat["PIC"],dat["GMPI"],dat["MTGMPI"],dat["USER"]))
        db.commit()
    else:
        db.execute("insert into pimark values(?,?,?,?,?,?,?,?)",\
                (dat["CPU"],dat["HW"],dat["kernel"],dat["GCC"],dat["PIC"],dat["GMPI"],"",""))
        db.commit()
    pass


@app.route('/')
def index():
    a="asd"
    b="ddd"
    return "hello kitty ? ?"

@app.post('/send')
def postd():
    data=request.body
    datas=data.read().decode('utf-8')
    print(datas)
    insertdb(datas)
    makehtml.makehtml()
    return "Post OK\n" 

@app.post('/commit')
def commit():
    print("This is the github.com post me some mmessage:")
    data=request.body
    datas=data.read()
    print(datas)
    return "Post OK\n" 


#run(server="paste",host="0.0.0.0")
run(server="gevent",host="0.0.0.0")
