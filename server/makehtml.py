#!/usr/bin/env python
#coding:utf-8
import sqlite3
import os,sys
reload(sys)
sys.setdefaultencoding('utf-8')
from bottle import template

basedir=os.path.dirname(os.path.abspath(__file__))
html=basedir+"/static/pimark.htm"
html2=basedir+"/static/gmpimark.htm"
html3=basedir+"/static/mtgmpimark.htm"
html4=basedir+"/static/armpimark.htm"

def makehtml():
    db=sqlite3.connect("pimark.db")
    cur=db.execute("select * from pimark order by PIC asc")
    res=cur.fetchall()
    output=template("makehtml",rows=res,pi="C")
    if os.path.exists(html):
        os.remove(html)

    fi=open(html,'wb')
    fi.write(output)
    fi.close()
    print("::make html1 ok")
    
    cur=db.execute("select * from pimark order by GMPI asc")
    res=cur.fetchall()
    output=template("makehtml",rows=res,pi="GMP")
    if os.path.exists(html2):
        os.remove(html2)

    fi=open(html2,'w')
    fi.write(output)
    fi.close()
    print("::make html2 ok")

    cur=db.execute("select * from pimark where USER is not null order by MTGMPI asc")
    res=cur.fetchall()
    output=template("makehtml",rows=res,pi="MtGMP")
    if os.path.exists(html3):
        os.remove(html3)

    fi=open(html3,'w')
    fi.write(output)
    fi.close()
    print("::make html3 ok")

    cur=db.execute("select * from pimark where GCC like '%arm%' order by GMPI asc")
    res=cur.fetchall()
    output=template("makehtml",rows=res,pi="ARMGMP")
    if os.path.exists(html4):
        os.remove(html4)

    fi=open(html4,'w')
    fi.write(output)
    fi.close()
    print("::make html4 ok")








if __name__=="__main__":
    makehtml()
