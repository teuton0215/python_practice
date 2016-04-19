#/user/bin/env python3
# -*- coding:utf-8 -*-

#客户端向服务器端发起请求
# 导入socket库:
import socket

# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)           #AF_INET指定使用IPv4协议，如果使用Ipv6,就指定为AF_INET6

# 建立连接:
s.connect(('www.sina.com.cn', 80))              #80端口是Web服务的标准端口

# 发送数据:
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# 接收数据:
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break

data = b''.join(buffer)

# 关闭连接:
s.close()

header, html = data.split(b'\r\n\r\n', 1)    #split返回分割后的字符串列表。
#将头文件打印出来
print(header.decode('utf-8'))

# 把页面接收的数据写入文件
with open('sina.html', 'wb') as f:
    f.write(html)