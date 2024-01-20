from peewee import *
from Models.base_model import BaseModel

class ClientModel(BaseModel):
       client_id = AutoField(column_name='client_id')
       client_name = TextField(column_name='client_name', null=True)
       client_phone = IntegerField(column_name='client_phone', null=True)
       client_address = TextField(column_name='client_address', null=True)
             
       class Meta:
              table_name = 'clients'