#!/usr/bin/env python
#encode=utf8
from gevent import monkey
monkey.patch_all()
from bottle import run,request,post,route,get
import xml.etree.ElementTree as xmlet
import os
import bottle

@route('/<name>')
def static(name):
    print("Get some request" ,name)
    if name=='pimark.htm' or name=='gmpimark.htm' or name=='mtgmpimark.htm':
        return bottle.static_file(name,root='/myblog/public')
    if name=='favicon.ico':
        return bottle.static_file(name,root='/myblog/public')

@route('/')
def index():
    return bottle.static_file('pimark.htm',root='/myblog/public')

@get('/weixin')
def weiget():
    print (request.query_string)
    return request.query['echostr']

@post('/weixin')
def weipost():
    revstr=request.body.read()
    msg=xmlet.fromstring(revstr)
    for i in msg:
        if i.tag=='Content':
            print(i.text.encode('utf8'))
            print(i.tag)

    return "success"



run(host="0.0.0.0",port=80,server='gevent',reloader=True)
