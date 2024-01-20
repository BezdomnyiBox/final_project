from peewee import *
from Models.base_model import BaseModel


class MasterModel(BaseModel):
       master_id = AutoField(column_name='master_id')
       master_name = TextField(column_name='master_name', null=True)
       master_phone = IntegerField(column_name='master_phone', null=True)
       master_exp = IntegerField(column_name='master_exp', null=True)

       class Meta:
              table_name = 'masters'