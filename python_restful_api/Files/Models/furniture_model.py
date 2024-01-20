from peewee import *
from Models.base_model import BaseModel
from Models.type_model import TypeModel
from Models.color_model import ColorModel

class FurnitureModel(BaseModel):
       furniture_id = AutoField(column_name='furniture_id')
       furniture_name = TextField(column_name='furniture_name', null=True)
       furniture_type = ForeignKeyField(TypeModel, to_field='type_id')
       furniture_color = ForeignKeyField(ColorModel, to_field='color_id')
       furniture_length = IntegerField(column_name='furniture_length', null=True)
       furniture_width = IntegerField(column_name='furniture_width', null=True)
       furniture_height = IntegerField(column_name='furniture_height', null=True)
       furniture_price = IntegerField(column_name='furniture_price', null=True)
       
       class Meta:
              table_name = 'furnitures'