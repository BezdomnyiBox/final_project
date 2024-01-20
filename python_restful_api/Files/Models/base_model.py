from peewee import *

def get_db_connection_peewee():
        conn_peewee = SqliteDatabase("furniture_company.sqlite")
        return conn_peewee

class BaseModel(Model):
       class Meta:
             database = get_db_connection_peewee()
             
