#!/usr/bin/env python3
import sqlite3
import os
from bottle import template
html="pi.htm"
html2="gmpi.htm"

def makehtml():
    db=sqlite3.connect("test.db")
    cur=db.execute("select * from pimark order by PIC asc")
    res=cur.fetchall()
    output=template("makehtml",rows=res,pi="C")
    if os.path.exists(html):
        os.remove(html)

    fi=open(html,'w')
    fi.write(output)
    fi.close()
    print("::make html ok")
    
    cur=db.execute("select * from pimark order by GMPI asc")
    res=cur.fetchall()
    output=template("makehtml",rows=res,pi="GMP")
    if os.path.exists(html2):
        os.remove(html2)

    fi=open(html2,'w')
    fi.write(output)
    fi.close()
    print("::make html2 ok")






if __name__=="__main__":
    makehtml()
