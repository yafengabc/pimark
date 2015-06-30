from bottle import post,request,run,debug,route
import json
import sqlite3

def insertdb(dat):
    print("open the datebase")
    db=sqlite3.connect("test.db")
    print("insert into database")
    print (dat)
    dat=dat.replace("'",'"')
    dat=json.loads(dat)
    print (dat)
    db.execute("insert into pimark values(?,?,?,?,?,?)",\
            (dat["CPU"],dat["HW"],dat["kernel"],dat["GCC"],dat["PIC"],dat["GMPI"]))
    db.commit()
    pass

def makehtml():
    pass

@route('/')
def index():
    a="asd"
    b="ddd"
    return "hello kitty ? ?"

@post('/send')
def postd():
    data=request.body
    datas=data.read().decode('utf-8')
    print(datas)
    insertdb(datas)
    makehtml()
    return "Post OK\n" 

run(server="paste",host="0.0.0.0")
#run(host="0.0.0.0",debug=True)
