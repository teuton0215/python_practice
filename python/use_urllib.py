#!/user/bin/env python3
# -*-  coding: utf-8 -*-

from urllib import  request
#向URL发送请求
req = request.Request('http://www.douban.com/')
#User-Agent是用来识别有浏览器
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    '''with ...as de 用法：用去取代try ...finally...
    try:
    f = open('/path/to/file', 'r')
    print(f.read())
finally:
    if f:
        f.close()
        '''
   # data = f.read()
    print('Status:', f.status, f.reason)
    for k ,v in f.getheaders():
        print('%s: %s:' % (k, v))
    print('data:',f.read().decode('utf-8'))