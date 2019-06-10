from Application import app
import re
import os
import json

from dbhelper import Dbhelper

@app.route('/')
def index():
    data = b"Not Found"
    with open('template/index.html', 'rb') as fp:
        data = fp.read()
    app.start_response("200 ok", [('Content-Type', 'text/html')])
    return [data]

@app.route('/showprovince')
def index():
    data = b"Not Found"
    with open('template/province.html', 'rb') as fp:
        data = fp.read()
    app.start_response("200 ok", [('Content-Type', 'text/html')])
    return [data]

@app.route('/timer')
def index():
    data = b"Not Found"
    with open('template/秒表.html', 'rb') as fp:
        data = fp.read()
    app.start_response("200 ok", [('Content-Type', 'text/html')])
    return [data]

@app.route('/static')
def load_static():
    path = app.environ.get('PATH_INFO','/').lstrip('/')
    data = b"not found"
    if os.path.exists(path):
        with open(path,'rb') as fp:
            data = fp.read()
        # 获取文件后缀名
        ext = os.path.splitext(path)
        if len(ext)>1:
            ext = ext[1].lstrip('.')  # 有后缀名
        else:
            ext = 'html'  # 没有默认是html
        ct = {
            'jpeg':'image/jpeg',
            'jpg':'image/jpeg',
            'bmp':'image/bmp',
            'png':'image/png',
            'css':'text/css',
            'js':'application/x-javascript',
            'html':'text/html'
        }
        app.start_response("200 ok",[('Content-Type',ct[ext])])
    else:
        app.start_response("200 ok", [('Content-Type', 'text/html')])
    return [data]

@app.route('/province')
def province():
    db = Dbhelper('areainfo')
    res = db.where(pid=0).select()
    print(res)
    app.start_response("200 ok",[('Content-Type','application/json')])
    return [json.dumps(res).encode("utf-8")]

@app.route('/city/<value>')
def city(value):
    db = Dbhelper('areainfo')
    res = db.where(pid=value).select()
    app.start_response("200 ok", [('Content-Type', 'application/json')])
    return [json.dumps(res).encode("utf-8")]