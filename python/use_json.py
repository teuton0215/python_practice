#/use/env/python3
# -*- coding: utf-8 -*-
import json
#Python对象与json的转换
data = dict(name = 'Bob',age = 20, score = 88)
d = json.dumps(data)
print('JSON data is a str:',d)
reborn = json.loads(d)
print(reborn)


class Student(object):
    def __init__(self,name,age,score):
        self.name  = name
        self.age = age
        self.score = score
    #def __str__(self):
       # return  'Sturent object(%s, %s, %s)' % (self.name,self.age,self.score)
s = Student('Bob',20,88)
std_data  =  json.dumps(s,default= lambda  obj: obj.__dict__)
print('Dump Student:', std_data)
rebuild = json.loads(std_data, object_hook=lambda d: Student(d['name'], d['age'], d['score']))
print(rebuild)
