import sqlite3
import os
from bottle import template
html="index.html"
def makehtml():
    db=sqlite3.connect("test.db")
    cur=db.execute("select * from pimark order by PIC asc")
    res=cur.fetchall()
    output=template("makehtml",rows=res)
    if os.path.exists(html):
        os.remove(html)

    fi=open(html,'w')
    fi.write(output)
    fi.close()
    print("::make html ok")





if __name__=="__main__":
    makehtml()
