from peewee import *
from Models.base_model import BaseModel

class StepModel(BaseModel):
       step_id = AutoField(column_name='step_id')
       step_name = TextField(column_name='step_name', null=True)

       class Meta:
              table_name = 'steps'