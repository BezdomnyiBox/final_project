from peewee import *
from Models.base_model import BaseModel

class ColorModel(BaseModel):
       color_id = AutoField(column_name='color_id')
       color_name = TextField(column_name='color_name', null=True)
       
       class Meta:
              table_name = 'colors'
