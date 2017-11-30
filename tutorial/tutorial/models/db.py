from peewee import *

database = MySQLDatabase('spiders', **{'password': 'zongwen123', 'host': '120.27.46.39', 'user': 'wenwen', 'port': 3306})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Bilibili(BaseModel):
    name = CharField(null=True)

    class Meta:
        db_table = 'bilibili'

