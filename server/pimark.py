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
    db=sqlite3.connect("pimark.db")
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
def insertdb2():
    print("open the datebase")
    db=sqlite3.connect("pimark.db")
    print("insert into database")
    dat={}
    dat["CPU"]="CPU"
    dat["HW"]="CPU"
    dat["kernel"]="CPU"
    dat["GCC"]="CPU"
    dat["PIC"]="1000.0"
    dat["GMPI"]="1000.0"
    dat["MTGMPI"]="1000.0"
    dat["USER"]="debug"
    print (dat)
    if dat["USER"]:
        db.execute("insert into pimark values(?,?,?,?,?,?,?,?)",\
                (dat["CPU"],dat["HW"],dat["kernel"],dat["GCC"],dat["PIC"],dat["GMPI"],dat["MTGMPI"],dat["USER"]))
        db.commit()



@app.route('/test')
def index():
    #insertdb2() 
    return makehtml.makehtml()
#return "hello kitty ? ?"

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

if __name__=='__main__':
    #insertdb2()
    makehtml.makehtml()
    #run(server="paste",host="0.0.0.0")
    #run(server="gevent",host="0.0.0.0")

