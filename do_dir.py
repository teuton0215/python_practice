#/use/bin/env python3
# -*- coding: utf-8 -*-

import  os
#查看当前系统类型
print(os.name)
#查看当前文件的绝对路径
print(os.path.abspath('.'))
#在某目录下创建新目录，首先拜新目录的完整路径表示出来
#然后创建目录
os.path.join('D:/','test')
os.mkdir('D:/test')
#删除目录
os.rmdir('D:/test')
#对文件重命名(当前目录下)
os.rename('test.txt','new.txt')
#删除文件
os.remove('test.py')

