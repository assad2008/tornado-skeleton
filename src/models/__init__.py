#/usr/bin/python
# coding=utf-8

from peewee import MySQLDatabase, Model
from config.db import *

db_master = MySQLDatabase(DB_NAME, host=DB_HOST, port=DB_PORT, user=DB_USER,
                          passwd=DB_PASSWD)
db_master.connect()


class BaseModel(Model):

    class Meta:
        database = db_master
