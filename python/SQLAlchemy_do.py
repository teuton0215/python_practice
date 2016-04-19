#!/user/env/bin python3
#-*- coding:utf-8 -*-

from sqlalchemy import  Column,String,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative  import declarative_base

#创建对象的基类
Base = declarative_base()

#定义User对象
class User(Base):
    pass