import re
import os
import json

from dbhelper import Dbhelper


# 自定义web应用
class Application:

    def __init__(self):
        self.url_map = {}  # 路由规则对照字典


    # 可调用对象,必须实现call魔术方法
    def __call__(self, environ, start_response):
        self.environ = environ
        self.start_response = start_response
        # start_response('200 ok', [('Content-Type', 'text/html')])
        path = environ['PATH_INFO']
        # print(path)
        # print(environ["QUERY_STRING"])
        # 路由: 把用户请求和对应处理函数关联,根据请求自动调用处理函数
        for pattern, func in self.url_map.items():
            # print(self.url_map)
            res = re.match(pattern, path)
            if res:
                if len(res.groups())>0:
                    return func(*res.groups())
                return func()
        # print(self.url_map)
        # 返回响应体,必须是可迭代对象
        start_response('200 ok', [('Content-Type', 'text/html')])
        return [b'File Not Found']

    # 路由装饰器
    def route(self,rule):
        def inner(func):
            nonlocal rule
            if re.match(r'/static',rule):
                rule = '^' + rule
            else:
                rule = '^' + rule + '$'
            rule = re.sub(r'<\w+>','(\w+)',rule)
            print(rule)
            # 添加路由规则
            self.url_map[rule] = func
        return inner


#   web应用
app = Application()

from view import *

