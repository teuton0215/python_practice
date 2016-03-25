#/use/bin/env  oyhton3
# -*- coding: utf-8 -*-
import  pickle
#pickle.dumps()方法把任意对象序列化成一个bytes，然后把这个bytes写入文件。
data  = dict(name = 'Bob',age=20,score=88)
d = pickle.dumps(data)
print(d)
#反序列化出对象
reborn = pickle.loads(d)
print(reborn)
