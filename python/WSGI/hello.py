#!/user/env/bin python3
#-*- coding:utf-8 -*-

# hello.py

def applicaton(environ, start_response):
    start_response('200 OK',[('Content-Type','text/html')])
    return [b'<h1>Hello, </h1>']