from peewee import *
from Models.base_model import BaseModel

class TypeModel(BaseModel):
       type_id = AutoField(column_name='type_id')
       type_name = TextField(column_name='type_name', null=True)  

       class Meta:
              table_name = 'types'