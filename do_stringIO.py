#/use/bin/env python3
# -*- coding: utf-8 -*-
from io import  StringIO

f = StringIO('Hello!')
f.write('ello')
print(f.getvalue())

#read from StringIO
f = StringIO('Hello!\nHi!\nGoodbay!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())